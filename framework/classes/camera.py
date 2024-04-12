from framework.classes.layer import Layer
from framework.utils.imports import *


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface) -> None:
        super().__init__()
        self.display_surface = display_surface

        self.offset = pygame.Vector2()

        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

        self.camera_delay = 25

        self.layers = []


    def add_group(self, layer, player):
        if layer.collidable == True:
            player.collision_groups.append(layer)
        
        if layer.y_sorted == True:
            for chunk in layer.chunks:
                for sprite in chunk:
                    sprite.visible = chunk.visible
                    self.add(sprite)
        else:
            self.layers.append(layer)
    

    def center_target_camera(self, target):
        self.offset.x += round((target.rect.centerx - self.half_width - self.offset.x) / self.camera_delay, 4)
        self.offset.y += round((target.rect.centery - self.half_height - self.offset.y) / self.camera_delay, 4)


    def update(self, delta_time) -> None:

        for layer in self.layers:
            layer.update(delta_time)
        
        for sprite in self:
            sprite.update(delta_time)
    

    def render(self, player) -> None:
        self.center_target_camera(target=player)

        for layer in sorted(self.layers, key=lambda layer: layer.z_index):
            for chunk in layer.chunks:
                chunk.render()
                if chunk.visible == True:
                    for sprite in chunk:
                        offset = sprite.rect.topleft - self.offset
                        self.display_surface.blit(sprite.image, offset)


        # for layer in self.y_sort_layer:
        #     for chunk in layer.chunks:
        #         chunk.render()
        #         if chunk.visible == True:
        #             for sprite in sorted(chunk.sprites(), key=lambda sprite: sprite.rect.centery):
        #                 offset = sprite.rect.topleft - self.offset
        #                 self.display_surface.blit(sprite.image, offset)
        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.centery):
            offset = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset)