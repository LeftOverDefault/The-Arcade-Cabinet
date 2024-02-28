from arcade.utils.imports import *


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface) -> None:
        super().__init__()
        self.display_surface = display_surface

        self.offset = pygame.Vector2()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2
        
        self.y_sorts = []


    def center_target_camera(self, target):
        self.offset.x += (target.rect.centerx - self.half_width - self.offset.x) / 30
        self.offset.y += (target.rect.centery - self.half_height - self.offset.y) / 30
    
    
    def add_group(self, group, player):
        if group.collidable:
            player.collision_groups.append(group)

        if group.y_sorted == True:
            self.y_sorts.append(group)
        else:
            for sprite in group:
                self.add(sprite)


    def draw(self, player):
        self.center_target_camera(player)

        for sprite in self:
            offset = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset)

        for group in self.y_sorts:
            for sprite in sorted(group, lambda sprite: sprite.rect.centery):
                offset = sprite.rect.topleft - self.offset
                self.display_surface.blit(sprite.image, offset)