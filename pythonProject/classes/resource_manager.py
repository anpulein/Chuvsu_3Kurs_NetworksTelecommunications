from .material import Material
from .mesh import Mesh
from .texture import Texture

__all__ = [
    'resource_manager'
]


class ResourceManager:
    """Менеджер ресурсов"""

    def __init__(self):
        self._meshes = dict()
        self._textures = dict()
        self._materials = dict()

    def get_or_create_mesh(self, filename):
        if filename in self._meshes:
            return self._meshes[filename]
        mesh = Mesh(filename)
        self._meshes[filename] = mesh
        return mesh

    def get_or_create_texture(self, filename):
        if filename in self._textures:
            return self._textures[filename]
        texture = Texture(filename)
        self._textures[filename] = texture
        return texture

    def get_or_create_material(self, filename):
        if filename in self._materials:
            return self._materials[filename]
        material = Material(filename)
        return material


resource_manager = ResourceManager()
