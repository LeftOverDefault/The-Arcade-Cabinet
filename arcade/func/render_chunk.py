def render_chunk(config, chunk_coordinates, chunk_x_offset, chunk_y_offset):
    tiles = []
    for coordinate in chunk_coordinates:
        tile_x = (coordinate[0] * config.tile_size) + chunk_x_offset
        tile_y = (coordinate[1] * config.tile_size) + chunk_y_offset
        tiles.append([tile_x, tile_y])
    return tiles