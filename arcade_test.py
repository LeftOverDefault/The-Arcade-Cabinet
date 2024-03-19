# def render_chunk(config, chunk_coordinates, chunk_x_offset, chunk_y_offset):
#     tiles = []
#     for coordinate in chunk_coordinates:
#         tile_x = (coordinate[0] * config.tile_size) + chunk_x_offset
#         tile_y = (coordinate[1] * config.tile_size) + chunk_y_offset
#         tiles.append([tile_x, tile_y])
#     return tiles


# class Main:
#     def __init__(self) -> None:
#         self.window = arcade.Arcade(config=config)
#         self.debugger = Debugger(font_path="./assets/font/font.png", config=self.window.config)

#         self.camera = Camera(display_surface=self.window.display_surface)
#         self.player = Player(initial_position=(288 / 2, 162 / 2), path="./assets/sprite/entity/player/", group=self.camera)

#         self.window.render = self.render
#         self.window.update = self.update
#         self.window.event = self.event
#         self.debugger.render = self.debug_render

#         self.camera.camera_delay = 25

#         with open("./world.json", "r") as file:
#             world = json.load(file)

#         self.world = World(self.window.display_surface, world, self.window.config)
#         self.world.camer = self.camera
#         self.world.player = self.player

#         pygame.event.set_grab(False)
#         # pygame.mouse.set_visible(False)
#         # self.mouse_pos = pygame.Vector2()
#         # self.mouse_img = pygame.transform.scale_by(pygame.image.load("./assets/sprite/mouse.png").convert_alpha(), 2)


#     def render(self) -> None:
#         self.window.display_surface.fill((255, 255, 255))

#         self.world.render(self.camera.offset)

#         self.camera.draw(player=self.player)
#         self.window.screen.blit(source=arcade.pygame.transform.scale(surface=self.window.display_surface, size=self.window.screen.get_size()), dest=(0, 0))
#         if self.window.config.debug == True:
#             self.debugger.draw()
#         # self.window.screen.blit(self.mouse_img, self.mouse_pos)


#     def debug_render(self) -> None:
#         self.debugger.font.render(surface=self.debugger.surface, text=f"Debug Menu:", location=(10, 10 + (0 * self.debugger.font.line_height)))
#         self.debugger.font.render(surface=self.debugger.surface, text=f"FPS: {round(number=self.window.clock.get_fps())}", location=(10, 10 + (1 * self.debugger.font.line_height)))
#         self.debugger.font.render(surface=self.debugger.surface, text=f"Delta Time: {round(self.window.delta_time, 4)}", location=(10, 10 + (2 * self.debugger.font.line_height)))
#         self.debugger.font.render(surface=self.debugger.surface, text=f"Player Pos: x = {int(self.player.position.x)}, y = {int(self.player.position.y)}", location=(10, 10 + (3 * self.debugger.font.line_height)))
#         self.debugger.font.render(surface=self.debugger.surface, text=f"Player State: {self.player.status}", location=(10, 10 + (4 * self.debugger.font.line_height)))


#     def update(self):
#         self.camera.update(delta_time=self.window.delta_time)
#         # self.mouse_pos = pygame.mouse.get_pos()



#     def event(self, event):
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_ESCAPE:
#                 pygame.quit()
#                 exit()


#     def run(self):
#         self.window.run()


# if __name__ == "__main__":
#     main = Main()
#     main.run()


import arcade
from arcade.debug.debugger import Debugger


config = {
    "name": "Arcade Test",
    "screen_multiplier": 6,
    "display_surface_multiplier": 1.5,
    "tile_size": 16,
    "chunk_size": 8,
    "debug": True,
    "tilesets": {
        "tilesheet": "./assets/sprite/tilesets/tileset.png",
        # "plains": "./assets/sprite/tilesets/plains.png"
    },
    "font": "./assets/font/font.png",
    "font_order": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ".", "-", ",", ":", "+", "'", "!", "?", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "(", ")", "/", "_", "=", "\\", "[", "]", "*", "\"", "<", ">", ";", "|", "~", "£", "ƒ", "{", "}", "@", "#", "$", "%", "&", "^", "`"],
    "font_size": 2,
    "world_name": "overworld",
    "world_directory": "./build/",
    "player_path": "./assets/sprite/entity/player/"
}


class Main:
    def __init__(self, config) -> None:
        self.config = config
        self.arcade = arcade.Arcade(self.config)

        self.debugger = Debugger(self.arcade.config.font, self.arcade.config)
        self.debugger.render = self.debug_render

        self.arcade.debugger = self.debugger

    
    def debug_render(self) -> None:
        self.debugger.font.render(surface=self.debugger.surface, text=f"Debug Menu:", location=(10, 10 + (0 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"FPS: {round(number=self.arcade.clock.get_fps())}", location=(10, 10 + (1 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Delta Time: {round(self.arcade.delta_time, 4)}", location=(10, 10 + (2 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Player Pos: x = {int(self.arcade.world.player.position.x)}, y = {int(self.arcade.world.player.position.y)}", location=(10, 10 + (3 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Player State: {self.arcade.world.player.status}", location=(10, 10 + (4 * self.debugger.font.line_height)))
        self.debugger.font.render(surface=self.debugger.surface, text=f"Rendered Tile Count: {len(self.arcade.world.camera.sprites())}", location=(10, 10 + (5 * self.debugger.font.line_height)))
    

    def run(self) -> None:
        self.arcade.run()


if __name__ == "__main__":
    main = Main(config)
    main.run()