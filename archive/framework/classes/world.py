from framework.classes.layer import Layer
from framework.classes.player import Player
from framework.classes.tile.layer_single import LayerSingle
from framework.func.import_cut_graphics import import_cut_graphics
from framework.classes.camera import Camera
from framework.classes.chunk import Chunk
from framework.utils.imports import *


class World:
    def __init__(self, world_name, display_surface, config) -> None:
        self.display_surface = display_surface
        self.config = config

        self.camera = Camera(self.display_surface)
        self.player = Player("./assets/sprite/entity/player/", (0, 0), self.camera)

        self.world_name = world_name

        self.convert_world_layout()


    def convert_world_layout(self) -> None:
        for directory, _, layouts in os.walk(self.config.world_directories):
            for layout in layouts:
                if layout.split("_")[0] == self.world_name:
                    with open(f"{directory}/{layout}", "r") as layout_file:
                        layer_dict = json.load(layout_file)
                        chunks = []
                        tileset = import_cut_graphics(f"./assets/sprite/tilesets/tileset.png", self.config)
                        layer = Layer(layer_dict["layer_index"], tileset, layer_dict["y-sorted"], layer_dict["collidable"], chunks)

                        for chunk, chunk_data in layer_dict["layer_chunks"].items():
                            chunk_x = chunk.split(";")[0]
                            chunk_y = chunk.split(";")[1]
                            chunks.append(self.generate_chunks(layer, [chunk_x, chunk_y], chunk_data))
                    self.camera.add_group(layer, self.player)


    def generate_chunks(self, layer, chunk_position, chunk_data) -> dict:
        tiles = []
        for tile_x_position in range(0, self.config.chunk_size):
            for tile_y_position in range(0, self.config.chunk_size):
                tile_position = f"{tile_x_position};{tile_y_position}"
                if tile_position in chunk_data:
                    tile_value = chunk_data[tile_position]
                    tiles.append({"position": [tile_x_position, tile_y_position], "value": tile_value})
        return Chunk(layer, chunk_position, tiles, self.display_surface, self.camera, self.config)

        
    def update(self, delta_time) -> None:
        self.camera.update(delta_time)
    

    def render(self) -> None:
        self.camera.render(self.player)