from framework.utils.imports import *


class Layer(pygame.sprite.Group):
    def __init__(self, z_index, tileset, y_sorted, collidable, chunks) -> None:
        super().__init__()
        self.z_index = z_index
        self.tileset = tileset
        self.y_sorted = y_sorted
        self.collidable = collidable
        self.chunks = chunks


    def update(self, delta_time):
        for chunk in self.chunks:
            chunk.update(delta_time)