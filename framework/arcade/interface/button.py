from framework.arcade.font.font import Font
from framework.arcade.utils.imports import *


class Button:
    def __init__(self, image, position, text, font_path, base_color, hover_color, menu) -> None:
        self.image = image

        self.menu = menu

        self.position = position

        self.font_base = Font(font_path, 1, pygame.Color(base_color), menu.config)
        self.font_hover = Font(font_path, 1, pygame.Color(hover_color), menu.config)

        self.text_images_base = self.font_base.return_image(text)[0]
        self.text_images_hover = self.font_hover.return_image(text)[0]

        self.text_images_offset = self.font_hover.return_image(text)[1]

        self.text_rect = pygame.Rect(self.text_images_base[-1][1], position[1], self.text_images_offset, self.font_base.line_height)

        if self.image != None:
            self.rect = self.image.get_rect(center=position)
        else:
            self.image = self.text_images_base
            self.rect = self.text_rect

        self.menu.buttons.append(self)


    def check_input(self, position) -> bool:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False


    def change_color(self, position) -> None:
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.image = self.text_images_hover
        else:
            self.image = self.text_images_base
    

    def event(self, menu):
        ...


    def draw(self) -> None:
        if self.image != self.text_images_base and self.image != self.text_images_hover:
            self.menu.display_surface.blit(self.image, self.rect)
        
        for image in self.image:
            self.menu.display_surface.blit(image[0], [self.text_rect.x + image[1], self.text_rect.y])