from framework.interface.button import Button
from framework.utils.imports import *


class Menu:
    def __init__(self, screen: pygame.Surface, display_surface: pygame.Surface, clock: pygame.time.Clock, fps: int, state_handler: str) -> None:
        self.screen = screen
        self.display_surface = display_surface

        self.state_handler = state_handler

        self.buttons: list[Button] = []

    
    def render(self) -> None:
        ...

    
    def update(self, delta_time: float) -> None:
        ...
    

    def events(self, event: pygame.Event) -> None:
        ...