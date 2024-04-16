from framework.utils.imports import *


class StateHandler:
    def __init__(self) -> None:
        self.current_state = ""
    

    def update_state(self, new_state) -> None:
        self.current_state = new_state