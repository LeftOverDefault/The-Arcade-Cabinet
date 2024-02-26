from arcade.utils.imports import *


def read_json(file) -> dict:
    with open(file, "r") as json_file:
        file = json.load(json_file)
    
    return file