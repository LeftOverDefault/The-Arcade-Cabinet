from framework.arcade.utils.imports import *


class Layer(pygame.sprite.Group):
    def __init__(self, y_sorted, collidable) -> None:
        super().__init__()
        self.y_sorted = y_sorted
        self.collidable = collidable