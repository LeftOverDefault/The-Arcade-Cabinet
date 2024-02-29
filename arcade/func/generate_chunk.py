from arcade.utils.imports import *


def generate_chunk(config, x, y):
    chunk_data = []
    for x_position in range(0, 8):
        for y_position in range(0, 8):
            target_x = (x * config.chunk_size) + x_position
            target_y = (y * config.chunk_size) + y_position
            chunk_data.append([target_x,target_y])
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
    return chunk_data