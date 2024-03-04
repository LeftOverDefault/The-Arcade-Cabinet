from world_engine.func.array_split import array_split
from world_engine.func.import_cut_graphics import import_cut_graphics
from world_engine.utils.imports import *


class Sidenav:
    def __init__(self, display_surface, config) -> None:
        self.config = config
        self.display_surface = display_surface
        self.surface = pygame.Surface((198 / self.config.display_surface_multiplier, 108 * self.config.screen_multiplier))
        self.layers = []
        self.tiles_per_row = 4
        tiles = list(import_cut_graphics(self.config.tileset, self.config).keys())
        self.tiles = array_split(tiles, len(tiles) // self.tiles_per_row)

        self.tile_surface = pygame.Surface((self.surface.get_width() - 2, len(self.tiles) * self.config.tile_size))
        # self.tile_group = pygame.sprite.Group()
        # self.layer_surface = pygame.Surface((self.surface.get_width() - 2, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) - 1))

        self.scroll_height = 0

        self.sidenav_width = (pygame.display.get_surface().get_width() / self.config.screen_multiplier) * (3 / 2)
        self.layer_surface_height = (self.surface.get_height() // self.config.screen_multiplier) * (self.config.display_surface_multiplier)


    def draw(self) -> None:
        self.surface.fill((40, 50, 60))
        self.tile_surface.fill((25, 35, 45))
        # self.layer_surface.fill((25, 35, 45))
        for y, tile_group in enumerate(self.tiles):
            for x, tile in enumerate(tile_group):
                self.tile_surface.blit(tile, (x * (self.config.tile_size + 0), y * (self.config.tile_size + 0) + self.scroll_height))
                # self.tile_surface.blit(tile, (x * (self.config.tile_size + 2) + ((self.surface.get_width() - ((self.config.tile_size * 4) + (self.config.screen_multiplier / self.config.display_surface_multiplier))) // 2), y * (self.config.tile_size + 2) + 2 + self.scroll_height))

        # self.surface.blit(self.layer_surface, (1, 1))
        # self.tile_group.draw(self.tile_surface)
        self.surface.blit(self.tile_surface, (0, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) + 1))
        self.display_surface.blit(self.surface, (0, 0))