import framework
from framework.interface.button import Button


def video_options_menu(game):

    img = framework.imports.pygame.Surface((96, 16))
    img.fill((0, 0, 0))

    resolution_up_button = Button(img, "Resolution Up", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 0], game.video_options_menu)
    resolution_down_button = Button(img, "Resolution Down", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 20], game.video_options_menu)
    back_button = Button(img, "Back", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 40], game.video_options_menu)

    def resolution_up_button_event(event):
        game.config.screen_multiplier += 2
        game.arcade.screen = framework.imports.pygame.display.set_mode((192 * game.config.screen_multiplier, 108 * game.config.screen_multiplier))
        game.arcade.debugger.rect = game.arcade.debugger.surface.get_rect(bottomright=game.arcade.screen.get_size())
    def resolution_down_button_event(event):
        game.config.screen_multiplier -= 2
        game.arcade.screen = framework.imports.pygame.display.set_mode((192 * game.config.screen_multiplier, 108 * game.config.screen_multiplier))
        game.arcade.debugger.rect = game.arcade.debugger.surface.get_rect(bottomright=game.arcade.screen.get_size())
    def back_button_event(event):
        back_button.menu.running = False


    resolution_up_button.event = resolution_up_button_event
    resolution_down_button.event = resolution_down_button_event
    back_button.event = back_button_event