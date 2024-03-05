from platform import python_version
# from arcade.classes.camera import Camera
from arcade.classes.configure import Configure
# from arcade.classes.player import Player
# from arcade.debug.debugger import Debugger
# from arcade.utils.imports import *
from arcade import *


class Arcade:
    def __init__(self, config) -> None:
        self.version = "0.1.0"
        self.config = Configure(config)

        pygame.init()
        pygame.display.set_caption(f"{self.config.name} v{self.config.version}")

        self.on_init()


    def on_init(self):
        self.screen = pygame.display.set_mode((192 * 6, 108 * 6))
        self.display_surface = pygame.Surface((192 * 1.5, 108 * 1.5))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.fullscreen = False
        self.running = True

        print(f"Arcade v{self.version} (Python {python_version()}, pygame-ce {pygame.ver})")


    def render(self):
        ...


    def update(self):
        ...


    def event(self, event):
        ...


    def run(self):
        while self.running:
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
                            self.screen = pygame.display.set_mode((192 * 6, 108 * 6))
                self.event(event=event)

            self.display_surface.fill((0, 0, 0))

            self.delta_time = self.clock.tick(self.fps) / 1000

            self.render()
            self.update()

            pygame.display.update()