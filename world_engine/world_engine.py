from world_engine.classes.camera import Camera
from world_engine.utils.imports import *


class WorldEngine:
    """
    An Engine for generating worlds stored as JSON files to be read by the `arcade` module.
    """
    def __init__(self) -> None:
        self.version = "0.1.0"
        pygame.init()
        pygame.display.set_caption(f"World Engine v{self.version}")
        self.on_init()

    
    def on_init(self):
        self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
        self.display_surface = pygame.Surface((198 * 2, 108 * 2))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.running = True
        self.fullscreen = False

        self.camera = Camera(self.display_surface)

        mouse_image = pygame.image.load("./assets/sprite/mouse.png").convert_alpha()
        cursor = pygame.cursors.Cursor((0, 0), mouse_image)
        pygame.mouse.set_cursor(cursor)


        self.origin = pygame.Vector2()


    def render(self) -> None:
        self.camera.draw()

    def update(self) -> None:
        self.camera.update(self.delta_time)


    def events(self, event) -> None:
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:
                self.fullscreen = not self.fullscreen
                if self.fullscreen == True:
                    self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                else:
                    self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
            elif event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                self.events(event)
            
            self.delta_time = self.clock.tick(self.fps) / 1000

            self.display_surface.fill((0, 0, 0))

            self.render()
            self.update()

            pygame.draw.circle(self.display_surface, "red", self.origin, 5)
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))

            pygame.display.update()