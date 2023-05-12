import pyrr
from OpenGL.GL import (
    glClearColor, glClear, glEnable, glGetUniformLocation, glUniformMatrix4fv, glUniform4f,
    GL_FALSE, GL_COLOR_BUFFER_BIT, GL_DEPTH_BUFFER_BIT, GL_DEPTH_TEST
)

from const import WHITE
from .camera import camera
from .light import light
from .shader import shader
from .state import state

__all__ = [
    'render_manager'
]


class RenderManager:
    def __init__(self):
        self.shader = shader
        self.camera = camera
        self.graphic_objects = []

    def start(self):
        # Очистка буфера кадра
        glClearColor(*WHITE)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        # Включение буфера теста глубины
        glEnable(GL_DEPTH_TEST)

        self.graphic_objects = []

    def add_to_render_queue(self, graphic_object):
        self.graphic_objects.append(graphic_object)

    def finish(self):
        # Матрица проекции
        projection = pyrr.matrix44.create_perspective_projection_matrix(
            45, state.window_width / state.window_height, 0.1, 200.0
        )
        # Матрица вида
        view = camera.get_view_matrix()

        # Активация шейдера
        self.shader.activate()
        proj_loc = glGetUniformLocation(self.shader.program, 'projection')
        # view_model_loc = glGetUniformLocation(self.shader.program, 'view_model')
        many_view_model_loc = glGetUniformLocation(self.shader.program, 'many_view_model')

        light_ambient_loc = glGetUniformLocation(self.shader.program, 'lAmbient')
        light_diffuse_loc = glGetUniformLocation(self.shader.program, 'lDiffuse')
        light_specular_loc = glGetUniformLocation(self.shader.program, 'lSpecular')
        light_position_loc = glGetUniformLocation(self.shader.program, 'lPosition')

        glUniform4f(light_ambient_loc, *light.ambient)
        glUniform4f(light_diffuse_loc, *light.diffuse)
        glUniform4f(light_specular_loc, *light.specular)

        sorted_go = sorted(self.graphic_objects)

        # Предыдущие материал, текстура, меш
        prev_material = None
        prev_texture = None
        prev_mesh = None
        many_view_model = []

        # Статистика
        materials_changed = 0
        textures_changed = 0

        for go in sorted_go:
            # Матрица модели
            model = go.model_matrix

            view_model = view * model
            glUniformMatrix4fv(proj_loc, 1, GL_FALSE, projection)

            light_vector = pyrr.Vector4(light.direction)
            light_pos = view_model * light_vector

            glUniform4f(light_position_loc, *light_pos)

            # if go.material != prev_material:
            #     if prev_material is not None:
            #         prev_material.apply(self.shader)
            #     prev_material = go.material
            #     materials_changed += 1
            # if go.texture != prev_texture:
            #     if prev_texture is not None:
            #         prev_texture.apply()
            #     prev_texture = go.texture
            #     textures_changed += 1
            # many_view_model = [view_model]
            # glUniformMatrix4fv(many_view_model_loc, len(many_view_model), GL_FALSE, *many_view_model)
            # go.mesh.draw_many(len(many_view_model))
            if go.mesh != prev_mesh:
                if len(many_view_model):
                    for i in range(len(many_view_model)):
                        many_view_model_loc = glGetUniformLocation(self.shader.program, f'many_view_model[{i}]')
                        glUniformMatrix4fv(many_view_model_loc, 1, GL_FALSE, many_view_model[i])
                    prev_mesh.draw_many(len(many_view_model))
                many_view_model = [view_model]
                prev_mesh = go.mesh
            else:
                many_view_model.append(view_model)
        # prev_material.apply(self.shader)
        # prev_texture.apply()
        # for i in range(len(many_view_model)):
        #     many_view_model_loc = glGetUniformLocation(self.shader.program, f'many_view_model[{i}]')
        #     glUniformMatrix4fv(many_view_model_loc, 1, GL_FALSE, many_view_model[i])
        # prev_mesh.draw_many(len(many_view_model))
        state.materials_changed = materials_changed
        state.textures_changed = textures_changed


render_manager = RenderManager()
