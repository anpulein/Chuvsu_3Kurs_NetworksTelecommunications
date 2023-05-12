import logging
import sys

from OpenGL.GL import glGetString, GL_VERSION
from OpenGL.GLUT import (
    glutInit, glutInitDisplayMode, GLUT_RGBA, GLUT_DOUBLE, GLUT_DEPTH, GLUT_STENCIL, GLUT_MULTISAMPLE,
    glutInitContextVersion, glutInitContextProfile, GLUT_CORE_PROFILE, glutInitWindowPosition, glutInitWindowSize,
    glutCreateWindow, glutDisplayFunc, glutReshapeFunc, glutIdleFunc, glutMainLoop, glutMouseWheelFunc,
    glutMouseFunc
)


import callbacks
import const
from classes import shader, state

if __name__ == '__main__':
    logging.basicConfig(format='%(message)s', datefmt='%m.%d.%Y %H:%M:%S', level=logging.NOTSET)

    # Инициализация библиотеки glut
    glutInit(sys.argv)
    # Инициализация дисплея
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH | GLUT_STENCIL | GLUT_MULTISAMPLE)

    # Требования к версии OpenGL
    glutInitContextVersion(3, 3)
    glutInitContextProfile(GLUT_CORE_PROFILE)

    # region Создание окна
    # Установка левого верхнего угла окна
    glutInitWindowPosition(*const.WINDOW_POSITION)
    # Установка размера окна
    glutInitWindowSize(*const.WINDOW_SIZE)
    # Создание окна
    glutCreateWindow(state.window_title)
    # endregion

    # Логируем текущую версию OpenGl
    # logging.info(f'OpenGl version = {glGetString(GL_VERSION)}')
    print(f'OpenGl version = {glGetString(GL_VERSION)}')

    # Загрузка Шейдера
    shader.load()

    # Установка функции, которая будет вызываться для перерисовки окна
    glutDisplayFunc(callbacks.display)
    # Установка функции, которая будет вызываться при изменении параметров окна
    glutReshapeFunc(callbacks.reshape)
    glutMouseFunc(callbacks.mouse_pressed)
    # Установка функции, которая вызывается каждый раз, когда процессор простаивает
    glutIdleFunc(callbacks.simulation)

    # Основной цикл обработки сообщений ОС
    glutMainLoop()
