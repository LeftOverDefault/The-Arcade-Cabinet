import framework


class AudioOptionsMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)
        self.button_image = framework.imports.pygame.Surface((128, 48))
        self.button_image.fill((255, 0, 0))

        # self.video_options_button = framework.Button(self.button_image, [100, 100], self)
        # self.audio_options_button = framework.Button(self.button_image, [100, 164], self)
        self.back_button = framework.Button(self.button_image, [100, 228], self)


    def render(self):
        for button in self.buttons:
            self.display_surface.blit(button.image, button.rect)


    def update(self, delta_time: float):
        for button in self.buttons:
            button.update(delta_time)


    def events(self, event: framework.imports.pygame.Event) -> None:
        # if self.video_options_button.check_input(event):
        #     self.state_handler.update_state("video_options_menu")
        # elif self.audio_options_button.check_input(event):
        #     self.state_handler.update_state("audio_options_menu")
        if self.back_button.check_input(event):
            self.state_handler.update_state("options_menu")