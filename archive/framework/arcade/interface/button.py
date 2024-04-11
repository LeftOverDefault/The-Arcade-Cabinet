from framework.arcade.font.font import Font
from framework.arcade.utils.imports import *


class Button:
    def __init__(self, image, position, text, font_path, base_color, hover_color, menu) -> None:
        self.image = image

        self.menu = menu

        self.position = position

        self.base_color = base_color
        self.hover_color = hover_color

        self.font_base = Font(font_path, 1, pygame.Color(self.base_color), menu.config)
        self.font_hover = Font(font_path, 1, pygame.Color(self.hover_color), menu.config)

        self.text_images_base = self.font_base.return_image(text)[0]
        self.text_images_hover = self.font_hover.return_image(text)[0]
        
        self.current_text = self.text_images_base

        self.text_images_offset = self.font_hover.return_image(text)[1]

        self.text_rect = pygame.Rect(position[0] - (self.text_images_offset // 2), position[1] - (self.font_base.line_height // 2), self.text_images_offset, self.font_base.line_height)

        if self.image != None:
            self.rect = self.image.get_rect(center=position)
            self.text_rect = pygame.Rect(self.rect.topleft[0] + ((self.image.get_width() - self.text_images_offset) // 2), self.rect.topleft[1] + ((self.image.get_height() - self.font_base.line_height) / 2), self.rect.bottomright[0], self.rect.bottomright[1])
        else:
            self.image = self.current_text
            self.rect = self.text_rect

        self.menu.buttons.append(self)


    def check_input(self, position) -> bool:
        if position[0] in range(int(self.rect.left * (pygame.display.get_surface().get_width() / (192 * self.menu.config.screen_multiplier))), int(self.rect.right * (pygame.display.get_surface().get_width() / (192 * self.menu.config.screen_multiplier)))) and position[1] in range(int(self.rect.top * (pygame.display.get_surface().get_height() / (108 * self.menu.config.screen_multiplier))), int(self.rect.bottom * (pygame.display.get_surface().get_height() / (108 * self.menu.config.screen_multiplier)))):
            if pygame.mouse.get_pressed()[0]:
                return True
        return False


    def change_color(self, position) -> None:
        if position[0] in range(int(self.rect.left * (pygame.display.get_surface().get_width() / (192 * self.menu.config.screen_multiplier))), int(self.rect.right * (pygame.display.get_surface().get_width() / (192 * self.menu.config.screen_multiplier)))) and position[1] in range(int(self.rect.top * (pygame.display.get_surface().get_height() / (108 * self.menu.config.screen_multiplier))), int(self.rect.bottom * (pygame.display.get_surface().get_height() / (108 * self.menu.config.screen_multiplier)))):
            if self.image != self.text_images_base and self.image != self.text_images_hover:
                self.current_text = self.text_images_hover
                # self.image.fill(self.base_color)
            else:
                self.image = self.text_images_hover
        else:
            if self.image != self.text_images_base and self.image != self.text_images_hover:
                self.current_text = self.text_images_base
                # self.image.fill(self.hover_color)
            else:
                self.image = self.text_images_base


    def event(self):
        ...


    def draw(self) -> None:
        if self.image == self.text_images_base or self.image == self.text_images_hover:
            for image in self.image:
                self.menu.display_surface.blit(image[0], [self.text_rect.x + image[1], self.text_rect.y])
        else:
            self.menu.display_surface.blit(self.image, self.rect)
            for image in self.current_text:
                self.menu.display_surface.blit(image[0], [self.text_rect.x + image[1], self.text_rect.y])