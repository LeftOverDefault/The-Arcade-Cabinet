from world_engine.classes.camera import Camera
from world_engine.classes.canvas import Canvas
from world_engine.classes.grid import Grid
from world_engine.classes.tile.static_tile import StaticTile
from world_engine.func.export_to_json import export_to_json
from world_engine.func.import_cut_graphics import import_cut_graphics
from world_engine.interface.sidenav import Sidenav
from world_engine.utils.imports import *


class WorldEngine:
    def __init__(self, config) -> None:
        pygame.init()
        pygame.display.set_caption("World Engine v0.1.0")

        self.config = config
        self.screen = pygame.display.set_mode((198 * self.config.screen_multiplier, 108 * self.config.screen_multiplier))
        self.display_surface = pygame.Surface((198 * self.config.display_surface_multiplier, 108 * self.config.display_surface_multiplier))
        self.clock = pygame.time.Clock()
        self.fps = 60

        self.running = True
        self.fullscreen = False

        self.camera = Camera(self.display_surface)
        self.grid = Grid(self.display_surface, self.config, self.camera.offset)

        # self.cursor_img = pygame.image.load("./assets/sprite/mouse_img.png").convert_alpha()
        cursor_image = pygame.image.load("./assets/sprite/mouse.png").convert_alpha()
        cursor = pygame.Cursor((0, 0), cursor_image)
        pygame.mouse.set_cursor(cursor)

        self.tile_sheet = import_cut_graphics(self.config.tileset, self.config)

        self.current_tile = 0

        self.sidenav = Sidenav(self.display_surface, self.config)

        self.canvas = Canvas(self.display_surface, self.camera, self.config)


    # def get_mouse_click(self):
    #     if pygame.mouse.get_pos()[0] > (self.sidenav.surface.get_width() * ((self.screen.get_width() / 198) / self.config.display_surface_multiplier)):
    #         distance_to_origin_x = (pygame.mouse.get_pos()[0] / ((self.screen.get_width() / 198) / self.config.display_surface_multiplier)) + self.camera.offset.x
    #         distance_to_origin_y = (pygame.mouse.get_pos()[1] / ((self.screen.get_height() / 108) / self.config.display_surface_multiplier)) + self.camera.offset.y

    #         current_x = int((distance_to_origin_x // self.config.tile_size) * self.config.tile_size)
    #         current_y = int((distance_to_origin_y // self.config.tile_size) * self.config.tile_size)

    #         if pygame.mouse.get_pressed()[0]:
    #             StaticTile(list(self.tile_sheet.keys())[self.current_tile], list(self.tile_sheet.values())[self.current_tile], (current_x, current_y), self.camera, self.config)

    #         elif pygame.mouse.get_pressed()[2]:
    #             for sprite in self.camera.sprites():
    #                 if sprite.rect.x == current_x and sprite.rect.y == current_y:
    #                     self.camera.remove(sprite)

    #     elif pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < (self.sidenav.surface.get_width() * ((self.screen.get_width() / 198) / self.config.display_surface_multiplier)):
    #         if pygame.mouse.get_pos()[1] > (self.sidenav.surface.get_height() // self.config.display_surface_multiplier) * (2 / 3) + 1:
    #             distance_to_origin_x = (pygame.mouse.get_pos()[0] / ((self.screen.get_width() / 198) / self.config.display_surface_multiplier)) - 18
    #             distance_to_origin_y = (((pygame.mouse.get_pos()[1] / ((self.screen.get_height() / 108) / self.config.display_surface_multiplier)) - (self.sidenav.surface.get_height() / self.config.display_surface_multiplier) * (1 / 3) / self.config.display_surface_multiplier) - (self.config.screen_multiplier / self.config.display_surface_multiplier) - self.sidenav.scroll_height)

    #             current_x = int((distance_to_origin_x // self.config.tile_size) * self.config.tile_size)
    #             current_y = int((distance_to_origin_y // self.config.tile_size) * self.config.tile_size)

    #             print(distance_to_origin_x, distance_to_origin_y)

    #             if current_x >= 0 and current_y >= 0:
    #                 current_tile = (current_x / self.config.tile_size, current_y / self.config.tile_size)
    #                 tile_index = 0
    #                 for i in range(4):
    #                     for j in range(len(self.sidenav.tiles)):
    #                         if i == current_tile[0] and j == current_tile[1]:
    #                             tile_index = (j * 4) + i
    #                 self.current_tile = tile_index


    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.fullscreen = not self.fullscreen
                        if self.fullscreen == True:
                            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((198 * self.config.screen_multiplier, 108 * self.config.screen_multiplier))
                    if event.key == pygame.K_e:
                        export_to_json(self.camera, self.config)
                elif event.type == pygame.MOUSEWHEEL:
                    if self.sidenav.scroll_height + (event.y) * 3 <= 0:
                        self.sidenav.scroll_height += (event.y) * 3
                self.canvas.get_mouse_click()

            self.delta_time = self.clock.tick(self.fps) / 1000
            self.display_surface.fill((0, 0, 0))


            # self.canvas.create_ghost_sprite(int(int((pygame.mouse.get_pos()[0] / ((pygame.display.get_surface().get_width() / 198) / self.config.display_surface_multiplier)) + self.camera.offset.x) // self.config.tile_size) * self.config.tile_size, int(int((pygame.mouse.get_pos()[1] / ((pygame.display.get_surface().get_height() / 108) / self.config.display_surface_multiplier)) + self.camera.offset.y) // self.config.tile_size) * self.config.tile_size)
            self.camera.draw()
            self.camera.update(self.delta_time)

            self.sidenav.draw()
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))

            pygame.display.update()