from arcade.classes.tile.tile import Tile
from arcade.utils.imports import *


class StaticTile(Tile):
    def __init__(self, image, tile_index, position, group, config) -> None:
        super().__init__(position=position, group=group, config=config)
        self.image = image
        self.tile_index = tile_index
        self.rect = self.image.get_rect(topleft=position)