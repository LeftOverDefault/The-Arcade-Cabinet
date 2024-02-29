from arcade.classes.layer import Layer
from arcade.utils.imports import *


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface) -> None:
        super().__init__()
        self.display_surface = display_surface

        self.offset = pygame.Vector2()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        
        self.y_sorts = Layer(True, False)

        self.camera_delay = 25


    def center_target_camera(self, target):
        self.offset.x += (target.rect.centerx - self.half_width - self.offset.x) / self.camera_delay
        self.offset.y += (target.rect.centery - self.half_height - self.offset.y) / self.camera_delay


    def add_group(self, group, player) -> None:
        if group.collidable:
            player.collision_groups.append(group)

        if group.y_sorted == True:
            for sprite in group.sprites():
                self.y_sorts.add(sprite)
        else:
            for sprite in group:
                self.add(sprite)


    def draw(self, player):
        self.center_target_camera(target=player)

        for sprite in self:
            offset = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset)

        for sprite in sorted(self.y_sorts.sprites(), key=lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(source=sprite.image, dest=offset_pos)
    

    def update(self, delta_time):
        for sprite in self:
            sprite.update(delta_time)

        for sprite in self.y_sorts.sprites():
            sprite.update(delta_time)