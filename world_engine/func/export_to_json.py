from world_engine.utils.imports import *


def export_to_json(group: pygame.sprite.Group, config):
    world = {}
    for sprite in group.sprites():
        sprite_position = (sprite.rect.topleft[0] // config.tile_size, sprite.rect.topleft[1] // config.tile_size)
        sprite_index = sprite.tile_index
    
        sprite_chunk = f"{sprite_position[0] // config.chunk_size};{sprite_position[1] // config.chunk_size}"
        sprite_coordinate = f"{sprite.rect.topleft[0] // config.tile_size};{sprite.rect.topleft[1] // config.tile_size}"

        if sprite_chunk not in world.keys():
            world[sprite_chunk] = {}

            sprite_coordinate = f"{sprite_position[0] % 8};{sprite_position[1] % 8}"
            world[sprite_chunk][sprite_coordinate] = sprite_index

            # for x in range(config.chunk_size):
            #     for y in range(config.chunk_size):
            #         pass
            #         print(x, y)
            # world[sprite_chunk][f"{x};{y}"] = sprite_index
        else:
            sprite_coordinate = f"{sprite_position[0] % 8};{sprite_position[1] % 8}"
            world[sprite_chunk][sprite_coordinate] = sprite_index
        # for x in range(0, config.chunk_size):

    # for chunk_x_offset in range(0, config.chunk_size):
        # for chunk_y_offset in range(0, config.chunk_size):
            # tile_value = self.world_data[f"{x};{y}"][f"{chunk_x_offset};{chunk_y_offset}"]
            # chunk_x_target = chunk_x_offset
            # chunk_y_target = chunk_y_offset
            # chunk_data.append(([chunk_x_target, chunk_y_target], tile_value))
        # return chunk_data
    # for chunk_x in range(8):
    #     for chunk_y in range(8):
    #         world[f"{chunk_x};{chunk_y}"] = {}
    #         for sprite in group.sprites():
    #             tile_position = f"{sprite.rect.topleft[0] // config.tile_size};{sprite.rect.topleft[1] // config.tile_size}"
    #             world[f"{chunk_x};{chunk_y}"][tile_position] = sprite.tile_index

    
    with open("./world_engine/build.json", "w") as file:
        json.dump(world, file)