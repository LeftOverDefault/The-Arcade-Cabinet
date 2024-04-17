import pygame
import framework

from framework.func.json_read import json_read
from framework.func.json_write import json_write
from framework.func.tween import Easing
from src.menus.pre_menu import PreMenu
from src.menus.audio_options_menu import AudioOptionsMenu
from src.menus.video_options_menu import VideoOptionsMenu
from src.menus.main_menu import MainMenu
from src.menus.options_menu import OptionsMenu

class Main:
    def __init__(self) -> None:
        framework.imports.pygame.init()
        framework.imports.pygame.display.set_caption("Game")
        
        self.settings = framework.imports.os.path.join(".", "src", "config", "settings.json")

        self.on_init()

        self.create_menus()


    def on_init(self) -> None:
        if json_read(self.settings)["fullscreen"] == True:
            self.screen = framework.imports.pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        else:
            self.screen = framework.imports.pygame.display.set_mode((192 * json_read(self.settings)["current_screen_multiplier"], 108 * json_read(self.settings)["current_screen_multiplier"]))
        self.display_surface = framework.imports.pygame.Surface((192 * json_read(self.settings)["display_surface_multiplier"], 108 * json_read(self.settings)["display_surface_multiplier"]))

        self.clock = framework.imports.pygame.time.Clock()
        self.fps = 60

        self.running = True

        self.state_handler = framework.StateHandler()
    

    def create_menus(self) -> None:
        self.pre_menu = PreMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler, self.settings)
        self.main_menu = MainMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler, self.settings)
        self.options_menu = OptionsMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler, self.settings)
        self.audio_options_menu = AudioOptionsMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler, self.settings)
        self.video_options_menu = VideoOptionsMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler, self.settings)


    def run(self) -> None:
        self.state_handler.update_state("pre_menu")
        while self.running == True:
            for event in framework.imports.pygame.event.get():
                if event.type == framework.imports.pygame.QUIT:
                    framework.imports.pygame.quit()
                    exit()
                elif event.type == framework.imports.pygame.KEYDOWN:
                    if event.key == framework.imports.pygame.K_F11:
                        json_write(self.settings, "fullscreen", not json_read(self.settings)["fullscreen"])

                        if json_read(self.settings)["fullscreen"] == True:
                            self.screen = framework.imports.pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            json_write(self.settings, "current_screen_multiplier", self.screen.get_width() / 192)
                        else:
                            json_write(self.settings, "current_screen_multiplier", json_read(self.settings)["screen_multiplier"])
                            self.screen = framework.imports.pygame.display.set_mode((192 * json_read(self.settings)["current_screen_multiplier"], 108 * json_read(self.settings)["current_screen_multiplier"]))

                if self.state_handler.current_state == "pre_menu":
                    self.pre_menu.events(event)
                elif self.state_handler.current_state == "main_menu":
                    self.main_menu.events(event)
                elif self.state_handler.current_state == "options_menu":
                    self.options_menu.events(event)
                elif self.state_handler.current_state == "audio_options_menu":
                    self.audio_options_menu.events(event)
                elif self.state_handler.current_state == "video_options_menu":
                    self.video_options_menu.events(event)

            self.display_surface.fill((0, 0, 0))
            self.delta_time = self.clock.tick(self.fps) / 1000

            if self.state_handler.current_state == "pre_menu":
                self.pre_menu.run(self.delta_time)
            elif self.state_handler.current_state == "main_menu":
                self.main_menu.run(self.delta_time)
            elif self.state_handler.current_state == "options_menu":
                self.options_menu.run(self.delta_time)
            elif self.state_handler.current_state == "video_options_menu":
                self.video_options_menu.run(self.delta_time)
            elif self.state_handler.current_state == "audio_options_menu":
                self.audio_options_menu.run(self.delta_time)
            # elif self.state_handler.current_state == "main_game":
                # self.options_menu.render()
                # self.options_menu.update(self.delta_time)

            self.screen.blit(framework.imports.pygame.transform.scale(self.display_surface, self.screen.get_size()), [0, 0])

            framework.imports.pygame.display.update()