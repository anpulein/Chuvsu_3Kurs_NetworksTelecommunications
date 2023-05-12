from enum import Enum
from math import radians, cos, sin

from pyrr import Matrix44, Vector4

__all__ = [
    'GraphicObject',
    'GraphicObjectType',
]


class GraphicObjectType(Enum):
    none = 0
    road = 1
    building = 2
    vehicle = 3
    big_nature = 4
    small_nature = 5
    big_prop = 6
    medium_prop = 7
    small_prop = 8


class GraphicObject:
    def __init__(self, shader, position, angle, mesh, texture, material, type_=None, dimensions=None,
                 vertices=None):
        self.vertices = vertices
        self.shader = shader
        self._position = position
        self._angle = angle
        self._mesh = mesh
        self._texture = texture
        self._material = material
        self._type = type_
        self._dimensions = dimensions
        # Матрица модели (Расположение объекта)
        self.model_matrix = []
        self._recalculate_model_matrix()

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, new_pos):
        self.position = new_pos

    @property
    def angle(self):
        return self._angle

    @property
    def mesh(self):
        return self._mesh

    @mesh.setter
    def mesh(self, new_mesh):
        self._mesh = new_mesh

    @property
    def texture(self):
        return self._texture

    @texture.setter
    def texture(self, new_texture):
        self._texture = new_texture

    @property
    def material(self):
        return self._material

    @material.setter
    def material(self, new_material):
        self._material = new_material

    @property
    def type_(self):
        return self._type

    @type_.setter
    def type_(self, new_type):
        self._type = new_type

    @property
    def dimensions(self):
        return self._dimensions

    def _recalculate_model_matrix(self):
        """Пересчёт model_matrix"""
        temp = Matrix44([
            Vector4([1, 0, 0, 0]),
            Vector4([0, 1, 0, 0]),
            Vector4([0, 0, 1, 0]),
            Vector4(self._position + [1]),
        ])
        rad = radians(self.angle)
        rot = Matrix44([
            Vector4([cos(rad), 0, sin(rad), 0]),
            Vector4([0, 1, 0, 0]),
            Vector4([-sin(rad), 0, cos(rad), 0]),
            Vector4([0, 0, 0, 1])
        ])
        self.model_matrix = temp * rot

    @property
    def bounding_volume(self):
        x = self.dimensions[0]
        y = self.dimensions[1]
        z = self.dimensions[2]
        return [
            Vector4([x / 2, y / 2, z / 2, 1.0]),
            Vector4([x / 2, y / 2, -z / 2, 1.0]),
            Vector4([x / 2, -y / 2, z / 2, 1.0]),
            Vector4([x / 2, -y / 2, -z / 2, 1.0]),
            Vector4([-x / 2, y / 2, z / 2, 1.0]),
            Vector4([-x / 2, y / 2, -z / 2, 1.0]),
            Vector4([-x / 2, -y / 2, z / 2, 1.0]),
            Vector4([-x / 2, -y / 2, -z / 2, 1.0]),
        ]

    def draw(self):
        pass
        # self._material.apply(self.shader)
        # self._texture.apply()
        # self._mesh.draw_one()

    def __lt__(self, other):
        # Порядок сравнения: материал, текстура, меш
        if self.material < other.material:
            return True
        elif self.material == other.material:
            if self.texture < other.texture:
                return True
            elif self.texture == other.texture:
                if self.mesh < other.mesh:
                    return True
                return False
            return False
        return False

    def __gt__(self, other):
        # Порядок сравнения: материал, текстура, меш
        if self.material > other.material:
            return True
        elif self.material == other.material:
            if self.texture > other.texture:
                return True
            elif self.texture == other.texture:
                if self.mesh > other.mesh:
                    return True
                return False
            return False
        return False

    def __eq__(self, other):
        return self.material == other.material and self.texture == other.texture and self.mesh == other.texture
