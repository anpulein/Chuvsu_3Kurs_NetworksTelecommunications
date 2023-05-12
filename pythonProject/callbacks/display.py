from OpenGL.GLUT import glutSwapBuffers, glutSetWindowTitle

from classes import *

__all__ = [
    'display',
]


def display():
    """Перерисовка окна"""
    # Начинаем вывод нового кадра
    render_manager.start()
    # Выводим сцену
    scene.draw()
    # Завершаем построение кадра
    render_manager.finish()

    glutSetWindowTitle(state.window_title)

    # Смена переднего и заднего буфера
    glutSwapBuffers()
