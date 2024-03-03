from world_engine.utils.imports import *


def export_to_json(group: pygame.sprite.Group, config):
    world = {}
    for chunk_x in range(8):
        for chunk_y in range(8):
            world[f"{chunk_x};{chunk_y}"] = {}
            for sprite in group.sprites():
                tile_position = f"{sprite.rect.topleft[0] // config.tile_size};{sprite.rect.topleft[1] // config.tile_size}"
                world[f"{chunk_x};{chunk_y}"][tile_position] = sprite.tile_index

    
    with open("./world_engine/build.json", "w") as file:
        json.dump(world, file)