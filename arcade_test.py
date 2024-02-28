import arcade
from arcade.classes.camera import Camera
from arcade.classes.configure import Configure
from arcade.classes.layer import Layer
from arcade.classes.player import Player
from arcade.debug.debugger import Debugger


# world = {
#     "0;0": {
#         "0;0": -1, "1;0": -1, "2;0": -1, "3;0": -1, "4;0": -1, "5;0": -1, "6;0": -1, "7;0": -1,
#         # "0;1": -1, "1;1": -1, "2;1": -1, "3;1": -1, "4;1": -1, "5;1": -1, "6;1": -1, "7;1": -1,
#         # "0;2": -1, "1;2": -1, "2;2": -1, "3;2": -1, "4;2": -1, "5;2": -1, "6;2": -1, "7;2": -1,
#         # "0;3": -1, "1;3": -1, "2;3": -1, "3;3": -1, "4;3": -1, "5;3": -1, "6;3": -1, "7;3": -1,
#         # "0;4": -1, "1;4": -1, "2;4": -1, "3;4": -1, "4;4": -1, "5;4": -1, "6;4": -1, "7;4": -1,
#         # "0;5": -1, "1;5": -1, "2;5": -1, "3;5": -1, "4;5": -1, "5;5": -1, "6;5": -1, "7;5": -1,
#         # "0;6": -1, "1;6": -1, "2;6": -1, "3;6": -1, "4;6": -1, "5;6": -1, "6;6": -1, "7;6": -1,
#         # "0;7": 0, "1;7": 0, "2;7": 0, "3;7": 0, "4;7": 0, "5;7": 0, "6;7": 0, "7;7": 0,
#     }
# }

# config = {
#     "name": "Arcade Test",
#     "version": "0.1.0",
#     "resolution": [int(192 * 1.25), int(108 * 1.25)],
#     "scale_factor": 5,
#     "tile_size": 16,
#     "chunk_size": 8,
#     "camera_delay": 25,
#     "fps": 60,
#     "fullscreen": False,
#     "worlds": [
#         world
#     ]
# }

config = {
    "name": "Arcade Test",
    "version": "0.1.0",
    "scale_factor": 2,
    "debug": True
}


class Main:
    def __init__(self) -> None:
        self.window = arcade.Window(config)
        self.camera = Camera(self.window.display_surface)
        self.player = Player((0, 0), self.camera)

        self.window.render = self.render
        self.window.update = self.update

        self.debugger = Debugger(self.window.config)



        self.layer_1 = Layer(False, True)

        self.camera.add_group(self.layer_1, self.player)


    def render(self):
        self.camera.draw(self.player)
        self.window.screen.blit(arcade.pygame.transform.scale(self.window.display_surface, self.window.screen.get_size()), (0, 0))
        self.debugger.draw(self.window.clock, self.window.delta_time, self.player)


    def update(self):
        self.camera.update(self.window.delta_time)


    def run(self):
        self.window.run()


if __name__ == "__main__":
    main = Main()
    main.run()