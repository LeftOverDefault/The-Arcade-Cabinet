import framework
from framework.func.fade_in import fade_in
from framework.func.fade_out import fade_out
from framework.interface.button import Button


def main_menu(game):

    img = framework.imports.pygame.Surface((96, 16))
    img.fill((0, 0, 0))

    fade_surf = framework.imports.pygame.Surface(framework.imports.pygame.display.get_surface().get_size())
    fade_surf.fill((0, 0, 0))

    play_button = Button(img, "Play", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 0], game.main_menu)
    options_button = Button(img, "Options", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 20], game.main_menu)
    quit_button = Button(img, "Quit", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 40], game.main_menu)

    def play_button_event(event):
        fade_out(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.main_menu.render)
        game.arcade.run()
    def options_button_event(event):
        game.options_menu.run()
    def quit_button_event(event):
        framework.imports.pygame.quit()
        exit()

    play_button.event = play_button_event
    options_button.event = options_button_event
    quit_button.event = quit_button_event