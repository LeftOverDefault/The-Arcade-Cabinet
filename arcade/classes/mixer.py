from arcade.utils.imports import *


class Mixer:
    def __init__(self) -> None:
        self.mixer = pygame.mixer()


    def play_music(self, audio):
        self.mixer.music.play(audio)


    def stop(self):
        self.mixer.music.fadeout(2)