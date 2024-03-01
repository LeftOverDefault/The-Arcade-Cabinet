from arcade.classes.configure import Configure
from arcade.classes.tile.tile import Tile
from world_engine.classes.camera import Camera
import world_engine


class Main:
    def __init__(self) -> None:
        self.engine = world_engine.Engine()

        self.engine.render = self.render
        self.engine.update = self.update

        self.camera = Camera(self.engine.display_surface)
        self.tile = Tile((0, 0), self.camera, Configure({"tile_size": 16}))
        self.tile.image.fill((255, 255, 255))

    
    def render(self):
        self.camera.draw()


    def update(self):
        self.camera.update(self.engine.delta_time)

    
    def run(self):
        self.engine.run()


if __name__ == "__main__":
    main = Main()
    main.run()