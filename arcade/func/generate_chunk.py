from arcade.utils.imports import *


def generate_chunk(config, x, y):
    chunk_data = []
    for y_position in range(config.chunk_size):
        for x_position in range(config.chunk_size):
            target_x = x * config.chunk_size + x_position
            target_y = y * config.chunk_size + y_position
            # tile_type = 0 # nothing
            # if target_y > 10:
            #     tile_type = 2 # dirt
            # elif target_y == 10:
            #     tile_type = 1 # grass
            # elif target_y == 9:
            #     if random.randint(1,5) == 1:
            #         tile_type = 3 # plant
            # if tile_type != 0:
            #     chunk_data.append([[target_x,target_y],tile_type])
            chunk_data.append([target_x,target_y])
    return chunk_data