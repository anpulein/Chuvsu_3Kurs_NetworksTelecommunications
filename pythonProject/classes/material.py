import json

from OpenGL.GL import glGetUniformLocation, glUniform4f, glUniform1f

__all__ = [
    'Material',
]


class Material:
    """Материал"""

    def __init__(self, filename):
        # Файл, в котором хранится описание материала
        self._filename = filename
        # Устанавливаем заглушки
        # Фоновая составляющая
        self.ambient = (0, 0, 0, 1)
        # Диффузная составляющая
        self.diffuse = (0, 0, 0, 1)
        # Зеркальная составляющая
        self.specular = (0, 0, 0, 1)
        # Блеск
        self.shininess = 32
        self.load()

    def load(self):
        """Загрузка материала из файла"""
        with open(self._filename) as file:
            description = json.load(file)
        self.ambient = description.get('ambient')
        self.diffuse = description.get('diffuse')
        self.specular = description.get('specular')
        self.shininess = description.get('shininess')

    def apply(self, shader):
        ambient_loc = glGetUniformLocation(shader.program, 'mAmbient')
        diffuse_loc = glGetUniformLocation(shader.program, 'mDiffuse')
        specular_loc = glGetUniformLocation(shader.program, 'mSpecular')
        shininess_loc = glGetUniformLocation(shader.program, 'mShininess')

        glUniform4f(ambient_loc, *self.ambient)
        glUniform4f(diffuse_loc, *self.diffuse)
        glUniform4f(specular_loc, *self.specular)
        glUniform1f(shininess_loc, self.shininess)

    @property
    def filename(self):
        return self._filename

    def __lt__(self, other):
        return self._filename < other.filename

    def __gt__(self, other):
        return self._filename > other.filename

    def __eq__(self, other):
        return self._filename == other.filename

    def __ne__(self, other):
        try:
            return self._filename != other.filename
        except:
            return True
