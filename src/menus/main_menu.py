import framework
from framework.func.fade_in import fade_in
from framework.func.fade_out import fade_out
from framework.interface.button import Button
from framework.interface.menu import Menu



class MainMenu(Menu):
    def __init__(self, screen, display_surface, config) -> None:
        super().__init__(screen, display_surface, config)
        img = framework.imports.pygame.Surface((96, 16))
        img.fill((100, 100, 100))

        self.play_button = Button(img, "Play", [self.display_surface.get_width() // 2, self.display_surface.get_height()], self)
        self.options_button = Button(img, "Options", [self.display_surface.get_width() // 2, (self.display_surface.get_height() // 2) + 20], self)
        self.quit_button = Button(img, "Quit", [self.display_surface.get_width() // 2, (self.display_surface.get_height() // 2) + 40], self)



    
    def create_button_events(self, game) -> None:
        # fade_surf = framework.imports.pygame.Surface(framework.imports.pygame.display.get_surface().get_size())
        # fade_surf.fill((0, 0, 0))
        def play_button_event(event):
            # fade_out(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.main_menu.render)
            # fade_in(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.arcade.render)
            game.arcade.run()
        def options_button_event(event):
            # fade_out(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.main_menu.render)
            # fade_in(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.options_menu.render)
            game.options_menu.run()
        def quit_button_event(event):
            framework.imports.pygame.quit()
            exit()

        self.play_button.event = play_button_event
        self.options_button.event = options_button_event
        self.quit_button.event = quit_button_event

        self.play_button_rect_y_counter = self.display_surface.get_height()

    def render(self):
        super().render()
    

    def update(self):
        if self.play_button.rect.centery >= (self.display_surface.get_height() // 2):
            self.play_button.rect.centery = int(self.play_button_rect_y_counter)
            self.play_button.text_rect.centery = int(self.play_button_rect_y_counter)
            self.play_button_rect_y_counter -= 0.05


def main_menu(game):
    game.main_menu = MainMenu(game.arcade.screen, game.arcade.display_surface, game.config)
    game.main_menu.create_button_events(game)