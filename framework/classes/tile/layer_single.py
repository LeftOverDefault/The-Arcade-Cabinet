from framework.utils.imports import *


class LayerSingle(pygame.sprite.GroupSingle):
    def __init__(self, z_index, y_sorted, collidable) -> None:
        super().__init__()
        self.z_index = z_index
        self.y_sorted = y_sorted
        self.collidable = collidable