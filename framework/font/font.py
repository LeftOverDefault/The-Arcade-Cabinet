from framework.utils.imports import *


class Font:
    def __init__(self, path, size, color) -> None:
        self.spacing = 1
        self.character_order = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "-", ",", ":", "+", "'", "!", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "/", "_", "=", "\\", "[", "]", "*", "\"", "<", ">", ";", "|", "~", "£", "ƒ", "{", "}", "@", "#", "$", "%", "&", "^", "`"],
        font_img = pygame.image.load(path).convert_alpha()
        current_char_width = 0
        self.characters = {}
        character_count = 0

        for x in range(font_img.get_width()):
            c = font_img.get_at((x, 0))
            if c[0] == 127:
                char_img = self.clip(surface=font_img, x=x - current_char_width, y=0, x_size=current_char_width, y_size=font_img.get_height())
                char_img.fill(color=(0, 0, 0, 255), rect=None, special_flags=pygame.BLEND_RGBA_MULT)
                char_img.fill(color=color[0:3] + (0,), rect=None, special_flags=pygame.BLEND_RGBA_ADD)
                char_img = pygame.transform.scale_by(surface=char_img, factor=size)
                self.characters[list(self.character_order[0])[character_count]] = char_img.copy()
                character_count += 1
                current_char_width = 0
            else:
                current_char_width += 1
        self.space_width = self.characters["A"].get_width()
        self.line_height = self.characters["A"].get_height()


    def clip(self, surface: pygame.Surface, x, y, x_size, y_size):
        handle_surface = surface.copy()
        clip_rect = pygame.Rect(x, y, x_size, y_size)
        handle_surface.set_clip(clip_rect)
        image = surface.subsurface(handle_surface.get_clip())
        return image.copy()


    def render(self, surface: pygame.Surface, text, location):
        x_offset = 0
        center = 0
        for char in text:
            if char != " ":
                center += self.characters[char].get_width() + self.spacing
            else:
                center += self.space_width + self.spacing
        for char in text:
            if char != " ":
                surface.blit(source=self.characters[char], dest=(location[0] + (x_offset) - (center // 2), location[1]))
                x_offset += self.characters[char].get_width() + self.spacing
            else:
                x_offset += self.space_width + self.spacing


    # def return_image(self, text):
    #     x_offset = 0
    #     text_images = []
    #     for char in text:
    #         if char != " ":
    #             text_images.append([self.characters[char], x_offset])
    #             x_offset += self.characters[char].get_width() + self.spacing
    #         else:
    #             x_offset += self.space_width + self.spacing
    #     return text_images, x_offset