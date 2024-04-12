from framework.utils.imports import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, group, config) -> None:
        super().__init__(group)
        self.config = config
        self.image = pygame.Surface((self.config.tile_size, self.config.tile_size))
        self.rect = self.image.get_rect(center=position)