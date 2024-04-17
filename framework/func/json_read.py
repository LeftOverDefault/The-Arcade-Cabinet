from framework.utils.imports import *


def json_read(file_path: str) -> dict:
    with open(file_path, "r") as json_file:
        return json.load(json_file)