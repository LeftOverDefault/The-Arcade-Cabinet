from world_engine.classes.line import HorizontalLineSprite, VerticalLineSprite
from world_engine.utils.imports import *


class Grid:
    def __init__(self, display_surface: pygame.Surface, config, camera_offset) -> None:
        self.display_surface = display_surface
        self.config = config

        self.camera_offset = camera_offset



    def draw_lines(self) -> None:
        self.group = []
        width = self.display_surface.get_width()
        height = self.display_surface.get_height()

        columns = width // self.config.tile_size
        rows = height // self.config.tile_size

        offset_vector = pygame.Vector2(
            x = self.camera_offset.x - (int(self.camera_offset.x / self.config.tile_size) * self.config.tile_size),
            y = self.camera_offset.y - (int(self.camera_offset.y / self.config.tile_size) * self.config.tile_size)
        )

        for column in range(columns + 1):
            x = offset_vector.x + column * self.config.tile_size
            self.group.append(VerticalLineSprite((x, offset_vector.y), height, pygame.Color("black")))
        
        for row in range(rows + 1):
            y = offset_vector.y + row * self.config.tile_size
            self.group.append(HorizontalLineSprite((offset_vector.x, y), width, pygame.Color("black")))