from arcade_cabinet_LeftOverDefault import arcade
from arcade_cabinet_LeftOverDefault.arcade.classes.world import World
from arcade_cabinet_LeftOverDefault.arcade.interface.menu import Menu
from arcade_cabinet_LeftOverDefault.arcade.utils.imports import *


config = {
    "name": "Arcade Test",
    "screen_multiplier": 6,
    "display_surface_multiplier": 1.5,
    "tile_size": 16,
    "chunk_size": 8,
    "debug": False,
    "tilesets": {
        "tilesheet": "./assets/sprite/tilesets/tileset.png",
        # "plains": "./assets/sprite/tilesets/plains.png"
    },
    "font": "./assets/font/font.png",
    "font_colour": (255, 236, 250),
    "font_order": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "-", ",", ":", "+", "'", "!", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "/", "_", "=", "\\", "[", "]", "*", "\"", "<", ">", ";", "|", "~", "£", "ƒ", "{", "}", "@", "#", "$", "%", "&", "^", "`"],
    "font_size": 2,
    "world_name": "overworld",
    "world_directory": "./build/",
    "player_path": "./assets/sprite/entity/player/"
}


class Main:
    def __init__(self, config) -> None:
        self.arcade = arcade.Arcade(config)

        self.world = World(self.arcade.display_surface, self.arcade.config)
        self.pause = Pause(self.arcade.display_surface, self.arcade.debugger, self.arcade.config)
        self.pause.bg_color = (255, 255, 255, 0)

        self.arcade.render = self.render
        self.arcade.update = self.update
        self.arcade.events = self.events


    def render_debugger(self):
        self.arcade.debugger.debug_info.clear()

        self.arcade.debugger.debug_info.append(f"Debug Menu:")
        self.arcade.debugger.debug_info.append(f"FPS: {round(number=self.arcade.clock.get_fps())}")
        self.arcade.debugger.debug_info.append(f"Delta Time: {round(self.arcade.delta_time, 4)}")
        self.arcade.debugger.debug_info.append(f"Player Pos: x = {int(self.world.player.position.x)}, y = {int(self.world.player.position.y)}")
        self.arcade.debugger.debug_info.append(f"Player Status: {self.world.player.status}")


    def render(self) -> None:
        self.render_debugger()

        self.world.render()


    def update(self, delta_time) -> None:
        self.world.update(delta_time)


    def events(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.world.render()
                self.pause.run()


    def run(self) -> None:
        self.arcade.run()


class Pause(Menu):
    def __init__(self, display_surface, debugger, config) -> None:
        super().__init__(display_surface, debugger, config)


    def events(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False


if __name__ == "__main__":
    main = Main(config)
    main.run()



# py -m build
# py -m twine upload --repository testpypi dist/*
# pip uninstall arcade-cabinet-LeftOverDefault
# pip install -i https://test.pypi.org/simple/ arcade-cabinet-LeftOverDefault==0.0.0.8