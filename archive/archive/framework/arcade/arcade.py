from framework.arcade.classes.configure import Configure
from framework.arcade.classes.particle_system import ParticleSystem
from framework.arcade.debug.debugger import Debugger
from framework.arcade.func.fade_in import fade_in
from framework.arcade.func.fade_out import fade_out
from framework.arcade.utils.imports import *


class Arcade:
    def __init__(self, config) -> None:
        self.config = Configure(config)

        pygame.init()
        pygame.display.set_caption(f"{self.config.name}")

        self.on_init()


    def on_init(self) -> None:
        self.screen = pygame.display.set_mode((192 * self.config.screen_multiplier, 108 * self.config.screen_multiplier))
        self.display_surface = pygame.Surface((192 * self.config.display_surface_multiplier, 108 * self.config.display_surface_multiplier))

        self.clock = pygame.time.Clock()
        self.fps = 60
        self.delta_time = self.clock.tick(self.fps) / 1000

        self.running = True
        self.fullscreen = False

        self.debugger = Debugger(self.config.font, self.config)

        self.particle_system = ParticleSystem(self.display_surface, self.config)

        self.fade_surf = pygame.Surface(pygame.display.get_surface().get_size())
        self.fade_surf.fill((0, 0, 0))

        print(f"arcade 0.1.0 (Python {platform.python_version()})")


    def render(self) -> None:
        ...


    def update(self, delta_time) -> None:
        ...


    def events(self, event):
        ...


    def run(self) -> None:
        fade_in(int(time_converter(0.0025, "milliseconds")), self.fade_surf, self.display_surface, self.screen, self.render)
        self.running = True
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
        fade_out(int(time_converter(0.0025, "milliseconds")), self.fade_surf, self.display_surface, self.screen, self.render)
        