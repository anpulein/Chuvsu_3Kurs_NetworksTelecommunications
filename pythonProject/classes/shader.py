from OpenGL.GL import (
    glCreateProgram, glUseProgram, GL_VERTEX_SHADER, GL_FRAGMENT_SHADER, shaders
)

__all__ = [
    'Shader',
    'shader'
]


class Shader:
    """Шейдер"""

    def __init__(self, vertex_shader_filename, fragment_shader_filename):
        # Имена внешних файлов с кодом шейдеров
        self.vertex_shader_filename = vertex_shader_filename
        self.fragment_shader_filename = fragment_shader_filename

        # Код шейдеров
        self.vertex_shader_data = ''
        self.fragment_shader_data = ''

        # Шейдеры
        self.vertex_shader = None
        self.fragment_shader = None
        self.program = None

    def load(self):
        """Загрузка шейдера из внешних файлов"""
        with open(self.vertex_shader_filename) as vertex_file, open(self.fragment_shader_filename) as fragment_file:
            self.vertex_shader_data = vertex_file.read()
            self.fragment_shader_data = fragment_file.read()

        # Обязательно после logging.info(f'OpenGl version = {glGetString(GL_VERSION)}')
        self.program = glCreateProgram()
        self.vertex_shader = shaders.compileShader(self.vertex_shader_data, GL_VERTEX_SHADER)
        self.fragment_shader = shaders.compileShader(self.fragment_shader_data, GL_FRAGMENT_SHADER)

        self.program = shaders.compileProgram(self.vertex_shader, self.fragment_shader)

    def activate(self):
        """Выбор шейдера в качестве текущего"""

        # Собираем шейдерную программу
        glUseProgram(self.program)

    def deactivate(self):
        """Отключение шейдера"""
        glUseProgram(0)


shader = Shader('data/shader/My.vsh', 'data/shader/My.fsh')
