import numpy
from OpenGL.GL import (
    glBindTexture, glTexParameteri, glTexImage2D, glGenTextures,
    GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT, GL_TEXTURE_WRAP_T, GL_TEXTURE_MIN_FILTER,
    GL_LINEAR, GL_UNSIGNED_BYTE, GL_TEXTURE_MAG_FILTER, GL_RGBA
)
from PIL import Image

__all__ = [
    'Texture',
]


class Texture:
    """Текстура"""

    def __init__(self, file_name):
        self.__file_name = file_name
        # Индекс текстурного объекта
        self.__texture_index = None
        self.__image_data = None
        self.__image = None
        self.__flipped_image = None
        self.__flipped_image_data = None
        self.__load()
        self.__texture = None

    def __load(self):
        """Загрузка текстуры из файла"""
        self.__image = Image.open(self.__file_name)
        self.__image_data = self.__image.tobytes()
        self.__flipped_image = self.__image.transpose(Image.FLIP_TOP_BOTTOM)
        self.__flipped_image_data = numpy.array(list(self.__flipped_image.getdata()), numpy.uint8)

    @property
    def image(self):
        return self.__image

    @property
    def image_data(self):
        return self.__image_data

    @property
    def filename(self):
        return self.__file_name

    def apply(self):
        """Применение текстуры (привязка к текстурному блоку и установка параметров)"""
        if self.__texture is None:
            self.__texture = glGenTextures(1)
            glBindTexture(GL_TEXTURE_2D, self.__texture)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
            glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, self.__image.width, self.__image.height, 0, GL_RGBA, GL_UNSIGNED_BYTE,
                     self.__flipped_image_data)

    def __lt__(self, other):
        return self.__file_name < other.filename

    def __gt__(self, other):
        return self.__file_name > other.filename

    def __eq__(self, other):
        return self.__file_name == other.filename

    def __ne__(self, other):
        try:
            return self.__file_name != other.filename
        except:
            return True
