from framework.arcade.utils.imports import *


class Button:
    def __init__(self, image, alt_image, position, surface) -> None:
        self.surface = surface
        self.original_image = image
        self.alt_image = alt_image

        self.image = self.original_image
        self.rect = self.image.get_rect(topleft=position)

        self.clicked = False
    

    def on_hover(self, mouse_rect) -> None:
        if self.rect.colliderect(mouse_rect):
            self.image = self.alt_image
        else:
            self.image = self.original_image
    

    def on_click(self, mouse_rect) -> None:
        if self.rect.colliderect(mouse_rect):
            if pygame.mouse.get_pressed()[0] == True:
                self.clicked = True
            else:
                self.clicked = False


    def draw(self) -> None:
        self.surface.blit(self.image, self.rect)