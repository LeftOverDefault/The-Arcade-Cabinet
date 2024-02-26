from arcade.classes.window import Window
from arcade.func.read_json import read_json
from arcade.utils.imports import *


class Main:
    def __init__(self) -> None:
        self.config = read_json("./config.json")
        self.window = Window(config=self.config)
    
    def run(self):
        self.window.run()
