from framework.debug.debugger import Debugger
from framework.utils.imports import *


class Arcade:
    def __init__(self, config) -> None:
        pygame.init()
        pygame.display.set_caption(config.name)

        self.on_init(config)
    

    def on_init(self, config) -> None:
        self.config = config

        self.screen = pygame.display.set_mode((192 * self.config.screen_multiplier, 108 * self.config.screen_multiplier))
        self.display_surface = pygame.Surface((192 * self.config.display_surface_multiplier, 108 * self.config.display_surface_multiplier))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.delta_time = self.clock.tick(self.fps)

        self.config.fullscreen = False
        self.running = True

        self.debugger = Debugger(self.config.font_path, self.config)

        print(f"arcade 0.1.0 (Python {platform.python_version()})")


    def render(self) -> None:
        ...


    def update(self, delta_time) -> None:
        ...
    

    def events(self, event) -> None:
        ...
    

    def run(self) -> None:
        self.running = True
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_F11:
                        self.config.fullscreen = not self.config.fullscreen

                        if self.config.fullscreen == True:
                            self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        else:
                            self.screen = pygame.display.set_mode((192 * self.config.screen_multiplier, 108 * self.config.screen_multiplier))
                self.events(event)

            self.delta_time = self.clock.tick(self.fps) / 1000
            self.display_surface.fill((40, 42, 50))

            self.render()
            self.update(self.delta_time)

            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))
            if self.config.debug == True:
                self.debugger.draw()

            pygame.display.update()