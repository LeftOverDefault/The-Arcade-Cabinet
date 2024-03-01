from world_engine.utils.imports import *


class Layer:
# class Layer(pygame.sprite.Group):
    def __init__(self, collidable, y_sorted) -> None:
        # super().__init__()
        self.collidable = collidable
        self.y_sorted = y_sorted

        self.sprites = []

    def add(self, sprite):
        sprite = sprite
        position = sprite.rect.topleft
        sprite.rect = sprite.image.get_rect(topleft=(position[0] * 16, position[1] * 16))

        self.sprites.append(sprite)

    def __str__(self) -> str:
        return self.sprites

    def __iter__(self):
        return iter(self.sprites)