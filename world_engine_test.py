import world_engine
from world_engine.classes.camera import Camera


class Main:
    def __init__(self) -> None:
        self.engine = world_engine.Engine()

        self.engine.render = self.render
        self.engine.update = self.update

        self.camera = Camera(self.engine.display_surface)


    def render(self):
        self.camera.draw()


    def update(self):
        self.camera.update(self.engine.delta_time)

    
    def run(self):
        self.engine.run()


if __name__ == "__main__":
    main = Main()
    main.run()