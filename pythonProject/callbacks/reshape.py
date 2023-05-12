from OpenGL.GL import glViewport

from classes import state
__all__ = [
    'reshape'
]


def reshape(width, height):
    """Изменение размеров окна"""
    # Установка новой области просмотра, равной всей области окна
    glViewport(0, 0, width, height)
    state.window_width = width
    state.window_height = height
