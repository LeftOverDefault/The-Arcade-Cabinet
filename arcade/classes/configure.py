from arcade.utils.imports import *


class Configure:
    def __init__(self, config) -> None:
        self.config = config

        for key, value in config.items():
            setattr(self, key, value)