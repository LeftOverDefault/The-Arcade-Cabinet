from arcade.classes.player import Player
from arcade.utils.imports import *


class Camera(pygame.sprite.Group):
    def __init__(self, display_surface: pygame.Surface) -> None:
        super().__init__()
        self.display_surface = display_surface

        self.offset = pygame.math.Vector2()
        self.half_width = self.display_surface.get_width() // 2
        self.half_height = self.display_surface.get_height() // 2

        self.camera_borders = {'left': 100, 'right': 100, 'top': 50, 'bottom': 50}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.display_surface.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.display_surface.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.camera_rect = pygame.Rect(l,t,w,h)

        self.mouse_speed = 0.15
        self.keyboard_speed = 3.5


    def center_target_camera(self, target: pygame.sprite.Sprite):
        self.offset.x = target.rect.centerx - self.half_width
        self.offset.y = target.rect.centery - self.half_height


    def delayed_center_target_camera(self, target):
        self.offset.x += (target.rect.centerx - self.half_width - self.offset.x) / config["camera_delay"]
        self.offset.y += (target.rect.centery - self.half_height - self.offset.y) / config["camera_delay"]
    

    def box_target_camera(self,target):
        if target.rect.left < self.camera_rect.left:
            self.camera_rect.left = target.rect.left
        if target.rect.right > self.camera_rect.right:
            self.camera_rect.right = target.rect.right
        if target.rect.top < self.camera_rect.top:
            self.camera_rect.top = target.rect.top
        if target.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = target.rect.bottom

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
    

    def keyboard_control_camera(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.camera_rect.x -= self.keyboard_speed
        if keys[pygame.K_RIGHT]: self.camera_rect.x += self.keyboard_speed
        if keys[pygame.K_UP]: self.camera_rect.y -= self.keyboard_speed
        if keys[pygame.K_DOWN]: self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_borders["left"]
        self.offset.y = self.camera_rect.top - self.camera_borders["top"]


    
    def mouse_control_camera(self):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()

        left_border = self.camera_borders["left"]
        top_border = self.camera_borders["top"]
        right_border = self.display_surface.get_size()[0] - self.camera_borders["right"]
        bottom_border = self.display_surface.get_size()[1] - self.camera_borders["bottom"]

        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
            # if mouse.x < left_border - (left_border * 2 / 3):
                # pygame.mouse.set_pos((left_border - (left_border * 2 / 3),mouse.y))
        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border,top_border)
                # pygame.mouse.set_pos((left_border,top_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border,top_border)
            # if mouse.x > right_border / 2:
                # pygame.mouse.set_pos((right_border * 2 / 3,top_border))
        elif mouse.y > bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border,bottom_border)
                # pygame.mouse.set_pos((left_border,bottom_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border,bottom_border)
                # pygame.mouse.set_pos((right_border,bottom_border))

        if left_border < mouse.x < right_border:
            if mouse.y < top_border:
                mouse_offset_vector.y = mouse.y - top_border
                # pygame.mouse.set_pos((mouse.x,top_border - 1))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                # pygame.mouse.set_pos((mouse.x,bottom_border))

        self.offset += mouse_offset_vector * self.mouse_speed

    def draw(self, player):
        self.delayed_center_target_camera(target=player)

        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)

        # for group in self.y_sorted_groups:
        #     for sprite in sorted(group, key=lambda sprite: sprite.rect.centery):
        #         offset_pos = sprite.rect.topleft - self.offset
        #         self.display_surface.blit(source=sprite.image, dest=offset_pos)

        # for sprite in self.sprites_array:
        #     offset_pos = sprite.rect.topleft - self.offset
        #     self.display_surface.blit(source=sprite.image, dest=offset_pos)