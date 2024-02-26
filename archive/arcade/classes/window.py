from arcade.classes.camera.top_down_camera import Camera
from arcade.classes.player.top_down_player import Player
from arcade.utils.imports import *


class Window:
    def __init__(self, config) -> None:
        pygame.init()
        self.config = config
        pygame.display.set_caption(self.config["name"] + f" v{self.config["version"]}")
        self.screen = pygame.display.set_mode(size=[self.config["resolution"][0] * self.config["scale_factor"], self.config["resolution"][1] * self.config["scale_factor"]])
        self.display_surface = pygame.Surface(size=self.screen.get_size())
        self.clock = pygame.time.Clock()
        self.fps = self.config["fps"]

        self.running = True

        self.camera = Camera(display_surface=self.display_surface)
        self.player = Player(group=self.camera)
    

    def render(self):
        self.display_surface.fill(color=(0, 180, 200))

        self.camera.draw(player=self.player)

        self.screen.blit(source=pygame.transform.scale(surface=self.display_surface, size=self.screen.get_size()), dest=(0, 0))
    

    def update(self):
        self.delta_time = self.clock.tick(self.fps) / 1000

        self.camera.update(self.delta_time)

        pygame.display.update()


    def run(self):
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            
            self.render()
            self.update()