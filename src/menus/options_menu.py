import framework
from framework.func.fade_in import fade_in
from framework.func.fade_out import fade_out
from framework.interface.button import Button


def options_menu(game):

    img = framework.imports.pygame.Surface((96, 16))
    img.fill((0, 0, 0))

    fade_surf = framework.imports.pygame.Surface(framework.imports.pygame.display.get_surface().get_size())
    fade_surf.fill((0, 0, 0))

    video_options_button = Button(img, "Video Options", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 0], game.options_menu)
    audio_options_button = Button(img, "Audio Options", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 20], game.options_menu)
    back_button = Button(img, "Back", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 40], game.options_menu)

    def video_options_button_event(event):
        fade_out(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.options_menu.render)
        fade_in(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.video_options_menu.render)
        game.video_options_menu.run()
    def audio_options_button_event(event):
        fade_out(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.options_menu.render)
        fade_in(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.audio_options_menu.render)
        game.audio_options_menu.run()
    def back_button_event(event):
        fade_out(int(2.5), fade_surf, game.arcade.display_surface, game.arcade.screen, game.options_menu.render)
        back_button.menu.running = False


    video_options_button.event = video_options_button_event
    audio_options_button.event = audio_options_button_event
    back_button.event = back_button_event