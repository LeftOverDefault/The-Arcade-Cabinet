from framework.arcade.utils.imports import *


def import_folder(path) -> list:
    surface_array = []

    for _, __, image_array in list(os.walk(path)):
        for image in image_array:
            full_path = path + image
            surface = pygame.image.load(full_path).convert_alpha()
            surface_array.append(surface)
    
    return surface_array