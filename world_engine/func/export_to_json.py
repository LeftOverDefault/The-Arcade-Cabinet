from world_engine.utils.imports import *


def export_to_json(layer_name, group: pygame.sprite.Group, config):
    layers = {}
    layers[layer_name] = []
    for sprite in group.sprites():
        if sprite.tile_layer == layer_name:
            layers[layer_name].append(sprite)

    for layer in layers:
        layer_dict = {}
        for sprite in layers[layer]:
            sprite_position = (sprite.rect.topleft[0] // config.tile_size, sprite.rect.topleft[1] // config.tile_size)
            sprite_index = sprite.tile_index
        
            sprite_chunk = f"{sprite_position[0] // config.chunk_size};{sprite_position[1] // config.chunk_size}"
            sprite_coordinate = f"{sprite.rect.topleft[0] // config.tile_size};{sprite.rect.topleft[1] // config.tile_size}"

            if sprite_chunk not in layer_dict.keys():
                layer_dict[sprite_chunk] = {}

                sprite_coordinate = f"{sprite_position[0] % 8};{sprite_position[1] % 8}"
                layer_dict[sprite_chunk][sprite_coordinate] = sprite_index

            else:
                sprite_coordinate = f"{sprite_position[0] % 8};{sprite_position[1] % 8}"
                layer_dict[sprite_chunk][sprite_coordinate] = sprite_index
        
        try:
            with open(f"./world_engine/build/{config.world_name.lower()}_{layer_name.lower()}.json", "x") as file:
                json.dump(layer_dict, file)
        except FileExistsError:
            with open(f"./world_engine/build/{config.world_name.lower()}_{layer_name.lower()}.json", "w") as file:
                json.dump(layer_dict, file)