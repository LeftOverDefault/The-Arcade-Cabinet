from world_engine.utils.imports import *


class WorldEngine:
    def __init__(self, config) -> None:
        pygame.init()
        pygame.display.set_caption("World Engine v0.1.0")

        self.config = config
        self.screen = pygame.display.set_mode((198 * 6, 108 * 6))
        self.display_surface = pygame.Surface((198 * 2, 108 * 2))

        self.running = True
    

    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            self.display_surface.fill("#1B1E2B")
            
            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))

            pygame.display.update()