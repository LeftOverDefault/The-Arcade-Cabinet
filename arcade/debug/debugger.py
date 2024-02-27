from arcade.utils.imports import *
from arcade.font.font import Font

class Debugger:
    def __init__(self, config) -> None:
        self.config = config

        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface(size=(pygame.display.get_surface().get_width() / 2, pygame.display.get_surface().get_height() / 2))
        self.rect = self.surface.get_rect(bottomright=self.screen.get_size())
        self.font = Font(path="./font.png", size=self.config.scale_factor, color=(255, 255, 255))


    def draw(self, clock) -> None:
        self.surface.fill(color=(100, 100, 100))
        self.font.render(surface=self.surface, text=f"FPS: {round(number=clock.get_fps())}", location=(10, 10))

        self.screen.blit(source=self.surface, dest=(0, 0))