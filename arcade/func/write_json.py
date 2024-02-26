from arcade.func.read_json import read_json
from arcade.utils.imports import *


def write_json(file, key, value) -> None:
    json_file = read_json(file=file)

    json_file[key] = value
    
    with open(file=file, mode="w") as out_file:
        json.dump(obj=json_file, fp=out_file)