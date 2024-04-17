from framework.func.json_read import json_read
from framework.utils.imports import *


def json_write(file_path: str, key, value) -> dict:
    json_file = json_read(file_path)

    json_file[key] = value

    with open(file_path, "w") as outfile:
        json.dump(json_file, outfile)