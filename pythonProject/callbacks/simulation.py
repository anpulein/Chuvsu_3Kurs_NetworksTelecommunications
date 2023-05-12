from OpenGL.GLUT import glutPostRedisplay
from win32api import GetAsyncKeyState
from win32con import MOUSE_MOVED, VK_UP, VK_DOWN, VK_RIGHT, VK_LEFT

import utils
from callbacks.mouse import mouse_moved
from classes import state, camera

__all__ = [
    'simulation'
]


def simulation():
    """Изменение параметров сцены"""
    simulation_time = utils.get_simulation_time()
    state.simulation_time = simulation_time
    if GetAsyncKeyState(MOUSE_MOVED):
        mouse_moved()
    if GetAsyncKeyState(VK_UP):
        camera.move_forward()
    if GetAsyncKeyState(VK_DOWN):
        camera.move_backward()
    if GetAsyncKeyState(VK_RIGHT):
        camera.move_right()
    if GetAsyncKeyState(VK_LEFT):
        camera.move_left()
    # Перерисовка окна
    glutPostRedisplay()
