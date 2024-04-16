from framework.utils.imports import *
from framework.font.font import Font

class Debugger:
    def __init__(self, font_path, config) -> None:
        self.config = config

        self.screen = pygame.display.get_surface()
        self.surface = pygame.Surface(size=(pygame.display.get_surface().get_width() / 2, pygame.display.get_surface().get_height() / 2)).convert_alpha()
        self.rect = self.surface.get_rect(bottomright=self.screen.get_size())
        self.font = Font(path=font_path, size=2, color=(255, 255, 255), config=self.config)

        self.debug_info = ["Debug Menu:"]
    

    def render(self) -> None:
        for info_index, info in enumerate(self.debug_info):
            self.font.render(surface=self.surface, text=info, location=(10, 10 + (info_index * (self.font.line_height + 4))))


    def draw(self) -> None:
        self.surface.fill(color="#64646490")

        self.render()

        self.screen.blit(source=self.surface, dest=self.rect)