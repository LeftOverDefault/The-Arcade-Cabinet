from framework.arcade.func.import_folder import import_folder
from framework.arcade.utils.imports import *


# class Particle(pygame.sprite.Sprite):
#     def __init__(self, image_path, position, velocity, acceleration, timer, group) -> None:
#         super().__init__(group)
#         self.get_animations(image_path)
#         self.image = pygame.image.load(f"{image_path}/0.png").convert_alpha()
#         self.rect = self.image.get_rect(topleft=position)

#         self.alive = True

#         self.position = position
#         self.velocity = velocity
#         self.acceleration = acceleration

#         self.timer = timer
#         self.lifetime = 0

#         self.animation_speed = len(self.animation) + (len(self.animation) // 2)
#         self.frame_index = 0
    

#     def get_animations(self, path) -> None:
#         full_path = path + "/"
#         self.animation = import_folder(full_path)
    

#     def animate(self, delta_time) -> None:
#         self.frame_index += self.animation_speed * delta_time

#         if self.frame_index >= len(self.animation):
#             self.frame_index = len(self.animation) - 1

#         self.image = self.animation[int(self.frame_index)]


#     def update(self, delta_time) -> None:
#         self.animate(delta_time)
#         # self.position[0] += self.velocity[0] 
#         # self.position[1] += self.velocity[1]
#         # self.rect.x = self.position[0]
#         # self.rect.y = self.position[1]
#         # self.timer -= delta_time
#         # self.velocity[1] += self.acceleration * delta_time
#         # if self.timer <= self.lifetime:
#             # self.alive = False


class Particle(pygame.sprite.Sprite):
    def __init__(self, image_path, initial_position, particle_system) -> None:
        super().__init__(particle_system)
        self.image = pygame.image.load(f"{image_path}/0.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=initial_position)

        self.get_animations(image_path)

        self.animation_speed = len(self.animation) + (len(self.animation) // 2)
        self.frame_index = 0
    

    def get_animations(self, path) -> None:
        full_path = path + "/"
        self.animation = import_folder(full_path)


    def animate(self, delta_time) -> None:
        self.frame_index += self.animation_speed * delta_time

        if self.frame_index >= len(self.animation):
            self.frame_index = len(self.animation) - 1

        self.image = self.animation[int(self.frame_index)]
    

    def update(self, delta_time) -> None:
        self.animate(delta_time)