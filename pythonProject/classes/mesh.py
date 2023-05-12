import ctypes
from dataclasses import dataclass

from OpenGL.GL import (
    glGenBuffers, glBindBuffer, glBufferData, GL_TRIANGLES, GL_ARRAY_BUFFER,
    GL_STATIC_DRAW, glEnableVertexAttribArray, glVertexAttribPointer, glDrawArraysInstanced,
    GL_FLOAT, glGenVertexArrays, glBindVertexArray, glDrawArrays, GL_FALSE
)

from .obj_loader import ObjLoader

__all__ = [
    'Mesh',
]


@dataclass
class _Vertex:
    """Вершина полигональной сетки"""
    # Геометрические координаты
    coord: list
    # Вектор нормали
    normal: list
    # Текстурные координаты нулевого текстурного блока
    texture_coord: list


class Mesh:
    """Класс для хранения Меша"""

    def __init__(self, filename):
        self.filename = filename
        self.data = ObjLoader()
        self.__load()
        self.vao = None
        self.vbo = None

    def __load(self):
        self.data.load_model(self.filename)

    def draw_one(self):
        if self.vao is None:
            self.vao = glGenVertexArrays(1)
            glBindVertexArray(self.vao)
        if self.vbo is None:
            self.vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        glBufferData(GL_ARRAY_BUFFER, self.data.model.itemsize * len(self.data.model), self.data.model, GL_STATIC_DRAW)
        # Позиция
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.data.model.itemsize * 3, ctypes.c_void_p(0))
        # glEnableVertexAttribArray(0)

        # Текстуры
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.data.model.itemsize * 2,
                              ctypes.c_void_p(len(self.data.vertex_index) * 12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.data.model.itemsize * 3,
                              ctypes.c_void_p(len(self.data.vertex_index) * 12 + len(self.data.texture_index) * 8))

        # texture.apply()
        glDrawArrays(GL_TRIANGLES, 0, len(self.data.vertex_index))

    def draw_many(self, count_=5):
        if self.vao is None:
            self.vao = glGenVertexArrays(1)
            glBindVertexArray(self.vao)
        if self.vbo is None:
            self.vbo = glGenBuffers(1)
            glBindBuffer(GL_ARRAY_BUFFER, self.vbo)

        glBufferData(GL_ARRAY_BUFFER, self.data.model.itemsize * len(self.data.model), self.data.model, GL_STATIC_DRAW)
        # Позиция
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, self.data.model.itemsize * 3, ctypes.c_void_p(0))
        # glEnableVertexAttribArray(0)

        # Текстуры
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, self.data.model.itemsize * 2,
                              ctypes.c_void_p(len(self.data.vertex_index) * 12))
        glEnableVertexAttribArray(2)
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, self.data.model.itemsize * 3,
                              ctypes.c_void_p(len(self.data.vertex_index) * 12 + len(self.data.texture_index) * 8))
        glDrawArraysInstanced(GL_TRIANGLES, 0, len(self.data.vertex_index), count_)

    def __str__(self):
        return self.filename

    def __lt__(self, other):
        return self.filename < other.filename

    def __gt__(self, other):
        return self.filename > other.filename

    def __eq__(self, other):
        return self.filename == other.filename

    def __ne__(self, other):
        try:
            return self.filename != other.filename
        except:
            return True
