import framework
from framework.font.font import Font
from framework.func.json_read import json_read
from framework.func.json_write import json_write
from framework.func.tween import Easing, EasingMode, Tween


class MainMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler, settings) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)
        self.button_image = framework.imports.pygame.Surface((128 * 2, 48))
        self.button_image.fill((255, 255, 0))

        self.font = Font("assets/graphics/font/font.png", 6, (255, 255, 255))

        self.settings = settings

        self.lang = json_read(framework.imports.os.path.join(".", "src", "lang", f"{json_read(self.settings)["lang"]}.json"))

        self.create_buttons()
    

    def create_buttons(self) -> None:
        self.play_button = framework.Button(self.button_image, [self.display_surface.get_width() // 2, self.display_surface.get_height() + (1 * 128)], self)
        self.options_button = framework.Button(self.button_image, [self.display_surface.get_width() // 2, self.display_surface.get_height() + (2 * 128)], self)
        self.quit_button = framework.Button(self.button_image, [self.display_surface.get_width() // 2, self.display_surface.get_height() + (3 * 128)], self)
    
        self.play_button_anim = Tween(begin=self.display_surface.get_height() + (1 * 128), end=self.display_surface.get_height() // 2, duration=2000, easing=Easing.BOUNCE, easing_mode=EasingMode.OUT, boomerang=False,  loop=False)
        self.options_button_anim = Tween(begin=self.display_surface.get_height() + (2 * 128), end=self.display_surface.get_height() // 2 + 64, duration=2500, easing=Easing.QUAD, easing_mode=EasingMode.IN_OUT, boomerang=False,  loop=False)
        self.quit_button_anim = Tween(begin=self.display_surface.get_height() + (3 * 128), end=self.display_surface.get_height() // 2 + 128, duration=3000, easing=Easing.QUAD, easing_mode=EasingMode.IN_OUT, boomerang=False,  loop=False)
        
        self.play_button_anim.start()
        self.options_button_anim.start()
        self.quit_button_anim.start()


    def render(self):
        self.display_surface.blit(self.play_button.image, self.play_button.rect)
        self.display_surface.blit(self.options_button.image, self.options_button.rect)
        self.display_surface.blit(self.quit_button.image, self.quit_button.rect)
        self.font.render(self.display_surface, self.lang["menu.title"], [self.display_surface.get_width() // 2, self.display_surface.get_height() // 4])
    

    def update(self, delta_time: float):
        mouse_pos = [framework.imports.pygame.mouse.get_pos()[0] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"]), framework.imports.pygame.mouse.get_pos()[1] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"])]
        self.play_button.mouse_collide_point = mouse_pos
        self.options_button.mouse_collide_point = mouse_pos
        self.quit_button.mouse_collide_point = mouse_pos

        self.play_button_anim.update()
        self.options_button_anim.update()
        self.quit_button_anim.update()

        self.play_button.rect.y = self.play_button_anim.value
        self.options_button.rect.y = self.options_button_anim.value
        self.quit_button.rect.y = self.quit_button_anim.value

        self.play_button.update(delta_time)
        self.options_button.update(delta_time)
        self.quit_button.update(delta_time)



    def events(self, event) -> None:
        if self.play_button.check_input(event):
            self.state_handler.update_state("main_game")
        elif self.options_button.check_input(event):
            self.state_handler.update_state("options_menu")
        elif self.quit_button.check_input(event):
            framework.imports.pygame.quit()
            exit()