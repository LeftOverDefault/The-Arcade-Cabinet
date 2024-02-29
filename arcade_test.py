import pygame
import arcade
from arcade.classes.camera import Camera
from arcade.classes.layer import Layer
from arcade.classes.player import Player
from arcade.debug.debugger import Debugger
from arcade.func.generate_chunk import generate_chunk


chunks = {
    "0;0": {
        # "0;0": -1, "1;0": -1, "2;0": -1, "3;0": -1, "4;0": -1, "5;0": -1, "6;0": -1, "7;0": -1,
        # "0;1": -1, "1;1": -1, "2;1": -1, "3;1": -1, "4;1": -1, "5;1": -1, "6;1": -1, "7;1": -1,
        # "0;2": -1, "1;2": -1, "2;2": -1, "3;2": -1, "4;2": -1, "5;2": -1, "6;2": -1, "7;2": -1,
        # "0;3": -1, "1;3": -1, "2;3": -1, "3;3": -1, "4;3": -1, "5;3": -1, "6;3": -1, "7;3": -1,
        # "0;4": -1, "1;4": -1, "2;4": -1, "3;4": -1, "4;4": -1, "5;4": -1, "6;4": -1, "7;4": -1,
        # "0;5": -1, "1;5": -1, "2;5": -1, "3;5": -1, "4;5": -1, "5;5": -1, "6;5": -1, "7;5": -1,
        # "0;6": -1, "1;6": -1, "2;6": -1, "3;6": -1, "4;6": -1, "5;6": -1, "6;6": -1, "7;6": -1,
        # "0;7": 0, "1;7": 0, "2;7": 0, "3;7": 0, "4;7": 0, "5;7": 0, "6;7": 0, "7;7": 0,
    },
    "1;0": {},
    "2;0": {},
    "3;0": {},
    "4;0": {},
    "0;1": {},
    "1;1": {},
    "2;1": {},
    "3;1": {},
    "4;1": {},
    "0;2": {},
    "1;2": {},
    "2;2": {},
    "3;2": {},
    "4;2": {},
    "0;3": {},
    "1;3": {},
    "2;3": {},
    "3;3": {},
    "4;3": {},
}

# config = {
#     "name": "Arcade Test",
#     "version": "0.1.0",
#     "resolution": [int(192 * 1.25), int(108 * 1.25)],
#     "scale_factor": 5,
#     "tile_size": 16,
#     "chunk_size": 8,
#     "camera_delay": 25,
#     "fps": 60,
#     "fullscreen": False,
#     "worlds": [
#         world
#     ]
# }

config = {
    "name": "Arcade Test",
    "version": "0.1.0",
    "scale_factor": 2,
    "tile_size": 16,
    "chunk_size": 8,
    "debug": True,
}


def render_chunk(config, chunk_coordinates, chunk_x_offset, chunk_y_offset):
    tiles = []
    for coordinate in chunk_coordinates:
        tile_x = (coordinate[0] * config.tile_size) + chunk_x_offset
        tile_y = (coordinate[1] * config.tile_size) + chunk_y_offset

        tiles.append([tile_x, tile_y])

    return tiles



class Main:
    def __init__(self) -> None:
        self.window = arcade.Window(config=config)
        self.debugger = Debugger(font_path="./assets/font/font.png", config=self.window.config)

        self.camera = Camera(display_surface=self.window.display_surface)
        self.player = Player(initial_position=(288 / 2, 162 / 2), path="./assets/sprite/entity/player/", group=self.camera, config=self.window.config)

        self.window.render = self.render
        self.window.update = self.update
        self.window.event = self.event
        self.debugger.render = self.debug_render

        self.camera.camera_delay = 25

        self.test_tile = pygame.image.load("./assets/sprite/environment/tile.png").convert_alpha()

        self.tile_count = len(chunks) * self.window.config.chunk_size ** 2

        # pygame.mouse.set_visible(False)
        # self.mouse_pos = pygame.Vector2()
        # self.mouse_img = pygame.transform.scale_by(pygame.image.load("./assets/sprite/mouse.png").convert_alpha(), 2)


    def render(self) -> None:
        self.window.display_surface.fill((255, 255, 255))

        for chunk_location in chunks:
            chunk_x = int(chunk_location.split(";")[0])
            chunk_y = int(chunk_location.split(";")[1])
            chunk_coordinated = generate_chunk(config=self.window.config, x=chunk_x, y=chunk_y)
            tiles = render_chunk(config=self.window.config, chunk_coordinates=chunk_coordinated, chunk_x_offset=round(chunk_x / self.window.config.chunk_size) - self.camera.offset.x, chunk_y_offset=round(chunk_y / self.window.config.chunk_size) - self.camera.offset.y)

            chunk_x *= self.window.config.chunk_size * self.window.config.tile_size
            chunk_y *= self.window.config.chunk_size * self.window.config.tile_size

            camera_left = self.camera.offset.x
            camera_right = self.camera.offset.x + self.camera.display_surface.get_width()
            camera_top = self.camera.offset.y
            camera_bottom = self.camera.offset.y + self.camera.display_surface.get_height()

            in_left = camera_left <= (chunk_x) + (self.window.config.chunk_size * self.window.config.tile_size)
            in_right = camera_right >= chunk_x
            in_top = camera_top <= (chunk_y) + (self.window.config.chunk_size * self.window.config.tile_size)
            in_bottom = camera_bottom >= chunk_y

            if in_left and in_right:
                if in_top and in_bottom:
                    for tile in tiles:
                        self.window.display_surface.blit(source=self.test_tile.copy(), dest=tile)

        self.camera.draw(player=self.player)
        self.window.screen.blit(source=arcade.pygame.transform.scale(surface=self.window.display_surface, size=self.window.screen.get_size()), dest=(0, 0))
        self.debugger.draw()
        # self.window.screen.blit(self.mouse_img, self.mouse_pos)


    def debug_render(self) -> None:
        self.debugger.font.render(surface=self.debugger.surface, text=f"Debug Menu:", location=(10, 10 + (0 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"FPS: {round(number=self.window.clock.get_fps())}", location=(10, 10 + (1 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Delta Time: {round(self.window.delta_time, 4)}", location=(10, 10 + (2 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Player Pos: x = {int(self.player.position.x)}, y = {int(self.player.position.y)}", location=(10, 10 + (3 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Player State: {self.player.status}", location=(10, 10 + (4 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Tile Count: {self.tile_count}", location=(10, 10 + (5 * self.debugger.font.line_height)))


    def update(self):
        self.camera.update(delta_time=self.window.delta_time)
        self.mouse_pos = pygame.mouse.get_pos()

        pygame.event.set_grab(False)


    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                exit()


    def run(self):
        self.window.run()


if __name__ == "__main__":
    main = Main()
    main.run()