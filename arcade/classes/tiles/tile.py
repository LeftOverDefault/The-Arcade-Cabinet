from arcade.utils.imports import *


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((config["tile_size"], config["tile_size"]))
        self.image = pygame.transform.scale_by(self.image, config["scale_factor"])
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(topleft=position)