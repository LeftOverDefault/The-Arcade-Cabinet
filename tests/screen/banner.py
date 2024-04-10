from framework.arcade import interface
from framework.arcade.func.fade_in import fade_in
from framework.arcade.func.fade_out import fade_out
from framework.arcade.utils.imports import *


class Banner:
    def __init__(self, screen) -> None:
        self.screen = screen

        self.background = pygame.image.load("./assets/banner.png")
        self.background_rect = self.background.get_rect(center=((screen.get_width() // 2) - (self.background.get_width() // 2), (screen.get_height() // 2) - (self.background.get_height() // 2)))

        self.fade_surf = pygame.Surface(pygame.display.get_surface().get_size())
        self.fade_surf.fill((0, 0, 0))


    def render(self) -> None:
        self.screen.blit(self.background, self.background_rect.center)


    def run(self) -> None:
        fade_in(int(time_converter(0.0025, "milliseconds")), self.fade_surf, self.screen, self.screen, self.render)
        self.running = True
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.events(event)

            self.render()

            pygame.display.update()

            pygame.time.delay(time_converter(1, "milliseconds"))

            self.running = False
        fade_out(int(time_converter(0.0025, "milliseconds")), self.fade_surf, self.screen, self.screen, self.render)