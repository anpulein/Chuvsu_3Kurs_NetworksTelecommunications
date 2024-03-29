WINDOW_POSITION = (200, 200)
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 900
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)
WINDOW_TITLE = 'Lab 7'

# Сцены
DEMO_SCENE = 'data/scenes/demo_scene.json'
BIG_SCENE = 'data/scenes/big_scene.json'
SMALL_SCENE = 'data/scenes/small_scene.json'
USING_SCENE_FILENAME = SMALL_SCENE
MODELS_FILENAME = 'data/models.json'

# Цвета
WHITE = [1, 1, 1, 1]
BLACK = [0, 0, 0, 1]
RED = [1, 0, 0, 1]
GREEN = [0, 1, 0, 1]
BLUE = [0, 0, 1, 1]
NAVY_BLUE = [0.23, 0.23, 1, 1]
GRAY = [0.5, 0.5, 0.5, 1]
DARK_GRAY = [0.2, 0.2, 0.2, 1]
LIME = [0.2, 0.8, 0.2, 1]
DARK_BROWN = [0.2, 0.2, 0.1, 1]
SCARLET = [0.95, 0.13, 0.13, 1]

# Скорость движения
OBJECT_SPEED_X = 0.2
OBJECT_SPEED_Y = 0.1

# Шаг при повороте, в градусах/секунду
ANGLE_STEP = 0.1
# Шаг при движении вперёд/назад
MOVE_STEP = 1

CUBE_VERTICES = [
    # передняя грань(два треугольника)
    -0.5, +0.5, +0.5, -0.5, -0.5, +0.5, +0.5, +0.5, +0.5,
    +0.5, +0.5, +0.5, -0.5, -0.5, +0.5, +0.5, -0.5, +0.5,
    # задняя грань(два треугольника)
    +0.5, +0.5, -0.5, +0.5, -0.5, -0.5, -0.5, +0.5, -0.5,
    -0.5, +0.5, -0.5, +0.5, -0.5, -0.5, -0.5, -0.5, -0.5,
    # правая грань(два треугольника)
    +0.5, -0.5, +0.5, +0.5, -0.5, -0.5, +0.5, +0.5, +0.5,
    +0.5, +0.5, +0.5, +0.5, -0.5, -0.5, +0.5, +0.5, -0.5,
    # левая грань(два треугольника)
    -0.5, +0.5, +0.5, -0.5, +0.5, -0.5, -0.5, -0.5, +0.5,
    -0.5, -0.5, +0.5, -0.5, +0.5, -0.5, -0.5, -0.5, -0.5,
    # верхняя грань(два треугольника)
    -0.5, +0.5, -0.5, -0.5, +0.5, +0.5, +0.5, +0.5, -0.5,
    +0.5, +0.5, -0.5, -0.5, +0.5, +0.5, +0.5, +0.5, +0.5,
    # нижняя грань(два треугольника)
    -0.5, -0.5, +0.5, -0.5, -0.5, -0.5, +0.5, -0.5, +0.5,
    +0.5, -0.5, +0.5, -0.5, -0.5, -0.5, +0.5, -0.5, -0.5
]

MOUSE_LEFT_BUTTON = 0
MOUSE_WHEEL_BUTTON = 1
MOUSE_RIGHT_BUTTON = 2
MOUSE_BUTTON_PRESSED = 0
MOUSE_BUTTON_NOT_PRESSED = 1
