from world_engine.classes.camera import Camera
from world_engine.classes.canvas import Canvas
from world_engine.classes.grid import Grid
from world_engine.func.export_to_json import export_to_json
from world_engine.func.import_cut_graphics import import_cut_graphics
from world_engine.func.import_from_json import import_from_json
from world_engine.interface.sidenav import Sidenav
from world_engine.utils.imports import *
from platform import python_version


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

        self.version = "0.1.0"

        self.camera = Camera(self.display_surface)
        self.grid = Grid(self.display_surface, self.config, self.camera.offset)

        # self.cursor_img = pygame.image.load("./assets/sprite/mouse_img.png").convert_alpha()
        cursor_image = pygame.image.load("./assets/sprite/mouse.png").convert_alpha()
        cursor = pygame.Cursor((0, 0), cursor_image)
        pygame.mouse.set_cursor(cursor)

        self.tile_sheet = import_cut_graphics(self.config.tileset, self.config)

        self.sidenav = Sidenav(self.display_surface, self.config)

        self.canvas = Canvas(self.display_surface, self.camera, self.config)

        self.debugger = None

        print(f"World Engine v{self.version} (Python {python_version()}, pygame-ce {pygame.ver})")


    def get_tile_index(self):
        if pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] < self.sidenav.sidenav_width:
            if pygame.mouse.get_pos()[1] > self.sidenav.layer_surface_height:
                for sprite in self.sidenav.tile_group:
                    if int(self.mouse_rect.topleft[0] // (self.config.screen_multiplier / self.config.display_surface_multiplier)) - 1 in range(sprite.rect.topleft[0], sprite.rect.topright[0]):
                        if (int(self.mouse_rect.topleft[1] - self.sidenav.layer_surface_height) // (self.config.screen_multiplier / self.config.display_surface_multiplier)) - 1 - self.sidenav.scroll_height in range(sprite.rect.topleft[1], sprite.rect.bottomleft[1]):
                            self.current_tile = sprite.tile_index


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
                    if event.key == pygame.K_i:
                        import_from_json("./world_engine/build.json", self.camera, self.canvas, self.tile_sheet, self.config)
                        # self.canvas.tile_positions = []
                        # for sprite in self.camera.sprites():
                            # position = [sprite.rect.x // self.config.tile_size, sprite.rect.y // self.config.tile_size]
                            # if position not in self.canvas.tile_positions:
                                # self.canvas.tile_positions.append(position)
                            # else:
                                # pass
                elif event.type == pygame.MOUSEWHEEL:
                    if (len(self.sidenav.tiles) * -self.config.tile_size) + (self.config.tile_size * self.config.screen_multiplier) <= self.sidenav.scroll_height + (event.y) * 5 <= 0:
                        self.sidenav.scroll_height += (event.y) * 5
                self.sidenav.get_tile_index()
                self.canvas.get_mouse_click(self.sidenav.current_tile)
            # self.sidenav.get_mouse_click(self.current_tile)

            self.delta_time = self.clock.tick(self.fps) / 1000
            self.display_surface.fill((0, 0, 0))

            self.camera.draw()
            self.camera.update(self.delta_time)
            # self.canvas.create_ghost_sprite(int(int((pygame.mouse.get_pos()[0] / ((pygame.display.get_surface().get_width() / 198) / self.config.display_surface_multiplier)) - self.camera.offset.x) // self.config.tile_size) * self.config.tile_size, int(int((pygame.mouse.get_pos()[1] / ((pygame.display.get_surface().get_height() / 108) / self.config.display_surface_multiplier)) + self.camera.offset.y) // self.config.tile_size) * self.config.tile_size)

            self.sidenav.draw()
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))
            if self.config.debug == True:
                self.debugger.draw()

            pygame.display.update()