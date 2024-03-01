from world_engine.utils.imports import *


class Engine:
    def __init__(self) -> None:
        pygame.init()
        self.version = "0.1.0"
        pygame.display.set_caption(f"World Engine v{self.version}")
        self.on_init()

    
    def on_init(self):
        self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
        self.display_surface = pygame.Surface((198 * 1.5, 108 * 1.5))

        self.clock = pygame.time.Clock()
        self.fps = 60

        self.running = True
        self.fullscreen = False


    def render(self) -> None:
        ...


    def update(self) -> None:
        ...
    

    def events(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()



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
                            self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
                self.events(event)
            
            self.delta_time = self.clock.tick(self.fps) / 1000

            self.display_surface.fill((0, 0, 0))

            self.render()
            self.update()
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))

            pygame.display.update()