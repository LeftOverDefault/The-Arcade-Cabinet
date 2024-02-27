from arcade.classes.configure import Configure
from arcade.debug.debugger import Debugger
from arcade.utils.imports import *


class Window:
    def __init__(self, config) -> None:
        self.config = Configure(config=config)

        pygame.init()
        pygame.display.set_caption(f"{self.config.name} v{self.config.version}")

        self.on_init()
    
    def on_init(self):
        self.screen = pygame.display.set_mode((192 * 4, 108 * 4))
        self.display_surface = pygame.Surface((192, 108))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.debugger = Debugger(self.config)


    def render(self):
        ...


    def update(self):
        ...


    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()

            self.delta_time = self.clock.tick(self.fps) / 1000

            self.render()
            self.update()

            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))
            self.debugger.draw(self.clock)

            pygame.display.update()