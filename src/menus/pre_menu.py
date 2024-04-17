import framework
from framework.font.font import Font
from framework.func.json_read import json_read
from framework.func.json_write import json_write
from framework.func.tween import Easing, EasingMode, Tween


class PreMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler, settings) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)
        self.button_image = framework.imports.pygame.Surface((128 * 2, 48))
        self.button_image.fill((255, 255, 0))

        self.font = Font("assets/graphics/font/font.png", 6, (255, 255, 255))
        self.title_font = framework.imports.pygame.font.Font(framework.imports.os.path.join(".", "assets", "graphics", "font", "Copperplate.ttf"), 100)

        self.settings = settings

        self.lang = json_read(framework.imports.os.path.join(".", "src", "lang", f"{json_read(self.settings)["lang"]}.json"))

        self.create_buttons()
    

    def create_buttons(self) -> None:
        self.play_button = framework.Button(self.button_image, [self.display_surface.get_width() // 2, self.display_surface.get_height() // 2], self)


    def render(self):
        self.display_surface.fill("#070707")
        text = self.title_font.render(self.lang["menu.title"], True, (255, 255, 255))
        self.display_surface.blit(text, [self.display_surface.get_width() // 2 - (text.get_width() // 2), 128])
        self.display_surface.blit(self.play_button.image, self.play_button.rect)
    

    def update(self, delta_time: float):
        mouse_pos = [framework.imports.pygame.mouse.get_pos()[0] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"]), framework.imports.pygame.mouse.get_pos()[1] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"])]
        self.play_button.mouse_collide_point = mouse_pos

        self.play_button.update(delta_time)



    def events(self, event) -> None:
        if self.play_button.check_input(event):
            self.state_handler.update_state("main_menu")