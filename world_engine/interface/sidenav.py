from world_engine.func.import_cut_graphics import import_cut_graphics
from world_engine.utils.imports import *


class Sidenav:
    def __init__(self, display_surface, config) -> None:
        self.config = config
        self.display_surface = display_surface
        self.surface = pygame.Surface((198 / self.config.display_surface_multiplier, 108 * self.config.screen_multiplier))
        self.layers = []
        tiles = list(import_cut_graphics(self.config.tileset, self.config).keys())
        self.tiles = array_split(tiles, len(tiles) // 4)

        self.tile_surface = pygame.Surface((self.surface.get_width() - 2, len(self.tiles) * self.config.tile_size))
        self.layer_surface = pygame.Surface((self.surface.get_width() - 2, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) - 1))

        self.scroll_height = 0
    

    def draw(self):
        self.tile_surface.fill((25, 35, 45))
        self.layer_surface.fill((25, 35, 45))
        self.surface.fill((40, 50, 60))
        for y, tile_group in enumerate(self.tiles):
            for x, tile in enumerate(tile_group):
                self.tile_surface.blit(tile, (x * (self.config.tile_size + 2) + ((self.surface.get_width() - ((self.config.tile_size * 4) + (self.config.screen_multiplier / self.config.display_surface_multiplier))) // 2), y * (self.config.tile_size + 2) + 2 + self.scroll_height))

        self.surface.blit(self.layer_surface, (1, 1))
        self.surface.blit(self.tile_surface, (1, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) + 1))
        self.display_surface.blit(self.surface, (0, 0))