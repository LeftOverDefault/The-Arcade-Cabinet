from world_engine.classes.tile.static_tile import StaticTile
from world_engine.utils.imports import *


def import_from_json(world, camera, tileset, config):
    with open(world, "r") as world_file:
        world = json.load(world_file)
    for chunk in world.keys():
        chunk_x = chunk.split(";")[0]
        chunk_y = chunk.split(";")[1]

        for tile in world[chunk].keys():
            tile_x = int(tile.split(";")[0]) + (int(chunk_x) * config.chunk_size)
            tile_y = int(tile.split(";")[1]) + (int(chunk_y) * config.chunk_size)

            tile_index = world[chunk][tile]

            StaticTile(list(tileset.keys())[int(tile_index)], tile_index, (tile_x * config.tile_size, tile_y * config.tile_size), camera, config)