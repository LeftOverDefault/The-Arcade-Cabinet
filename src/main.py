import framework

from src.menus.audio_options_menu import AudioOptionsMenu
from src.menus.video_options_menu import VideoOptionsMenu
from src.menus.main_menu import MainMenu
from src.menus.options_menu import OptionsMenu


class Main:
    def __init__(self) -> None:
        framework.imports.pygame.init()
        framework.imports.pygame.display.set_caption("Game")

        self.on_init()

        self.create_menus()
    

    def on_init(self) -> None:
        self.screen = framework.imports.pygame.display.set_mode((1920 // 2, 1080 // 2))
        self.display_surface = framework.imports.pygame.Surface((1920 // 2, 1080 // 2))

        self.clock = framework.imports.pygame.time.Clock()
        self.fps = 60

        self.running = True

        self.state_handler = framework.StateHandler()
    

    def create_menus(self) -> None:
        self.main_menu = MainMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler)
        self.options_menu = OptionsMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler)
        self.audio_options_menu = AudioOptionsMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler)
        self.video_options_menu = VideoOptionsMenu(self.screen, self.display_surface, self.clock, self.fps, self.state_handler)


    def run(self) -> None:
        self.state_handler.update_state("main_menu")
        while self.running == True:
            for event in framework.imports.pygame.event.get():
                if event.type == framework.imports.pygame.QUIT:
                    framework.imports.pygame.quit()
                    exit()

                if self.state_handler.current_state == "main_menu":
                    self.main_menu.events(event)
                elif self.state_handler.current_state == "options_menu":
                    self.options_menu.events(event)
                elif self.state_handler.current_state == "audio_options_menu":
                    self.audio_options_menu.events(event)
                elif self.state_handler.current_state == "video_options_menu":
                    self.video_options_menu.events(event)

            self.display_surface.fill((0, 0, 0))
            self.delta_time = self.clock.tick(self.fps) / 1000

            if self.state_handler.current_state == "main_menu":
                self.main_menu.render()
                self.main_menu.update(self.delta_time)
            elif self.state_handler.current_state == "options_menu":
                self.options_menu.render()
                self.options_menu.update(self.delta_time)
            elif self.state_handler.current_state == "video_options_menu":
                self.video_options_menu.render()
                self.video_options_menu.update(self.delta_time)
            elif self.state_handler.current_state == "audio_options_menu":
                self.audio_options_menu.render()
                self.audio_options_menu.update(self.delta_time)
            # elif self.state_handler.current_state == "main_game":
                # self.options_menu.render()
                # self.options_menu.update(self.delta_time)

            self.screen.blit(framework.imports.pygame.transform.scale(self.display_surface, self.screen.get_size()), [0, 0])

            framework.imports.pygame.display.update()