from arcade.utils.imports import *


class Sprite(pygame.sprite.Sprite):
    def __init__(self, path, position, group) -> None:
        super().__init__(group)
        # self.image = pygame.image.load(path).convert_alpha()
        # self.rect = self.image.get_rect(center=position)