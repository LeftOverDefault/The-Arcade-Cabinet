from framework.font.font import Font
from framework.utils.imports import *


class Button:
    def __init__(self, image: pygame.Surface, position: list, menu) -> None:
        self.image = image
        self.rect: pygame.Rect = self.image.get_rect(center=position)
        self.menu = menu

        self.menu.buttons.append(self)

        self.mouse_collide_point = pygame.mouse.get_pos()


    def check_input(self, event) -> bool:
        if event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(self.mouse_collide_point):
            if event.button == 1:
                return True
        return False
    

    def render(self) -> None:
        ...

    
    def update(self, delta_time: float) -> None:
        ...
