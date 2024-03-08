import world_engine


# class WorldEngineTest:
#     def __init__(self, config) -> None:
#         self.configuration = world_engine.Configure(config=config)
#         self.engine = world_engine.WorldEngine(self.configuration)
#         self.debugger = world_engine.Debugger(font_path="./assets/font/font.png", config=self.configuration)

#         self.debugger.render = self.debug_render
#         self.engine.debugger = self.debugger




#     def run(self):
#         self.engine.run()


config = {
    "screen_multiplier": 6,
    "display_surface_multiplier": 2,
    "tile_size": 16,
    "chunk_size": 8,
    "debug": True,
    "tilesets": [
        "./assets/sprite/tilesets/plains.png"
    ],
    "font": "./assets/font/font.png",
    "world_name": "overworld",
    "layers": [
        "Layer_1",
        "Layer_2"
    ]
}


if __name__ == "__main__":
    engine = world_engine.WorldEngine(config=config)

    def debug_render(self):
        self.font.render(surface=self.surface, text=f"Debug Menu:", location=(10, 10 + (0 * self.font.line_height)))
        self.font.render(surface=self.surface, text=f"FPS: {round(number=engine.clock.get_fps())}", location=(10, 10 + (1 * self.font.line_height)))
        self.font.render(surface=self.surface, text=f"Delta Time: {round(number=engine.delta_time, ndigits=4)}", location=(10, 10 + (2 * self.font.line_height)))

    engine.debugger.render = debug_render
    engine.run()