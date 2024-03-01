# def render_chunk(config, chunk_coordinates, chunk_x_offset, chunk_y_offset):
#     tiles = []
#     for offset_coordinate, value in chunk_coordinates:
#         tile_x = round(offset_coordinate[0] * config.tile_size) + int(chunk_x_offset)
#         tile_y = round(offset_coordinate[1] * config.tile_size) + int(chunk_y_offset)
#         tiles.append(([tile_x, tile_y], value))
#     return tiles