from framework.classes.tile.static_tile import StaticTile
from framework.utils.imports import *


class Chunk(pygame.sprite.Group):
    def __init__(self, layer, position, tiles, display_surface, camera, config) -> None:
        super().__init__()
        self.layer = layer
        self.position = position
        self.tiles = tiles
        self.display_surface = display_surface
        self.camera = camera
        self.config = config

        self.visible = False

        self.in_left = False
        self.in_right = False
        self.in_top = False
        self.in_bottom = False

        self.create_tiles()


    # def __str__(self) -> str:
    #     return f"Chunk({self.position}, {self.tiles})"


    def create_tiles(self):
        for tile in self.tiles:
            tile_x = int(tile["position"][0] + int(self.position[0]) * self.config.chunk_size) * self.config.tile_size
            tile_y = int(tile["position"][1] + int(self.position[1]) * self.config.chunk_size) * self.config.tile_size
            tile = StaticTile(self.layer.tileset[tile["value"]], [tile_x, tile_y], self, self.config)


    def update(self, delta_time):
        camera_left = self.camera.offset.x
        camera_right = self.camera.offset.x + self.display_surface.get_width()
        camera_top = self.camera.offset.y
        camera_bottom = self.camera.offset.y + self.display_surface.get_height()

        self.in_left = camera_left <= (int(self.position[0]) * self.config.chunk_size * self.config.tile_size) + (self.config.chunk_size * self.config.tile_size) - self.config.chunk_size
        self.in_right = camera_right >= (int(self.position[0]) * self.config.chunk_size * self.config.tile_size) - self.config.chunk_size
        self.in_top = camera_top <= (int(self.position[1]) * self.config.chunk_size * self.config.tile_size) + (self.config.chunk_size * self.config.tile_size) - self.config.chunk_size
        self.in_bottom = camera_bottom >= (int(self.position[1]) * self.config.chunk_size * self.config.tile_size) - self.config.chunk_size

        for sprite in self:
            sprite.update(delta_time)


    def render(self) -> None:
        if self.in_left and self.in_right and self.in_top and self.in_bottom:
            self.visible = True
        else:
            self.visible = False