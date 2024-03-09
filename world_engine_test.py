import world_engine


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
    ],
    "build_directory": "./build/"
}


def debug_render(self):
    self.font.render(surface=self.surface, text=f"Debug Menu:", location=(10, 10 + (0 * self.font.line_height)))
    self.font.render(surface=self.surface, text=f"FPS: {round(number=engine.clock.get_fps())}", location=(10, 10 + (1 * self.font.line_height)))
    self.font.render(surface=self.surface, text=f"Delta Time: {round(number=engine.delta_time, ndigits=4)}", location=(10, 10 + (2 * self.font.line_height)))


if __name__ == "__main__":
    engine = world_engine.WorldEngine(config=config)
    engine.debugger.render = debug_render
    engine.run()