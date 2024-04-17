import framework
from framework.func.json_read import json_read


class AudioOptionsMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler, settings) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)
        self.button_image = framework.imports.pygame.Surface((128, 48))
        self.button_image.fill((255, 0, 0))

        # self.video_options_button = framework.Button(self.button_image, [100, 100], self)
        # self.audio_options_button = framework.Button(self.button_image, [100, 164], self)
        self.back_button = framework.Button(self.button_image, [100, 228], self)

        self.settings = settings


    def render(self):
        for button in self.buttons:
            self.display_surface.blit(button.image, button.rect)


    def update(self, delta_time: float):

        mouse_pos = [framework.imports.pygame.mouse.get_pos()[0] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"]), framework.imports.pygame.mouse.get_pos()[1] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"])]
        # self.play_button.mouse_collide_point = mouse_pos
        # self.options_button.mouse_collide_point = mouse_pos
        self.back_button.mouse_collide_point = mouse_pos


        for button in self.buttons:
            button.update(delta_time)


    def events(self, event: framework.imports.pygame.event) -> None:
        # if self.video_options_button.check_input(event):
        #     self.state_handler.update_state("video_options_menu")
        # elif self.audio_options_button.check_input(event):
        #     self.state_handler.update_state("audio_options_menu")
        if self.back_button.check_input(event):
            self.state_handler.update_state("options_menu")