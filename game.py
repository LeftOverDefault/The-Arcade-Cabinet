#! /usr/bin/python
import framework
from framework.func.fade_in import fade_in
from framework.interface.menu import Menu

from src.menus.video_options_menu import video_options_menu
from src.menus.audio_options_menu import audio_options_menu
from src.menus.options_menu import options_menu
from src.menus.pause_menu import pause_menu
from src.menus.main_menu import main_menu
from src.utils import config
from src.screens.banner import Banner

configuration = {}

for variable in dict(vars(config)):
    if not variable.startswith("_"):
        configuration[variable.lower()] = dict(vars(config))[variable]


class Game:
    def __init__(self, config) -> None:
        self.config = framework.Configure(config)
        self.arcade = framework.Arcade(self.config)

        self.banner = Banner(self.arcade.screen)

        self.main_menu = Menu(self.arcade.screen, self.arcade.display_surface, self.config)
        self.options_menu = Menu(self.arcade.screen, self.arcade.display_surface, self.config)
        self.audio_options_menu = Menu(self.arcade.screen, self.arcade.display_surface, self.config)
        self.video_options_menu = Menu(self.arcade.screen, self.arcade.display_surface, self.config)
        self.pause_menu = Menu(self.arcade.screen, self.arcade.display_surface, self.config)

        self.on_init()


    def on_init(self) -> None:
        self.arcade.render = self.render
        self.arcade.update = self.update
        self.arcade.events = self.events


    def render(self) -> None:
        ...


    def update(self, delta_time) -> None:
        ...


    def events(self, event) -> None:
        if event.type == framework.imports.pygame.KEYDOWN:
            if event.key == framework.imports.pygame.K_ESCAPE:
                self.pause_menu.run()


    def run(self) -> None:
        self.banner.run()
        fade_in(int(2.5), self.main_menu.fade_surf, self.arcade.display_surface, self.arcade.screen, self.main_menu.render)
        self.main_menu.run()


if __name__ == "__main__":
    game = Game(configuration)

    game.main_menu.background_color = (255, 0, 0)
    game.options_menu.background_color = (0, 255, 0)
    game.audio_options_menu.background_color = (255, 255, 0)
    game.video_options_menu.background_color = (255, 0, 255)
    game.pause_menu.background_color = (0, 0, 255)

    main_menu(game)
    options_menu(game)
    audio_options_menu(game)
    video_options_menu(game)
    pause_menu(game)

    game.run()

























# from framework_old.arcade import arcade
# from framework_old.arcade.classes import World
# from framework_old.arcade.func.fade_in import fade_in
# from framework_old.arcade.func.fade_out import fade_out
# from framework_old.arcade.interface import Button, Menu
# from framework_old.arcade.utils.imports import *

# from tests.menu.main import MainMenu
# from tests.menu.options import Options
# from tests.menu.pause import Pause

# from tests.screen.banner import Banner


# config = {
#     "name": "Arcade Test",
#     "screen_multiplier": 6,
#     "display_surface_multiplier": 1.5,
#     "tile_size": 16,
#     "chunk_size": 8,
#     "debug": False,
#     "tilesets": {
#         "tilesheet": "./assets/sprite/tilesets/tileset.png",
#         # "plains": "./assets/sprite/tilesets/plains.png"
#     },
#     "font": "./assets/font/font.png",
#     "font_colour": (255, 236, 250),
#     "font_order": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "-", ",", ":", "+", "'", "!", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "/", "_", "=", "\\", "[", "]", "*", "\"", "<", ">", ";", "|", "~", "£", "ƒ", "{", "}", "@", "#", "$", "%", "&", "^", "`"],
#     "font_size": 2,
#     "world_name": "overworld",
#     "world_directory": "./build/",
#     "player_path": "./assets/sprite/entity/player/"
# }


# class Game:
#     def __init__(self, config) -> None:
#         self.arcade = arcade.Arcade(config)

#         self.world = World(self.arcade.display_surface, self.arcade.config)

#         self.banner = Banner(self.arcade.screen)
#         self.main_menu = MainMenu(self.arcade.screen, self.arcade.display_surface, self.arcade.debugger, self.arcade.config)
#         self.pause = Pause(self.arcade.screen, self.arcade.display_surface, self.arcade.debugger, self.arcade.config)
#         self.options = Options(self.arcade.display_surface, self.arcade.debugger, self.arcade.config)

#         self.arcade.render = self.render
#         self.arcade.update = self.update
#         self.arcade.events = self.events

#         self.arcade.particle_system.max_particles = 50


#     def render_debugger(self):
#         self.arcade.debugger.debug_info.clear()

