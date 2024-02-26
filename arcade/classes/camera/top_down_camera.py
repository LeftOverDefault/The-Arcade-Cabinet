from arcade.utils.imports import *

class TopDownCamera:
    def __init__(self, display_surface: pygame.Surface, player: pygame.sprite.Sprite) -> None:
        self.display_surface = display_surface
        self.player = player

        self.offset = pygame.Vector2()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

        self.groups = []

    
    def add_group(self, group) -> None:
        self.groups.append(group)
    

    def add_player_collision_groups(self) -> None:
        self.player.collision_groups.append(group for group in self.groups if group.collidable == True)

    
    def center_target_camera(self, target) -> None:
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height


    def draw(self) -> None:
        self.center_target_camera(target=self.player)

        for group in self.groups:
            if group.y_sorted == True:
                for sprite in sorted(group.sprites(), key=lambda sprite: sprite.rect.centery):
                    offset_position = sprite.rect.center - self.offset
                    self.display_surface.blit(source=sprite.image, dest=offset_position)