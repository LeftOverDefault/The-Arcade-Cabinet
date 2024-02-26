from arcade.utils.imports import *


class Window:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption(config["name"])

        self.screen = pygame.display.set_mode(size=(config["resolution"][0] * config["scale_factor"], config["resolution"][1] * config["scale_factor"]))
        self.display_surface = pygame.Surface(size=self.screen.get_size())

        self.clock = pygame.time.Clock()
        self.fps = config["fps"]

        self.running = True
        self.fullscreen = config["fullscreen"]
    

    def run(self) -> None:
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.delta_time = self.clock.tick(self.fps) / 1000

            self.display_surface.fill((0, 0, 0))


            self.screen.blit(self.display_surface, (0, 0))


            pygame.display.update()