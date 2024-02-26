from arcade.classes.tiles.static_tile import StaticTile
from arcade.func.import_csv import import_csv
from arcade.func.import_cut_graphics import import_cut_graphics
from arcade.utils.imports import *


class Layer(pygame.sprite.Group):
    def __init__(self, display_surface) -> None:
        super().__init__()

        self.display_surface = display_surface

        self.sprite_array = []

        # self.grass = import_csv(path="./src/data/overworld/overworld_grass.csv")
        # self.path = import_csv(path="./src/data/overworld/overworld_path.csv")
        # self.hill = import_csv(path="./src/data/overworld/overworld_hill.csv")
        # self.fence = import_csv(path="./src/data/overworld/overworld_fence.csv")
        # self.house = import_csv(path="./src/data/overworld/overworld_house.csv")
        # self.water = import_csv(path="./src/data/overworld/overworld_water.csv")

        self.collidable = False
        self.y_sorted = False
    

    def create_tiles(self, layout, tile_type) -> None:
        for row_index, row in enumerate(iterable=layout):
            for column_index, value in enumerate(iterable=row):
                if value != "-1":
                    x = column_index * config["tile_size"] * config["scale_factor"]
                    y = row_index * config["tile_size"] * config["scale_factor"]

                    # if tile_type == "grass":
                    #     terrain_graphics = import_cut_graphics(path="./assets/sprites/environment/grass.png")
                    #     tile_surface = terrain_graphics[int(value)]
                    #     StaticTile(position=(x, y), image=tile_surface, group=self)
                    # elif tile_type == "path":
                    #     terrain_graphics = import_cut_graphics(path="./assets/sprites/environment/path.png")
                    #     tile_surface = terrain_graphics[int(value)]
                    #     StaticTile(position=(x, y), image=tile_surface, group=self)
                    # elif tile_type == "hills":
                    #     terrain_graphics = import_cut_graphics(path="./assets/sprites/environment/hills.png")
                    #     tile_surface = terrain_graphics[int(value)]
                    #     StaticTile(position=(x, y), image=tile_surface, group=self)
                    # elif tile_type == "fence":
                    #     terrain_graphics = import_cut_graphics(path="./assets/sprites/environment/fence.png")
                    #     tile_surface = terrain_graphics[int(value)]
                    #     StaticTile(position=(x, y), image=tile_surface, group=self)
                    # elif tile_type == "house":
                    #     terrain_graphics = import_cut_graphics(path="./assets/sprites/environment/house.png")
                    #     tile_surface = terrain_graphics[int(value)]
                    #     StaticTile(position=(x, y), image=tile_surface, group=self)
                    # elif tile_type == "water":
                    #     terrain_graphics = import_cut_graphics(path="./assets/sprites/environment/water.png")
                    #     tile_surface = terrain_graphics[int(value)]
                    #     StaticTile(position=(x, y), image=tile_surface, group=self)

    # def add_tile_sheet(self, type, path) -> None:
