from arcade.utils.imports import *


def read_json(file):
    with open(file=file, mode="r") as read_file:
        json_file = json.load(fp=read_file)
        return json_file