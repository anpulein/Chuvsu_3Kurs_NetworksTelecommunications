import json

import pyrr

import const
import utils
from .camera import camera
from .graphic_object import GraphicObject, GraphicObjectType
from .light import light
from .render_manager import render_manager
from .resource_manager import resource_manager
from .shader import shader
from .state import state

__all__ = [
    'scene'
]


class Scene:
    """Сцена"""

    def __init__(self, filename, models_filename, camera_, light_):
        self._filename = filename
        self._models_filename = models_filename
        self._camera = camera_
        self._light = light_
        self._rendered_object_count = 0

        self._graphic_objects = []
        self._description = None
        self._models_description = None
        self._load()

    def _load_models(self):
        """Загрузка данных о моделях"""
        with open(self._models_filename) as file:
            description = json.load(file)
        self._models_description = description

    def _load(self):
        """Загрузка данных сцены"""
        self._load_models()
        with open(self._filename) as file:
            description = json.load(file)
        self.description = description

        for go_description in self.description:
            self._graphic_objects.append(self._create_graphic_object(go_description))

    def _create_graphic_object(self, go_description):
        """Создание графического объекта по идентификатору в json-файле"""
        model_name = go_description.get('model')
        model = self._models_description.get(model_name)

        position = go_description.get('position')
        angle = go_description.get('angle')
        type_name = model.get('type').replace(' ', '_')
        dimensions = model.get('dimensions')
        mesh_filename = model.get('mesh')
        texture_filename = model.get('texture')
        material_filename = model.get('material')

        mesh = resource_manager.get_or_create_mesh(mesh_filename)
        texture = resource_manager.get_or_create_texture(texture_filename)
        material = resource_manager.get_or_create_material(material_filename)
        type_ = getattr(GraphicObjectType, type_name)

        graphic_object = GraphicObject(
            shader=shader,
            position=position,
            angle=angle,
            mesh=mesh,
            texture=texture,
            material=material,
            type_=type_,
            dimensions=dimensions,
        )
        return graphic_object

    def _frustum_calling_test(self, graphic_object: GraphicObject):
        """Определение, попадает ли объект в усечённую пирамиду видимости"""
        projection = pyrr.matrix44.create_perspective_projection_matrix(
            45, state.window_width / state.window_height, 1, 500.0
        )
        transposed = graphic_object.model_matrix.transpose()
        pvm = projection * self._camera.get_view_matrix() * transposed
        bounding_volume_coords = []
        for coords in graphic_object.bounding_volume:
            bounding_volume_coords.append(pvm * coords)

        right_count = len(list(filter(lambda coord: coord.x > coord.w, bounding_volume_coords)))
        if right_count == 8:
            return False
        left_count = len(list(filter(lambda coord: coord.x < -coord.w, bounding_volume_coords)))
        if left_count == 8:
            return False
        up_count = len(list(filter(lambda coord: coord.y > coord.w, bounding_volume_coords)))
        if up_count == 8:
            return False
        down_count = len(list(filter(lambda coord: coord.y < -coord.w, bounding_volume_coords)))
        if down_count == 8:
            return False
        far_count = len(list(filter(lambda coord: coord.z > coord.w, bounding_volume_coords)))
        if far_count == 8:
            return False
        near_count = len(list(filter(lambda coord: coord.z < -coord.w, bounding_volume_coords)))
        if near_count == 8:
            return False
        return True

    def _lod_test(self, graphic_object: GraphicObject):
        """Определение видимости объекта в зависимости от дистанции до него"""
        if graphic_object.type_ in [GraphicObjectType.building, GraphicObjectType.road]:
            # Выводим всегда
            return True
        dist = utils.distance(self._camera.camera_pos, graphic_object.position)
        # dist_scale = 10  # Для удобства тестов
        dist_scale = 1  # Для удобства тестов
        if graphic_object.type_ == GraphicObjectType.vehicle:
            return dist <= 50 * dist_scale
        if graphic_object.type_ == GraphicObjectType.big_nature:
            return dist <= 35 * dist_scale
        if graphic_object.type_ == GraphicObjectType.small_nature:
            return dist <= 20 * dist_scale
        if graphic_object.type_ == GraphicObjectType.big_prop:
            return dist <= 40 * dist_scale
        if graphic_object.type_ == GraphicObjectType.medium_prop:
            return dist <= 30 * dist_scale
        if graphic_object.type_ == GraphicObjectType.small_prop:
            return dist <= 20 * dist_scale
        return False

    def _render_test(self, graphic_object):
        if not self._lod_test(graphic_object):
            return False
        # return True
        return self._frustum_calling_test(graphic_object)

    def draw(self):
        """Вывод всей сцены"""
        # Начинаем вывод сцены в новом кадре
        self._rendered_object_count = 0

        # Добавляем в очередь рендера с учётом оптимизации
        for graphic_object in self._graphic_objects:
            if not (self._render_test(graphic_object)):
                continue
            self._rendered_object_count += 1
            render_manager.add_to_render_queue(graphic_object)

    @property
    def description_verbose(self):
        """Информация о сцене"""
        return f'[Rendered {self._rendered_object_count} of {len(self._graphic_objects)}]'


scene = Scene(
    filename=const.USING_SCENE_FILENAME,
    models_filename=const.MODELS_FILENAME,
    camera_=camera,
    light_=light,
)
