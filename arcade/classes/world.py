from arcade.classes.camera import Camera
from arcade.func.generate_chunk import generate_chunk
from arcade.func.render_chunk import render_chunk
from arcade.utils.imports import *


class World:
    def __init__(self, display_surface, world_data, config) -> None:
        self.world_data = world_data
        self.display_surface = display_surface
        self.config = config
        self.camera = Camera(self.display_surface)
        self.player = None

        self.test_tile = pygame.image.load("./assets/sprite/environment/tile.png").convert_alpha()

        self.tile_x = [x for x in range(0, 8)]
        self.tile_y = [y for y in range(0, 8)]

    
    def render(self, camera_offset):
        for chunk_location in self.world_data:
            chunk_x = int(chunk_location.split(";")[0])
            chunk_y = int(chunk_location.split(";")[1])
            chunk_coordinates = generate_chunk(config=self.config, world_data=self.world_data, x=chunk_x, y=chunk_y)
            tiles = render_chunk(config=self.config, chunk_coordinates=chunk_coordinates, chunk_x_offset=round(chunk_x / self.config.chunk_size) - camera_offset.x, chunk_y_offset=round(chunk_y / self.config.chunk_size) - camera_offset.y)

            chunk_x_offset = chunk_x * self.config.chunk_size * self.config.tile_size
            chunk_y_offset = chunk_y * self.config.chunk_size * self.config.tile_size

            camera_left = camera_offset.x
            camera_right = camera_offset.x + self.display_surface.get_width()
            camera_top = camera_offset.y
            camera_bottom = camera_offset.y + self.display_surface.get_height()

            in_left = camera_left <= (chunk_x_offset) + (self.config.chunk_size * self.config.tile_size)
            in_right = camera_right >= chunk_x_offset
            in_top = camera_top <= (chunk_y_offset) + (self.config.chunk_size * self.config.tile_size)
            in_bottom = camera_bottom >= chunk_y_offset

            if in_left and in_right:
                if in_top and in_bottom:
                    for tile, value in tiles:
                        if int(value) != -1:
                            self.display_surface.blit(source=self.test_tile.copy(), dest=tile)