from world_engine.func.import_cut_graphics import import_cut_graphics
from world_engine.utils.imports import *


class Canvas:
    def __init__(self, display_surface, camera, config) -> None:
        self.config = config
        self.display_surface = display_surface
        self.tileset = list(import_cut_graphics(self.config.tileset, self.config))

        self.camera: pygame.sprite.Group = camera
        self.tile_index = 0
        self.sidenav_width = (pygame.display.get_surface().get_width() / self.config.screen_multiplier) * (3 / 2)

        self.tile_positions = []
    

    def create_ghost_sprite(self, current_x, current_y):
        position = (0, 0)
        for sprite in self.camera.sprites():
            position = (sprite.rect.topleft[0] // self.config.tile_size, sprite.rect.topleft[1] // self.config.tile_size)
        
        if current_x != position[0] and current_y != position[1]:
            tile = self.tileset[self.tile_index]
            tile.set_alpha(255 * (2 / 3))
            self.display_surface.blit(tile, (current_x, current_y))


    def get_mouse_click(self, tile_layer, tile_index):
        self.tile_index = tile_index
        if pygame.mouse.get_pos()[0] > self.sidenav_width:
            current_x = int(int((pygame.mouse.get_pos()[0] / ((pygame.display.get_surface().get_width() / 198) / self.config.display_surface_multiplier)) + self.camera.offset.x) // self.config.tile_size) * self.config.tile_size
            current_y = int(int((pygame.mouse.get_pos()[1] / ((pygame.display.get_surface().get_height() / 108) / self.config.display_surface_multiplier)) + self.camera.offset.y) // self.config.tile_size) * self.config.tile_size

            if pygame.mouse.get_pressed()[0]:
                tile_sprite = self.tileset[int(self.tile_index)]
                tile_pos = [current_x // self.config.tile_size, current_y // self.config.tile_size]

                if tile_pos not in self.tile_positions:
                    self.tile_positions.append(tile_pos)
                    # StaticTile(tile_sprite, self.tile_index, (tile_pos[0] * self.config.tile_size, tile_pos[1] * self.config.tile_size), tile_layer, self.camera, self.config)
            
            elif pygame.mouse.get_pressed()[2]:
                for sprite in self.camera.sprites():
                    if sprite.rect.x == current_x and sprite.rect.y == current_y:
                        self.tile_positions.remove([current_x // self.config.tile_size, current_y // self.config.tile_size])
                        self.camera.remove(sprite)