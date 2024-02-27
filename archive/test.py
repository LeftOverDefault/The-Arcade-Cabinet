# from arcade.classes.layer import Layer
# from arcade.classes.player import Player
# from arcade.classes.tiles.tile import Tile
# from arcade.classes.window import Window
# from arcade.func.read_json import read_json
# from arcade.utils.imports import *

import arcade.top_down as top_down
from arcade.top_down import config

class Main:
    def __init__(self) -> None:
        self.config = top_down.read_json("./config.json")
        self.window = top_down.Window(config=self.config)

        layer_1 = top_down.Layer(display_surface=self.window.display_surface)
        top_down.Tile((0, 0), layer_1)
        top_down.Tile((16 * config["scale_factor"], 0), layer_1)

        player_layer = top_down.Layer(display_surface=self.window.display_surface)
        self.window.player = top_down.Player(group=player_layer)

        self.window.camera.add_group(group=layer_1)
        self.window.camera.add_group(group=player_layer)


    def run(self):
        self.window.run()


if __name__ == "__main__":
    main = Main()
    main.run()