import framework


class MainMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)
        self.button_image = framework.imports.pygame.Surface((128, 48))
        self.button_image.fill((255, 255, 0))

        self.play_button = framework.Button(self.button_image, [self.display_surface.get_width() // 2, self.display_surface.get_height() // 2], self)
        self.options_button = framework.Button(self.button_image, [100, 164], self)
        self.quit_button = framework.Button(self.button_image, [100, 228], self)
    

    def render(self):
        for button in self.buttons:
            self.display_surface.blit(button.image, button.rect)
    

    def update(self, delta_time: float):
        for button in self.buttons:
            button.update(delta_time)
    

    def events(self, event: framework.imports.pygame.event) -> None:
        if self.play_button.check_input(event):
            self.state_handler.update_state("main_game")
        elif self.options_button.check_input(event):
            self.state_handler.update_state("options_menu")
        elif self.quit_button.check_input(event):
            framework.imports.pygame.quit()
            exit()