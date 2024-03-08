from world_engine.utils.imports import *


class HorizontalLineSprite(pygame.sprite.Sprite):
    def __init__(self, start_pos, end_pos, color):
        super().__init__()
        self.image = pygame.Surface((abs(end_pos - start_pos[0]), 1))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=start_pos)


class VerticalLineSprite(pygame.sprite.Sprite):
    def __init__(self, start_pos, end_pos, color):
        super().__init__()
        self.image = pygame.Surface((1, abs(end_pos - start_pos[1])), 1)
        # self.image = pygame.Surface((abs(end_pos - start_pos[1]), 1))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=start_pos)