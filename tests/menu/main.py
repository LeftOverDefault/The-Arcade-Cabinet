from framework.arcade import interface

from framework.arcade.func.fade_in import fade_in
from framework.arcade.func.fade_out import fade_out
from framework.arcade.utils.imports import *


class MainMenu(interface.Menu):
    def __init__(self, screen, display_surface, debugger, config):
        super().__init__(display_surface, debugger, config)
        self.background_color = "#2e2e2e"

        self.screen = screen

        self.fade_surf = pygame.Surface(pygame.display.get_surface().get_size())
        self.fade_surf.fill((0, 0, 0))


    def events(self, event) -> None:
        ...
    

    def run(self) -> None:
        fade_in(int(time_converter(0.0025, "milliseconds")), self.fade_surf, self.display_surface, self.screen, self.render)
        super().run()