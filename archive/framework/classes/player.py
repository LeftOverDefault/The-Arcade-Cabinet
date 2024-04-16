from re import S
from framework.func.import_folder import import_folder
from framework.utils.imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, path, initial_position, group) -> None:
        super().__init__(group)
        self.image = pygame.image.load(path + "idle_down/0.png").convert_alpha()
        self.rect = self.image.get_rect(center=initial_position)
        self.attack_surf = pygame.Surface((16, 16))
        self.attack_surf.fill((255, 0, 0))
        self.attack_rect = self.attack_surf.get_rect(topleft=initial_position)

        self.direction = pygame.Vector2()
        self.position = pygame.Vector2(initial_position)

        self.animation_speed = 4.5
        self.frame_index = 0
        self.speed = 75
        self.status = "idle_down"

        self.collision_groups = []

        self.get_animations(path)


    def get_animations(self, path) -> None:
        self.animations = {
            "idle_down": [], "idle_left": [], "idle_right": [], "idle_up": [],
            "run_down": [], "run_left": [], "run_right": [], "run_up": []
        }

        for animation in self.animations.keys():
            full_path = path + animation + "/"
            self.animations[animation] = import_folder(full_path)
    

    def get_status(self) -> None:
        if int(self.position.y) == self.rect.centery and int(self.position.x) == self.rect.centerx:
            if not "idle" in self.status:
                if "run" in self.status:
                    self.status = self.status.replace("run_", "idle_")


    def animate(self, delta_time) -> None:
        animation = self.animations[self.status]
        self.frame_index += self.animation_speed * delta_time

        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
            self.status = "run_up"
        elif keys[pygame.K_s]:
            self.direction.y = 1
            self.status = "run_down"
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
            self.status = "run_left"
        elif keys[pygame.K_d]:
            self.direction.x = 1
            self.status = "run_right"
        else:
            self.direction.x = 0
        # if keys[pygame.K_k]:
            # self.status = "attack_" + self.status.split("_")[1]
        
    
    def move(self, delta_time):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        self.rect.x += round(number=self.direction.x * self.speed * delta_time)
        self.collide_x()
        self.rect.y += round(number=self.direction.y * self.speed * delta_time)
        self.collide_y()
    

    def update_attack_rect(self) -> None:
        self.attack_rect.x = self.position.x
        self.attack_rect.y = self.position.y


    def collide_x(self) -> None:
        for group in self.collision_groups:
            for chunk in group.chunks:
                for sprite in chunk:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.x > 0:
                            self.rect.right = sprite.rect.left
                        elif self.direction.x < 0:
                            self.rect.left = sprite.rect.right


    def collide_y(self) -> None:
        for group in self.collision_groups:
            for chunk in group.chunks:
                for sprite in chunk:
                    if sprite.rect.colliderect(self.rect):
                        if self.direction.y > 0:
                            self.rect.bottom = sprite.rect.top
                        elif self.direction.y < 0:
                            self.rect.top = sprite.rect.bottom


    def update_position(self) -> None:
        self.position.x = self.rect.centerx
        self.position.y = self.rect.centery


    def update(self, delta_time):
        self.input()
        self.move(delta_time=delta_time)
        self.get_status()
        self.animate(delta_time=delta_time)
        self.update_position()
        self.update_attack_rect()