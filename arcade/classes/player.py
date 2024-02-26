from arcade.func.map_to_keys import map_to_keys
from arcade.utils.imports import *


class Player(pygame.sprite.Sprite):
    def __init__(self, group) -> None:
        super().__init__(group)

        self.image = pygame.Surface((config["tile_size"], config["tile_size"]))
        self.image = pygame.transform.scale_by(self.image, config["scale_factor"])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(center=(0, 0))

        self.direction = pygame.Vector2()
        self.speed = 200

        self.keys = {}
        for key in config["keys"]:
            self.keys[key] = map_to_keys(config["keys"][key])

    
    def input(self):
        keys = pygame.key.get_pressed()

        if keys[self.keys["move_up"]]:
            self.direction.y = -1
        elif keys[self.keys["move_down"]]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if keys[self.keys["move_left"]]:
            self.direction.x = -1
        elif keys[self.keys["move_right"]]:
            self.direction.x = 1
        else:
            self.direction.x = 0
    

    def move(self, delta_time):
        if self.direction.magnitude() > 0:
            self.direction.normalize()
        
        self.rect.x += self.direction.x * self.speed * delta_time
        self.rect.y += self.direction.y * self.speed * delta_time


    # def collide_x(self):
        # 


    def update(self, delta_time):
        self.input()
        self.move(delta_time=delta_time)