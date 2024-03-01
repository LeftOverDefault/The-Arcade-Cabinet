from arcade.utils.imports import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, position) -> None:
        super().__init__()
        self.image = pygame.Surface((16, 16))
        self.image.fill((16, 50, 255))
        self.rect = self.image.get_rect(topleft=position)