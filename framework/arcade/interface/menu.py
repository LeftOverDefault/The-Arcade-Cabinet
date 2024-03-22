from framework.arcade.utils.imports import *


class Menu:
    def __init__(self, display_surface, debugger, config) -> None:
        self.config = config
        self.screen = pygame.display.get_surface()
        self.display_surface = display_surface
        self.debugger = debugger

        self.buttons = []

        self.running = False
        self.bg_color = (100, 100, 100, 50)

        self.mouse_rect = pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 1, 1)


    def update_mouse_rect(self):
        self.mouse_rect.x = pygame.mouse.get_pos()[0] // (self.config.screen_multiplier // self.config.display_surface_multiplier)
        self.mouse_rect.y = pygame.mouse.get_pos()[1] // (self.config.screen_multiplier // self.config.display_surface_multiplier)
    

    def render_debugger(self):
        self.debugger.debug_info.clear()

        self.debugger.debug_info.append(f"Debug Menu:")


    def draw(self) -> None:
        for button in self.buttons:
            button.on_hover(self.mouse_rect)
            button.on_click(self.mouse_rect)

            if self.buttons[0].clicked == True:
                self.running = False

            button.draw()


    def events(self, event) -> None:
        ...


    def run(self) -> None:
        self.running = True
        while self.running == True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                self.events(event)

            self.display_surface.fill(self.bg_color)

            self.update_mouse_rect()

            self.draw()

            self.screen.blit(pygame.transform.scale(self.display_surface, self.screen.get_size()), (0, 0))
            if self.config.debug == True:
                self.render_debugger()
                self.debugger.draw()

            pygame.display.update()