from arcade.utils.imports import *
from arcade.font.font import Font

class Debugger:
    def __init__(self, font_path, config) -> None:
        self.config = config

        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface(size=(pygame.display.get_surface().get_width() / 2, pygame.display.get_surface().get_height() / 2)).convert_alpha()
        self.rect = self.surface.get_rect(bottomright=self.screen.get_size())
        self.font = Font(path=font_path, size=self.config.scale_factor, color=(255, 255, 255))
    

    def render(self) -> None:
        ...


    def draw(self) -> None:
        self.surface.fill(color=(100, 100, 100, 100))

        self.render()

        self.screen.blit(source=self.surface, dest=[self.screen.get_rect().bottomright[0] - self.surface.get_width(), self.screen.get_rect().bottomright[1] - self.surface.get_height()])