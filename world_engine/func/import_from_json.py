from world_engine.classes.tile.static_tile import StaticTile
from world_engine.utils.imports import *


def import_from_json(world, camera: pygame.sprite.Group, canvas, tileset, config):
    with open(world, "r") as world_file:
        world = json.load(world_file)
    for chunk in world.keys():
        chunk_x = chunk.split(";")[0]
        chunk_y = chunk.split(";")[1]

        for tile in world[chunk].keys():
            tile_x = int(tile.split(";")[0]) + (int(chunk_x) * config.chunk_size)
            tile_y = int(tile.split(";")[1]) + (int(chunk_y) * config.chunk_size)

            tile_index = world[chunk][tile]

            if [tile_x, tile_y] in canvas.tile_positions:
                for sprite in camera.sprites():
                    if sprite.rect.x // config.tile_size == tile_x:
                        if sprite.rect.y // config.tile_size == tile_y:
                            camera.remove(sprite)
                canvas.tile_positions.remove([tile_x, tile_y])
            

            StaticTile(list(tileset.keys())[int(tile_index)], tile_index, (tile_x * config.tile_size, tile_y * config.tile_size), current_layer, camera, config)
            canvas.tile_positions.append([tile_x, tile_y])