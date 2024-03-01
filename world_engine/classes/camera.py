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
        self.keyboard_speed = 75
        self.mouse_speed = 2

        self.camera_borders = {'left': 50, 'right': 50, 'top': 25, 'bottom': 25}
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = (self.display_surface.get_size()[0]  - (self.camera_borders['left'] + self.camera_borders['right']))
        h = (self.display_surface.get_size()[1]  - (self.camera_borders['top'] + self.camera_borders['bottom']))
        self.camera_rect = pygame.Rect(l,t,w,h)

    
    def keyboard_control(self, delta_time):
        keys = pygame.key.get_pressed()
        direction = pygame.Vector2()

        if keys[pygame.K_w]:
            direction.y = -1
        elif keys[pygame.K_s]:
            direction.y = 1
        else:
            direction.y = 0
        
        if keys[pygame.K_a]:
            direction.x = -1
        elif keys[pygame.K_d]:
            direction.x = 1
        else:
            direction.x = 0


        if direction.magnitude() > 0:
            direction = direction.normalize()

        self.offset += direction * self.keyboard_speed * delta_time


    def mouse_control(self, delta_time):
        mouse = pygame.math.Vector2(pygame.mouse.get_pos())
        mouse_offset_vector = pygame.math.Vector2()

        left_border = self.camera_borders['left']
        top_border = self.camera_borders['top']
        right_border = (self.display_surface.get_size()[0] * 4) - self.camera_borders['right']
        bottom_border = (self.display_surface.get_size()[1] * 4) - self.camera_borders['bottom']


        print(left_border, top_border, right_border, bottom_border)

        if top_border < mouse.y < bottom_border:
            if mouse.x < left_border:
                mouse_offset_vector.x = mouse.x - left_border
                # pygame.mouse.set_pos((left_border,mouse.y))
            if mouse.x > right_border:
                mouse_offset_vector.x = mouse.x - right_border
                # pygame.mouse.set_pos((right_border,mouse.y))
        elif mouse.y < top_border:
            if mouse.x < left_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(left_border,top_border)
                # pygame.mouse.set_pos((left_border,top_border))
            if mouse.x > right_border:
                mouse_offset_vector = mouse - pygame.math.Vector2(right_border,top_border)
                # pygame.mouse.set_pos((right_border,top_border))
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
                # pygame.mouse.set_pos((mouse.x,top_border))
            if mouse.y > bottom_border:
                mouse_offset_vector.y = mouse.y - bottom_border
                # pygame.mouse.set_pos((mouse.x,bottom_border))

        self.offset += mouse_offset_vector * self.mouse_speed * delta_time


    def draw(self):
        for sprite in self:
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_position)


    def update(self, delta_time):
        self.keyboard_control(delta_time)
        # self.mouse_control(delta_time)