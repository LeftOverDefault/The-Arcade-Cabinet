from arcade.classes.configure import Configure
from arcade.classes.world import World
from arcade.debug.debugger import Debugger
from arcade.utils.imports import *


class Arcade:
    def __init__(self, config) -> None:
        self.config = Configure(config)

        pygame.init()
        pygame.display.set_caption(f"{self.config.name}")

        self.on_init()


    def on_init(self) -> None:
        self.screen = pygame.display.set_mode((198 * self.config.screen_multiplier, 108 * self.config.screen_multiplier))
        self.display_surface = pygame.Surface((198 * self.config.display_surface_multiplier, 108 * self.config.display_surface_multiplier))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.running = True
        self.fullscreen = False

        self.debugger = Debugger(self.config.font, self.config)
        self.world = World(self.display_surface, self.config)


        def debug_render() -> None:
            self.debugger.font.render(surface=self.debugger.surface, text=f"Debug Menu:", location=(10, 10 + (0 * self.debugger.font.line_height)))
            self.debugger.font.render(surface=self.debugger.surface, text=f"FPS: {round(number=self.clock.get_fps())}", location=(10, 10 + (1 * self.debugger.font.line_height)))
            self.debugger.font.render(surface=self.debugger.surface, text=f"Delta Time: {round(self.delta_time, 4)}", location=(10, 10 + (2 * self.debugger.font.line_height)))
            self.debugger.font.render(surface=self.debugger.surface, text=f"Player Pos: x = {int(self.world.player.position.x)}, y = {int(self.world.player.position.y)}", location=(10, 10 + (3 * self.debugger.font.line_height)))
            self.debugger.font.render(surface=self.debugger.surface, text=f"Player State: {self.world.player.status}", location=(10, 10 + (4 * self.debugger.font.line_height)))
            self.debugger.font.render(surface=self.debugger.surface, text=f"Tile Count: {len(self.world.camera.sprites())}", location=(10, 10 + (5 * self.debugger.font.line_height)))
        

        self.debugger.render = debug_render


    def run(self) -> None:
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
                
            self.delta_time = self.clock.tick(self.fps) / 1000
            self.display_surface.fill((0, 0, 0))

            self.world.render()
            self.world.update(self.delta_time)

            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))
            if self.config.debug == True:
                self.debugger.draw()

            pygame.display.update()