from framework.arcade import interface

from framework.arcade.utils.imports import *


class Options(interface.Menu):
    def __init__(self, display_surface, debugger, config) -> None:
        super().__init__(display_surface, debugger, config)
        self.background_color = "#2e2e2e"


    def events(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.running = False