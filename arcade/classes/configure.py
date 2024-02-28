from arcade.utils.imports import *


class Configure:
    def __init__(self, config) -> None:
        print(config)
        self.config = config

        items = config.items()

        for key, value in config.items():
            setattr(self, key, value)