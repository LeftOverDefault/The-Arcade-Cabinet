import framework
from framework.font.font import Font
from framework.func.json_read import json_read
from framework.func.json_write import json_write
from framework.func.tween import Easing, EasingMode, Tween


class PreMenu(framework.Menu):
    def __init__(self, screen, display_surface, clock, fps, state_handler, settings) -> None:
        super().__init__(screen, display_surface, clock, fps, state_handler)

        self.bg = framework.imports.pygame.image.load(framework.imports.os.path.join(".", "assets", "graphics", "ui", "menu.png")).convert_alpha()

        self.button_image = framework.imports.pygame.Surface((128 * 2, 48))
        self.button_image.fill((255, 255, 0))

        self.font = Font("assets/graphics/font/font.png", 6, (255, 255, 255))
        self.title_font = framework.imports.pygame.font.Font(framework.imports.os.path.join(".", "assets", "graphics", "font", "Copperplate.ttf"), 100)

        self.settings = settings

        self.lang = json_read(framework.imports.os.path.join(".", "src", "lang", f"{json_read(self.settings)["lang"]}.json"))

        self.create_buttons()


    def create_buttons(self) -> None:
        self.play_button = framework.Button(self.button_image, [self.display_surface.get_width() // 2, self.display_surface.get_height() // 2], self)

        self.bar_buttons = []
        self.bars = {}
        self.animations_1 = []
        self.animations_2 = []
        self.animations_in_out = {}

        for i in range(0, 32):
            surface = framework.imports.pygame.Surface((10, 50))
            surface.fill((255, 255, 255))


            self.bar_buttons.append(framework.Button(surface, [((self.display_surface.get_width() // 2) - (7 * 32)) + (i * 14), self.display_surface.get_height() * (3 / 4)], self))

            self.bars[framework.imports.pygame.Surface((14, 2))] = framework.imports.pygame.Surface((14, 2)).get_rect(topleft=(self.bar_buttons[i].rect.topleft[0] - 2, self.bar_buttons[i].rect.topleft[1] - 7))
            
            self.animations_1.append(Tween(self.bar_buttons[0].rect.topleft[1] - 7, self.bar_buttons[0].rect.topleft[1] - 64, 2000, Easing.QUAD, EasingMode.OUT, False, False))
            self.animations_2.append(Tween(self.bar_buttons[0].rect.topleft[1] - 64, self.bar_buttons[0].rect.topleft[1] - 7, 2000, Easing.QUAD, EasingMode.IN_OUT, False, False))
            self.animations_in_out[i] = "in"

        for bar, bar_rect in self.bars.items():
            bar.fill((255, 0, 0))


    def render(self):
        self.display_surface.fill("#070707")
        self.display_surface.blit(framework.imports.pygame.transform.scale(self.bg, self.display_surface.get_size()), [0, 0])
        # text = self.title_font.render(self.lang["menu.title"], True, (255, 255, 255))
        # self.display_surface.blit(text, [self.display_surface.get_width() // 2 - (text.get_width() // 2), 128])
        self.display_surface.blit(self.play_button.image, self.play_button.rect)
        for button in self.bar_buttons:
            self.display_surface.blit(button.image, button.rect)
        for bar, bar_rect in self.bars.items():
            self.display_surface.blit(bar, bar_rect)


    def update(self, delta_time: float):
        mouse_pos = [framework.imports.pygame.mouse.get_pos()[0] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"]), framework.imports.pygame.mouse.get_pos()[1] // (json_read(self.settings)["current_screen_multiplier"] / json_read(self.settings)["display_surface_multiplier"])]
        self.play_button.mouse_collide_point = mouse_pos

        for button in self.bar_buttons:
            button.mouse_collide_point = mouse_pos
            button.update(delta_time)

        for animation in self.animations_1:
            animation.update()
        for animation in self.animations_2:
            animation.update()

        for index, bar_rect in enumerate(self.bars.values()):
            if int(self.animations_1[index].value) == self.bar_buttons[0].rect.topleft[1] - 64:
                self.animations_1[index]._value = self.bar_buttons[0].rect.topleft[1]
                self.animations_in_out[index] = "out"
                self.animations_2[index].start()
            elif int(self.animations_2[index].value) == self.bar_buttons[0].rect.topleft[1]:
                self.animations_2[index]._value = self.bar_buttons[0].rect.topleft[1] - 64
                self.animations_in_out[index] = "in"

            if self.animations_in_out[index] == "in":
                bar_rect.y = self.animations_1[index].value
            else:
                bar_rect.y = self.animations_2[index].value

        self.play_button.update(delta_time)


    def events(self, event) -> None:
        if self.play_button.check_input(event):
            self.state_handler.update_state("main_menu")
        for button_index, button in enumerate(self.bar_buttons):
            if button.hover(event) == True:
                self.animations_in_out[button_index] = "in"
                self.animations_1[button_index].start()