from arcade.classes.sprite.sprite import Sprite
from arcade.func.import_folder import import_folder
from arcade.utils.imports import *


class AnimatedSprite(Sprite):
    def __init__(self, path, position, group) -> None:
        super().__init__(path, position, group)
        self.animations = import_folder(path)
        self.image = pygame.image.load(f"{path}0.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)

        self.frame_index = 0
        self.animation_speed = 4.5

    
    def animate(self, delta_time) -> None:
        self.frame_index += self.animation_speed * delta_time

        if self.frame_index >= len(self.animations):
            self.frame_index = 0

        self.image = self.animations[int(self.frame_index)]


    def update(self, delta_time):
        # self.move(delta_time=delta_time)
        self.animate(delta_time)