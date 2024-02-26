from arcade.func.read_json import read_json
from arcade.utils.imports import *


def write_json(file, key, data) -> dict:
    json_file = read_json(file)

    json_file[key] = data

    with open(file, "w") as outfile:
        json.dump(json_file, outfile)