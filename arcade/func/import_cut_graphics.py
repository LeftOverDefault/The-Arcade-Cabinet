from arcade.utils.imports import *


def import_cut_graphics(path) -> list:
    cut_tiles = []

    surface = pygame.image.load(file=path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / TILE_SIZE)
    tile_num_y = int(surface.get_size()[1] / TILE_SIZE)

    for row in range(tile_num_y):
        for column in range(tile_num_x):
            x = column * TILE_SIZE
            y = row * TILE_SIZE
            new_surface = pygame.Surface(size=(TILE_SIZE, TILE_SIZE), flags=pygame.SRCALPHA)
            new_surface.blit(source=surface, dest=(0, 0), area=pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))
            cut_tiles.append(new_surface)
    
    return cut_tiles