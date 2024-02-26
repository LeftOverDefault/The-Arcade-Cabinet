from arcade.utils.imports import *

def import_csv(path) -> list:
    map = []

    with open(file=path, mode="r") as world_map:
        layout = reader(world_map, delimiter=",")
        for row in layout:
            map.append(list(row))
    
    return map