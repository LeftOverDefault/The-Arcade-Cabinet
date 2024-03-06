from world_engine.classes.tile.static_tile import StaticTile
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
        self.original_tiles = dict(import_cut_graphics(self.config.tileset, self.config))
        self.tiles = list(array_split(list(self.original_tiles.keys()), len(list(self.original_tiles.keys())) // self.tiles_per_row))

        self.tile_surface = pygame.Surface((self.surface.get_width() - 2, len(self.tiles) * self.config.tile_size))
        self.tile_group = pygame.sprite.Group()
        # self.layer_surface = pygame.Surface((self.surface.get_width() - 2, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) - 1))

        self.scroll_height = 0

        self.sidenav_width = (pygame.display.get_surface().get_width() / self.config.screen_multiplier) * (3 / 2)
        self.layer_surface_height = (self.surface.get_height() // self.config.screen_multiplier) * (self.config.display_surface_multiplier)
        self.tile_surface.fill((25, 35, 45))

        for y, tile_group in enumerate(self.tiles):
            for x, tile in enumerate(tile_group):
                tile_index = (y * self.tiles_per_row) + x
                StaticTile(tile, list(self.original_tiles.values())[tile_index], (x * (self.config.tile_size), (y * (self.config.tile_size))), self.tile_group, self.config)
                # self.tile_surface.blit(tile, (x * (self.config.tile_size + 1), y * (self.config.tile_size + 1) + self.scroll_height))
                # self.tile_surface.blit(tile, (x * (self.config.tile_size + 2) + ((self.surface.get_width() - ((self.config.tile_size * 4) + (self.config.screen_multiplier / self.config.display_surface_multiplier))) // 2), y * (self.config.tile_size + 2) + 2 + self.scroll_height))


    def draw(self) -> None:
        # self.layer_surface.fill((25, 35, 45))
        # self.surface.blit(self.layer_surface, (1, 1))
        self.surface.fill((40, 50, 60))
        self.tile_group.draw(self.tile_surface)
        self.surface.blit(self.tile_surface, (1, (self.surface.get_height() // self.config.screen_multiplier) * (2 / 3) + 1 + self.scroll_height))
        self.display_surface.blit(self.surface, (0, 0))