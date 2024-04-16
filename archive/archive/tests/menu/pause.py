from framework_old.arcade import interface

from framework_old.arcade.func.fade_in import fade_in
from framework_old.arcade.func.fade_out import fade_out
from framework_old.arcade.utils.imports import *


class Pause(interface.Menu):
    def __init__(self, screen, display_surface, debugger, config) -> None:
        super().__init__(display_surface, debugger, config)
        self.background_color = "#2e2e2e"

        self.screen = screen

        self.fade_surf = pygame.Surface(pygame.display.get_surface().get_size())
        self.fade_surf.fill((0, 0, 0))


    def events(self, event) -> None:
        ...