# from arcade.classes.layer import Layer
# from arcade.classes.player import Player
# from arcade.classes.tiles.tile import Tile
# from arcade.classes.window import Window
# from arcade.func.read_json import read_json
# from arcade.utils.imports import *

import arcade
from arcade import config

class Main:
    def __init__(self) -> None:
        self.config = arcade.read_json("./config.json")
        self.window = arcade.Window(config=self.config)

        layer_1 = arcade.Layer(display_surface=self.window.display_surface)
        arcade.Tile((0, 0), layer_1)
        arcade.Tile((16 * config["scale_factor"], 0), layer_1)

        player_layer = arcade.Layer(display_surface=self.window.display_surface)
        self.window.player = arcade.Player(group=player_layer)

        self.window.camera.add_group(group=layer_1)
        self.window.camera.add_group(group=player_layer)


    def run(self):
        self.window.run()


if __name__ == "__main__":
    main = Main()
    main.run()