#         self.arcade.debugger.debug_info.append(f"Debug Menu:")
#         self.arcade.debugger.debug_info.append(f"FPS: {round(number=self.arcade.clock.get_fps())}")
#         self.arcade.debugger.debug_info.append(f"Delta Time: {round(self.arcade.delta_time, 4)}")
#         self.arcade.debugger.debug_info.append(f"Player Pos: x = {int(self.world.player.position.x)}, y = {int(self.world.player.position.y)}")
#         self.arcade.debugger.debug_info.append(f"Player Status: {self.world.player.status}")
#         self.arcade.debugger.debug_info.append(f"Particle Count: {len(self.arcade.particle_system.sprites())}")


#     def render(self) -> None:
#         if self.arcade.config.debug == True:
#             self.render_debugger()

#         self.world.render()

#         # mx = pygame.mouse.get_pos()[0] // (self.arcade.config.screen_multiplier // self.arcade.config.display_surface_multiplier)
#         # my = pygame.mouse.get_pos()[1] // (self.arcade.config.screen_multiplier // self.arcade.config.display_surface_multiplier)

#         # Particle("./assets/sprite/environment/particle", [mx, my], [random.randint(0, 20) / 10 - 1, -2], 9.80665, random.randint(4, 6), self.arcade.particle_system)

#         # x = 0 - self.world.camera.offset[0]
#         # y = 0 - self.world.camera.offset[1]

#         # x_vel = 0
#         # y_vel = 0
#         # acceleration = 0
#         # Particle("./assets/sprite/environment/particle", [x, y], self.arcade.particle_system)

#         # Particle("./assets/sprite/environment/particle", [x, y], [x_vel, y_vel], acceleration, 100000, self.arcade.particle_system)
#         self.arcade.particle_system.draw()


#     def update(self, delta_time) -> None:
#         self.world.update(delta_time)
#         self.arcade.particle_system.update(self.arcade.delta_time)


#     def events(self, event) -> None:
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 fade_out(int(time_converter(0.0025, "milliseconds")), self.arcade.fade_surf, self.arcade.display_surface, self.arcade.screen, self.arcade.render)
#                 fade_in(int(time_converter(0.0025, "milliseconds")), self.pause.fade_surf, self.pause.display_surface, self.pause.screen, self.pause.render)
#                 self.pause.run()


#     def run(self) -> None:
#         # self.banner.run()
#         # self.main_menu.run()
#         self.arcade.run()


# if __name__ == "__main__":
#     main = Game(config)

#     img = pygame.Surface([96, 16])
#     img.fill((0, 0, 0))
        
#     play_button = Button(img, [main.arcade.display_surface.get_width() // 2, main.arcade.display_surface.get_height() // 3], "Play", "./assets/font/font.png", "#fefefe", "#8f8f8f", main.main_menu)
#     resume_button = Button(img, [main.arcade.display_surface.get_width() // 2, main.arcade.display_surface.get_height() // 3], "Resume", "./assets/font/font.png", "#fefefe", "#8f8f8f", main.pause)
#     options_button = Button(img, [main.arcade.display_surface.get_width() // 2, main.arcade.display_surface.get_height() // 2], "Options", "./assets/font/font.png", "#fefefe", "#8f8f8f", main.pause)
#     quit_button = Button(img, [main.arcade.display_surface.get_width() // 2, main.arcade.display_surface.get_height() // (3 / 2)], "Quit", "./assets/font/font.png", "#fefefe", "#8f8f8f", main.pause)

#     def play_event():
#         play_button.menu.running = False
#         fade_out(int(time_converter(0.0025, "milliseconds")), main.main_menu.fade_surf, main.main_menu.display_surface, main.main_menu.screen, main.main_menu.render)
#         pygame.time.delay(int(time_converter(0.5, "milliseconds")))
#         main.arcade.run()
#     def resume_event():
#         resume_button.menu.running = False
#         fade_out(int(time_converter(0.0025, "milliseconds")), resume_button.menu.fade_surf, resume_button.menu.display_surface, resume_button.menu.screen, resume_button.menu.render)
#         fade_in(int(time_converter(0.0025, "milliseconds")), main.arcade.fade_surf, main.arcade.display_surface, main.arcade.screen, main.arcade.render)
#     def options_event():
#         main.options.run()
#     def quit_event():
#         main.arcade.running = False
#         fade_out(int(time_converter(0.0025, "milliseconds")), main.pause.fade_surf, main.pause.display_surface, main.pause.screen, main.pause.render)
#         resume_button.menu.running = False
#         main.main_menu.run()

#     play_button.event = play_event
#     resume_button.event = resume_event
#     options_button.event = options_event
#     quit_button.event = quit_event

#     main.run()