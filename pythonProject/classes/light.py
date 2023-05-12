import const

__all__ = [
    'light'
]


class Light:
    def __init__(self, direction, ambient, diffuse, specular):
        self.direction = direction
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular


light = Light(
    direction=(20, 20, 15, 1),
    ambient=const.WHITE,
    diffuse=const.WHITE,
    specular=const.WHITE,
)
