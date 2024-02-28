from arcade.utils.imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((16, 16))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=initial_position)

        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(initial_position)
        self.speed = 75

        self.collision_groups = []


    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_w]:
            self.direction.y = -1
        elif keys[pygame.K_s]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[pygame.K_a]:
            self.direction.x = -1
        elif keys[pygame.K_d]:
            self.direction.x = 1
        else:
            self.direction.x = 0


    def move(self, delta_time):
        if self.direction.magnitude() > 0:
            self.direction.normalize()

        self.rect.x += round(self.direction.x * self.speed * delta_time)
        self.rect.y += round(self.direction.y * self.speed * delta_time)
        self.position.x = self.rect.centerx
        self.position.y = self.rect.centery


    def update(self, delta_time):
        self.input()
        self.move(delta_time)