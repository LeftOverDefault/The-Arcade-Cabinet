from arcade.classes.sprite.sprite import Sprite
from arcade.func.import_folder import import_folder
from arcade.utils.imports import *


class AnimatedSprite(Sprite):
    def __init__(self, path, position, group) -> None:
        super().__init__(path, position, group)
        self.frame_index = 0
        self.animations = import_folder(path)
        self.image = pygame.image.load(f"{path}0.png").convert_alpha()

    
    def animate(self, delta_time) -> None:
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed * delta_time

        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]