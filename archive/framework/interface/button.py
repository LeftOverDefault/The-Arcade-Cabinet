from framework.font.font import Font
from framework.utils.imports import *


class Button:
    def __init__(self, image, text, position, menu) -> None:
        self.image = image
        self.text = text
        self.menu = menu
        self.font = Font(self.menu.config.font_path, 1, (255, 255, 255), self.menu.config)

        self.text_render = self.font.return_image(self.text)[0]
        self.text_images_offset = self.font.return_image(text)[1]

        self.rect = self.image.get_rect(center=position)
        self.text_rect = pygame.Rect(position[0] - (self.text_images_offset // 2), position[1] - (self.font.line_height // 2), self.text_images_offset, self.font.line_height)

        self.menu.buttons.append(self)


    def check_input(self, event) -> None:
        if self.rect.colliderect(self.menu.mouse_rect):
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if self.rect.collidepoint(self.menu.mouse_rect.topleft):
                            return True
        return False


    def update(self) -> None:
        ...


    def event(self, event) -> None:
        ...


    def draw(self) -> None:
        self.menu.display_surface.blit(self.image, self.rect)
        for image in self.text_render:
            self.menu.display_surface.blit(image[0], [self.text_rect.x + image[1], self.text_rect.y])