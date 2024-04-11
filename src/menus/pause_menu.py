import framework
from framework.interface.button import Button


def pause_menu(game):

    img = framework.imports.pygame.Surface((96, 16))
    img.fill((0, 0, 0))

    resume_button = Button(img, "Resume", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 0], game.pause_menu)
    options_button = Button(img, "Options", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 20], game.pause_menu)
    exit_button = Button(img, "Exit To Menu", [game.arcade.display_surface.get_width() // 2, (game.arcade.display_surface.get_height() // 2) + 40], game.pause_menu)

    def resume_button_event(event):
        resume_button.menu.running = False
        game.arcade.run()
    def options_button_event(event):
        game.options_menu.running = False
        game.options_menu.run()
    def exit_button_event(event):
        game.main_menu.running = False
        game.main_menu.run()

    resume_button.event = resume_button_event
    options_button.event = options_button_event
    exit_button.event = exit_button_event