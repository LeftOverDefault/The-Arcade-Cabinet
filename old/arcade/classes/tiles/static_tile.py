from arcade.classes.tiles.tile import Tile
from arcade.utils.imports import *


class StaticTile(Tile):
    def __init__(self, image, position, group) -> None:
        super().__init__(position, group)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale_by(surface=self.image, factor=config["scale_factor"])
        self.collidable = True