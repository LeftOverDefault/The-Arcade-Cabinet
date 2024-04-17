import framework
from framework.func.json_read import json_read
from framework.func.json_write import json_write


class VideoOptionsMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler, settings) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)
        self.button_image = framework.imports.pygame.Surface((128, 48))
        self.button_image.fill((0, 255, 255))

        self.res_up_button = framework.Button(self.button_image, [100, 100], self)
        self.res_down_button = framework.Button(self.button_image, [100, 164], self)
        self.back_button = framework.Button(self.button_image, [100, 228], self)
        
        self.settings = settings


    def render(self):
        self.display_surface.blit(self.res_up_button.image, self.res_up_button.rect)
        self.display_surface.blit(self.res_down_button.image, self.res_down_button.rect)
        self.display_surface.blit(self.back_button.image, self.back_button.rect)


    def update(self, delta_time: float):
        mouse_pos = [framework.imports.pygame.mouse.get_pos()[0] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"]), framework.imports.pygame.mouse.get_pos()[1] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"])]

        self.res_up_button.mouse_collide_point = mouse_pos
        self.res_down_button.mouse_collide_point = mouse_pos
        self.back_button.mouse_collide_point = mouse_pos

        self.res_up_button.update(delta_time)
        self.res_down_button.update(delta_time)
        self.back_button.update(delta_time)
    

    def events(self, event: framework.imports.pygame.event) -> None:
        if self.res_up_button.check_input(event):
            if json_read(self.settings)["current_screen_multiplier"] + 1 <= 13:
                json_write(self.settings, "current_screen_multiplier", json_read(self.settings)["current_screen_multiplier"] + 1)
                self.screen = framework.imports.pygame.display.set_mode((192 * json_read(self.settings)["current_screen_multiplier"], 108 * json_read(self.settings)["current_screen_multiplier"]))
        elif self.res_down_button.check_input(event):
            if json_read(self.settings)["current_screen_multiplier"] - 1 > 0:
                json_write(self.settings, "current_screen_multiplier", json_read(self.settings)["current_screen_multiplier"] - 1)
                self.screen = framework.imports.pygame.display.set_mode((192 * json_read(self.settings)["current_screen_multiplier"], 108 * json_read(self.settings)["current_screen_multiplier"]))
        if self.back_button.check_input(event):
            self.state_handler.update_state("options_menu")