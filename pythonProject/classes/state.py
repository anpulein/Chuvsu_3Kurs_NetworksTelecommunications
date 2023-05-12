from const import WINDOW_TITLE, WINDOW_WIDTH, WINDOW_HEIGHT

__all__ = [
    'state'
]


class State:
    def __init__(self):
        self.simulation_time = 0
        self.window_width = WINDOW_WIDTH
        self.window_height = WINDOW_HEIGHT
        self.materials_changed = 0
        self.textures_changed = 0

    @property
    def fps(self):
        return round(1 / self.simulation_time)

    @property
    def window_title(self):
        from .scene import scene
        title = WINDOW_TITLE
        if self.simulation_time:
            title = f'{WINDOW_TITLE} [{self.fps} FPS] [matc {self.materials_changed}] [tc {self.textures_changed}]'
        title += ' ' + scene.description_verbose
        return title


state = State()
