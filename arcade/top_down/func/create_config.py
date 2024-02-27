from arcade.utils.imports import *


def create_config(configuration: dict):
    with open("./arcade/data/config.json", "w") as outfile:
        json.dump(configuration, outfile)