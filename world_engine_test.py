import world_engine


config = {
    "screen_multiplier": 6,
    "display_surface_multiplier": 2,
    "tile_size": 16,
    "chunk_size": 8,
    "debug": True,
    "tileset": "./assets/sprite/tilesets/plains.png"
}


if __name__ == "__main__":
    configuration = world_engine.Configure(config=config)
    engine = world_engine.WorldEngine(configuration)
    engine.run()