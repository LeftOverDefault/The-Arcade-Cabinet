# from arcade.utils.imports import *


# def generate_chunk(config, world_data, x, y):
#     chunk_data = []
#     for x_position in range(0, 8):
#         for y_position in range(0, 8):
#             tile_value = world_data[f"{x};{y}"][f"{x_position};{y_position}"]
#             target_x = (x * config.chunk_size) + x_position
#             target_y = (y * config.chunk_size) + y_position
#             chunk_data.append(([target_x, target_y], tile_value))
#     return chunk_data