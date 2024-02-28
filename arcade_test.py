import pygame
import arcade
from arcade.classes.camera import Camera
from arcade.classes.layer import Layer
from arcade.classes.player import Player
from arcade.classes.tile.tile import Tile
from arcade.debug.debugger import Debugger
from arcade.func.generate_chunk import generate_chunk


# world = {
#     "0;0": {
#         "0;0": -1, "1;0": -1, "2;0": -1, "3;0": -1, "4;0": -1, "5;0": -1, "6;0": -1, "7;0": -1,
#         # "0;1": -1, "1;1": -1, "2;1": -1, "3;1": -1, "4;1": -1, "5;1": -1, "6;1": -1, "7;1": -1,
#         # "0;2": -1, "1;2": -1, "2;2": -1, "3;2": -1, "4;2": -1, "5;2": -1, "6;2": -1, "7;2": -1,
#         # "0;3": -1, "1;3": -1, "2;3": -1, "3;3": -1, "4;3": -1, "5;3": -1, "6;3": -1, "7;3": -1,
#         # "0;4": -1, "1;4": -1, "2;4": -1, "3;4": -1, "4;4": -1, "5;4": -1, "6;4": -1, "7;4": -1,
#         # "0;5": -1, "1;5": -1, "2;5": -1, "3;5": -1, "4;5": -1, "5;5": -1, "6;5": -1, "7;5": -1,
#         # "0;6": -1, "1;6": -1, "2;6": -1, "3;6": -1, "4;6": -1, "5;6": -1, "6;6": -1, "7;6": -1,
#         # "0;7": 0, "1;7": 0, "2;7": 0, "3;7": 0, "4;7": 0, "5;7": 0, "6;7": 0, "7;7": 0,
#     }
# }

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


def render_chunk(config, display_surface: pygame.Surface, chunk, camera, chunk_x_offset, chunk_y_offset):
    tiles = []
    for location in chunk:
        x = location[0]
        y = location[1]
        sprite = pygame.sprite.Sprite()
        sprite.image = pygame.Surface((config.tile_size, config.tile_size))
        sprite.image.fill((0, 255, 255))
        sprite.rect = sprite.image.get_rect(topleft=(x * config.tile_size + chunk_x_offset, y * config.tile_size + chunk_y_offset, config.tile_size, config.tile_size))
        tiles.append(sprite)
    return tiles



class Main:
    def __init__(self) -> None:
        self.layer_1 = Layer(y_sorted=True, collidable=False)
        self.window = arcade.Window(config=config)
        self.debugger = Debugger(font_path="./assets/font/font.png", config=self.window.config)

        self.camera = Camera(display_surface=self.window.display_surface)
        self.player = Player(initial_position=(-12, -12), path="./assets/sprite/entity/player/", group=self.layer_1, config=self.window.config)

        self.window.render = self.render
        self.window.update = self.update
        self.window.event = self.event
        self.debugger.render = self.debug_render

        self.camera.camera_delay = 25

        self.visible_chunks = [(self.camera.offset.x // self.window.config.chunk_size, self.camera.offset.y // self.window.config.chunk_size)]

        self.camera.add_group(group=self.layer_1, player=self.player)

        self.layer = Layer(y_sorted=False, collidable=False)

        # pygame.mouse.set_visible(False)
        # self.mouse_pos = pygame.Vector2()
        # self.mouse_img = pygame.transform.scale_by(pygame.image.load("./assets/sprite/mouse.png").convert_alpha(), 2)


    def render(self):
        self.window.display_surface.fill((255, 255, 255))

        for item in self.visible_chunks:
            chunk_x = int(item[0])
            chunk_y = int(item[1])
            chunk = generate_chunk(config=self.window.config, x=chunk_x, y=chunk_y)

            # tiles = render_chunk(self.window.config, self.window.display_surface, self.camera, chunk, chunk_x * self.window.config.chunk_size * self.window.config.tile_size - self.camera.offset.x * self.window.config.tile_size, chunk_y * self.window.config.chunk_size * self.window.config.tile_size - self.camera.offset.y * self.window.config.tile_size)

            # for sprite in tiles:
                # self.window.display_surface.blit(source=sprite.image, dest=sprite.rect)

            # self.layer.add(tile for tile in tiles)

            # self.camera.add_group(self.layer, self.player)


            # render_chunk(self.window.config, self.window.display_surface, chunk, (chunk_x * self.window.config.tile_size) - self.camera.offset.x * self.window.config.tile_size, (chunk_y * self.window.config.tile_size) - self.camera.offset.y * self.window.config.tile_size)

        self.camera.draw(player=self.player)
        self.window.screen.blit(source=arcade.pygame.transform.scale(surface=self.window.display_surface, size=self.window.screen.get_size()), dest=(0, 0))
        self.debugger.draw()
        # self.window.screen.blit(self.mouse_img, self.mouse_pos)


    def debug_render(self):
        self.debugger.font.render(surface=self.debugger.surface, text=f"FPS: {round(number=self.window.clock.get_fps())}", location=(10, 10))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Delta Time: {round(self.window.delta_time, 4)}", location=(10, 10 + self.debugger.font.line_height))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Player Pos: x = {int(self.player.position.x)}, y = {int(self.player.position.y)}", location=(10, 10 + (2 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Player State: {self.player.status}", location=(10, 10 + (3 * self.debugger.font.line_height)))


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