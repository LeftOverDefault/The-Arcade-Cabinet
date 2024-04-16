import framework
from framework.interface.button import Button


def audio_options_menu(game):

    img = framework.imports.pygame.Surface((96, 16))
    img.fill((0, 0, 0))

    volume_up_button = Button(img, "Volume Up", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 0], game.audio_options_menu)
    volume_down_button = Button(img, "Volume Down", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 20], game.audio_options_menu)
    back_button = Button(img, "Back", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 40], game.audio_options_menu)

    def video_options_button_event(event):
        ...
    def audio_options_button_event(event):
        ...
    def back_button_event(event):
        back_button.menu.running = False


    volume_up_button.event = video_options_button_event
    volume_down_button.event = audio_options_button_event
    back_button.event = back_button_event