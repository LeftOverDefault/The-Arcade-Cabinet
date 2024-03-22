from arcade_cabinet_LeftOverDefault.arcade.classes.camera import Camera
from arcade_cabinet_LeftOverDefault.arcade.classes.layer import Layer
from arcade_cabinet_LeftOverDefault.arcade.classes.player import Player
from arcade_cabinet_LeftOverDefault.arcade.classes.tile.static_tile import StaticTile
from arcade_cabinet_LeftOverDefault.arcade.func.import_cut_graphics import import_cut_graphics
from arcade_cabinet_LeftOverDefault.arcade.utils.imports import *


class World:
    def __init__(self, display_surface, config) -> None:
        self.display_surface = display_surface
        self.config = config

        self.camera = Camera(self.display_surface)
        self.player = Player(config.player_path, (288 / 2, 162 / 2), self.camera.y_sort_layer)

        self.layers = {}
        self.tilesets = {}

        self.convert_world_layout()


    def convert_world_layout(self) -> None:
        for tileset in self.config.tilesets:
            self.tilesets[tileset] = import_cut_graphics(self.config.tilesets[tileset], self.config)

        for _, __, layers in os.walk(self.config.world_directory):
            for layer in layers:
                with open(f"{self.config.world_directory}{layer}", "r") as file:
                    layer_dict = json.load(file)
                    current_layer = Layer(layer_dict["y-sorted"], layer_dict["collidable"])
                    chunk_data = {}
                    for chunk in layer_dict["layer_chunks"].keys():
                        chunk_x = chunk.split(";")[0]
                        chunk_y = chunk.split(";")[1]
                        chunk_data[(chunk_x, chunk_y)] = self.generate_chunks(layer_dict, chunk_x, chunk_y)
                    self.layers[current_layer] = {"layer_name": layer_dict["layer_name"], "index": layer_dict["layer_index"], "tileset": layer_dict["layer_tileset"], "chunk_data": chunk_data}


    def generate_chunks(self, layer, x, y) -> dict:
        chunk_data = []
        for chunk_x_position in range(0, self.config.chunk_size):
            for chunk_y_position in range(0, self.config.chunk_size):
                tile_position = f"{chunk_x_position};{chunk_y_position}"
                if tile_position in layer["layer_chunks"][f"{x};{y}"]:
                    tile_value = layer["layer_chunks"][f"{x};{y}"][tile_position]
                    chunk_data.append(([chunk_x_position, chunk_y_position], tile_value))
        return chunk_data


    def render_chunks(self) -> None:
        for layer, layer_data in self.layers.items():
            for chunk in layer_data["chunk_data"]:
                camera_left = self.camera.offset.x
                camera_right = self.camera.offset.x + self.display_surface.get_width()
                camera_top = self.camera.offset.y
                camera_bottom = self.camera.offset.y + self.display_surface.get_height()

                chunk_x_offset = int(chunk[0])
                chunk_y_offset = int(chunk[1])

                in_left = camera_left <= (chunk_x_offset) + (self.config.chunk_size * self.config.tile_size) - self.config.chunk_size
                in_right = camera_right >= chunk_x_offset - self.config.chunk_size
                in_top = camera_top <= (chunk_y_offset) + (self.config.chunk_size * self.config.tile_size) - self.config.chunk_size
                in_bottom = camera_bottom >= chunk_y_offset - self.config.chunk_size

                tiles = layer_data["chunk_data"][chunk]

                if in_right and in_left and in_bottom and in_top:
                    for tile in tiles:
                        tile_x = round((tile[0][0] + (chunk_x_offset * self.config.chunk_size)) * self.config.tile_size)
                        tile_y = round((tile[0][1] + (chunk_y_offset * self.config.chunk_size)) * self.config.tile_size)
                        StaticTile(self.tilesets[layer_data["tileset"]][tile[1]], (tile_x, tile_y), layer_data["layer_name"], layer, self.config)

            self.camera.add_group(layer, self.player)
            layer.empty()


    def render(self) -> None:
        self.camera.empty()
        self.render_chunks()
        self.camera.draw(self.player)


    def update(self, delta_time) -> None:
        self.camera.update(delta_time)