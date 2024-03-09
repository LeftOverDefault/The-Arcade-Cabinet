from arcade.func.import_cut_graphics import import_cut_graphics
from arcade.utils.imports import *


class World:
    def __init__(self, display_surface, world_data, config) -> None:
        self.display_surface = display_surface
        self.world_data = world_data
        self.chunks = []
        self.config = config

        self.test_tile = import_cut_graphics("./assets/sprite/tilesets/plains.png", self.config)

        for chunk_location in self.world_data:
            chunk = {}
            chunk_x = int(chunk_location.split(";")[0])
            chunk_y = int(chunk_location.split(";")[1])
            chunk_data = self.generate_chunk(x=chunk_x, y=chunk_y)
            chunk_x_offset = chunk_x * self.config.chunk_size * self.config.tile_size
            chunk_y_offset = chunk_y * self.config.chunk_size * self.config.tile_size
            chunk["data"] = chunk_data
            chunk["offset"] = [chunk_x_offset, chunk_y_offset]
            self.chunks.append(chunk)


    def generate_chunk(self, x, y) -> dict:
        chunk_data = []
        for chunk_x_offset in range(0, self.config.chunk_size):
            for chunk_y_offset in range(0, self.config.chunk_size):
                if f"{chunk_x_offset};{chunk_y_offset}" in self.world_data[f"{x};{y}"]:
                    tile_value = self.world_data[f"{x};{y}"][f"{chunk_x_offset};{chunk_y_offset}"]
                    chunk_x_target = chunk_x_offset
                    chunk_y_target = chunk_y_offset
                    chunk_data.append(([chunk_x_target, chunk_y_target], tile_value))
                else:
                    pass
        return chunk_data


    def render_chunk(self, chunk, chunk_offset) -> None:
        tiles = []
        for coordinate, value in chunk["data"]:
            tile_x = round(coordinate[0] * self.config.tile_size) + int(chunk_offset[0])
            tile_y = round(coordinate[1] * self.config.tile_size) + int(chunk_offset[1])
            tiles.append(([tile_x, tile_y], value))
        return tiles


    def render(self, camera_offset) -> None:
        for chunk in self.chunks:
            camera_left = camera_offset.x
            camera_right = camera_offset.x + self.display_surface.get_width()
            camera_top = camera_offset.y
            camera_bottom = camera_offset.y + self.display_surface.get_height()
            
            chunk_x_offset = chunk["offset"][0]
            chunk_y_offset = chunk["offset"][1]

            in_left = camera_left <= (chunk_x_offset) + (self.config.chunk_size * self.config.tile_size)
            in_right = camera_right >= chunk_x_offset
            in_top = camera_top <= (chunk_y_offset) + (self.config.chunk_size * self.config.tile_size)
            in_bottom = camera_bottom >= chunk_y_offset

            tiles = self.render_chunk(chunk=chunk, chunk_offset=chunk["offset"])

            if in_right and in_left and in_bottom and in_top:
                for tile in tiles:
                    if int(tile[1]) != -1:
                        self.display_surface.blit(self.test_tile[tile[1]].copy(), (tile[0][0] - camera_offset.x, tile[0][1] - camera_offset.y))