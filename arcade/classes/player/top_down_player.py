from arcade.utils.imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, initial_position, group) -> None:
        super().__init__(group)
        self.image = pygame.Surface((16, 16))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=initial_position)

        self.direction = pygame.Vector2()
        self.speed = 10

        self.collidable_groups = []

    
    def input(self) -> None:
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
    

    def move(self, delta_time) -> None:
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.rect.x += self.direction.x * self.speed * delta_time
        self.collide_x(self)
        self.rect.y += self.direction.y * self.speed * delta_time
        self.collide_y(self)


    def collide_x(self) -> None:
        for group in self.collidable_groups:
            for sprite in group:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.x > 0:
                        self.rect.right = sprite.rect.left
                    if self.direction.x < 0:
                        self.rect.left = sprite.rect.right


    def collide_y(self) -> None:
        for group in self.collidable_groups:
            for sprite in group:
                if sprite.rect.colliderect(self.rect):
                    if self.direction.y > 0:
                        self.rect.bottom = sprite.rect.top
                    if self.direction.y < 0:
                        self.rect.top = sprite.rect.bottom


    def update(self, delta_time) -> None:
        self.input()
        self.move()