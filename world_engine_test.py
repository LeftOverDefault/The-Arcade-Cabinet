import world_engine


config = {
    "tile_size": 16,
    "chunk_size": 8,
    "debug": True,
}


if __name__ == "__main__":
    configuration = world_engine.Configure(config=config)
    engine = world_engine.WorldEngine(configuration)
    # engine = world_engine.WorldEngine()
    engine.run()