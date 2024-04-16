from src.utils.imports import *


class Banner:
    def __init__(self, screen, display_surface, state_handler) -> None:
        self.screen = screen
        self.display_surface = display_surface
        self.time_active = 0

    
    def update(self, delta_time):
        self.time_active += delta_time
        if int(self.time_active) >= 5000:
            self.done = True


    # def run(self) -> None:
    #     self.