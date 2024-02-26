from arcade.classes.camera import Camera
from arcade.classes.player import Player
from arcade.classes.tiles.tile import Tile
from arcade.utils.imports import *


class Window:
    def __init__(self, config) -> None:
        pygame.init()
        self.config = config
        pygame.display.set_caption(self.config["name"])
        self.screen = pygame.display.set_mode(self.config["resolution"])
        self.display_surface = pygame.Surface(self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.fps = self.config["fps"]

        self.running = True

        self.group = Camera(self.display_surface)
        self.tile = Tile((0, 0), self.group)

        self.player = Player(self.group)


    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.delta_time = self.clock.tick(self.fps) / 1000

            self.display_surface.fill((0, 180, 200))
            self.group.draw(self.player)
            self.group.update(self.delta_time)

            self.screen.blit(self.display_surface, (0, 0))

            pygame.display.update()