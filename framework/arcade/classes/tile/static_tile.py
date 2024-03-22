from framework.arcade.classes.tile.tile import Tile
from framework.arcade.utils.imports import *


class StaticTile(Tile):
    def __init__(self, image, position, layer_name, group, config) -> None:
        super().__init__(position=position, group=group, config=config)
        self.image = image
        self.layer_name = layer_name
        self.rect = self.image.get_rect(center=position)