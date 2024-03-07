from world_engine.classes.tile.static_tile import StaticTile
from world_engine.font.font import Font
from world_engine.func.array_split import array_split
from world_engine.func.import_cut_graphics import import_cut_graphics
from world_engine.utils.imports import *


class Sidenav:
    def __init__(self, display_surface, config) -> None:
        self.config = config
        self.display_surface = display_surface
        self.surface = pygame.Surface((198 / self.config.display_surface_multiplier, 108 * self.config.screen_multiplier))
        self.layers = self.config.layers
        self.tiles_per_row = 4
        self.original_tiles = dict(import_cut_graphics(self.config.tileset, self.config))
        self.tiles = list(array_split(list(self.original_tiles.keys()), len(list(self.original_tiles.keys())) // self.tiles_per_row))

        self.tile_surface = pygame.Surface((self.surface.get_width() - 2, (len(self.tiles) + 1) * self.config.tile_size))
        self.tile_group = pygame.sprite.Group()
        self.layer_surface = pygame.Surface((self.surface.get_width() - 2, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) - 1))
        self.mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)
        self.scroll_height = 0

        self.current_tile = 0

        self.sidenav_width = (pygame.display.get_surface().get_width() / self.config.screen_multiplier) * (3 / 2)
        self.layer_surface_height = (self.surface.get_height() // self.config.screen_multiplier) * (self.config.display_surface_multiplier)

        for y, tile_group in enumerate(self.tiles):
            for x, tile in enumerate(tile_group):
                tile_index = (y * self.tiles_per_row) + x
                StaticTile(tile, list(self.original_tiles.values())[tile_index], (x * (self.config.tile_size + 1), (y * (self.config.tile_size + 1))), self.tile_group, self.config)

        self.font = Font(self.config.font, 1, (255, 255, 255))

    

    def get_tile_index(self):
        self.mouse_rect.x = pygame.mouse.get_pos()[0]
        self.mouse_rect.y = pygame.mouse.get_pos()[1]
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < self.sidenav_width:
            if pygame.mouse.get_pos()[1] > self.layer_surface_height:
                for sprite in self.tile_group:
                    if int(self.mouse_rect.topleft[0] // (self.config.screen_multiplier / self.config.display_surface_multiplier)) - 1 in range(sprite.rect.topleft[0], sprite.rect.topright[0]):
                        if (int(self.mouse_rect.topleft[1] - self.layer_surface_height) // (self.config.screen_multiplier / self.config.display_surface_multiplier)) - 1 - self.scroll_height in range(sprite.rect.topleft[1], sprite.rect.bottomleft[1]):
                            self.current_tile = sprite.tile_index


    def draw(self) -> None:
        self.layer_surface.fill((25, 35, 45))
        self.surface.fill((40, 50, 60))
        self.tile_surface.fill((25, 35, 45))
        self.tile_group.draw(self.tile_surface)
        self.surface.blit(self.tile_surface, (1, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) + 1 + self.scroll_height))
        for height, layer in enumerate(self.layers):
            self.font.render(self.layer_surface, layer, (4, 2 + (height * self.font.line_height)))
        self.surface.blit(self.layer_surface, (1, 1))
        self.display_surface.blit(self.surface, (0, 0))