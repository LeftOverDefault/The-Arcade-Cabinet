from framework.utils.imports import *


class Configure:
    def __init__(self, config) -> None:
        self.config = config

        for key, value in self.config.items():
            setattr(self, key, value)
    

    def update_value(self, key, value):
        setattr(self, key, value)

