import framework
from framework.interface.button import Button


def options_menu(game):

    img = framework.imports.pygame.Surface((96, 16))
    img.fill((0, 0, 0))

    video_options_button = Button(img, "Video Options", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 0], game.options_menu)
    audio_options_button = Button(img, "Audio Options", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 20], game.options_menu)
    back_button = Button(img, "Back", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 40], game.options_menu)

    def video_options_button_event(event):
        game.video_options_menu.run()
    def audio_options_button_event(event):
        game.audio_options_menu.run()
    def back_button_event(event):
        back_button.menu.running = False


    video_options_button.event = video_options_button_event
    audio_options_button.event = audio_options_button_event
    back_button.event = back_button_event