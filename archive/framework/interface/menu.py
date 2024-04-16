from framework.func.fade_in import fade_in
from framework.func.fade_out import fade_out
from framework.utils.imports import *


class Menu:
    def __init__(self, screen, display_surface, config) -> None:
        self.screen = screen
        self.display_surface = display_surface
        self.config = config

        self.buttons = []

        self.running = False

        self.mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)

        self.background_color = (0, 0, 0)

        self.fade_surf = pygame.Surface(pygame.display.get_surface().get_size())
        self.fade_surf.fill((0, 0, 0))


    def update_mouse_rect(self) -> None:
        self.mouse_rect.x = pygame.mouse.get_pos()[0] // (self.config.screen_multiplier // self.config.display_surface_multiplier)
        self.mouse_rect.y = pygame.mouse.get_pos()[1] // (self.config.screen_multiplier // self.config.display_surface_multiplier)


    def draw_buttons(self) -> None:
        for button in self.buttons:
            button.draw()


    def render(self) -> None:
        self.display_surface.fill(self.background_color)
        self.draw_buttons()


    def update(self) -> None:
        for button in self.buttons:
            button.update()


    def events(self, event) -> None:
        for button in self.buttons:
            if button.check_input(event):
                button.event(event)


    def run(self) -> None:
        self.running = True
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.events(event)


            self.update_mouse_rect()

            self.render()
            self.update()

            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))

            pygame.display.update()