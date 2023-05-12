from win32api import GetCursorPos

from classes import camera
from const import ANGLE_STEP, MOUSE_LEFT_BUTTON, MOUSE_BUTTON_PRESSED, MOUSE_BUTTON_NOT_PRESSED

__all__ = [
    'mouse_moved',
    'mouse_pressed',
]

prev_x, prev_y = GetCursorPos()
dx, dy = 0, 0
pressed = False


def mouse_pressed(button, state, x, y):
    """Вызывается при нажатии кнопок мыши"""
    global prev_x, prev_y, dx, dy, pressed
    if button == MOUSE_LEFT_BUTTON:
        if state == MOUSE_BUTTON_PRESSED:
            pressed = True
            prev_x, prev_y = GetCursorPos()
        elif state == MOUSE_BUTTON_NOT_PRESSED:
            pressed = False


def mouse_moved():
    """Вызывается при вращении мыши"""
    global prev_x, prev_y, dx, dy, pressed
    if pressed:
        x, y = GetCursorPos()
        dx = x - prev_x
        dy = y - prev_y
        camera.rotate_up_down(-dy * ANGLE_STEP)
        camera.rotate_left_right(dx * ANGLE_STEP)
        prev_x = x
        prev_y = y
