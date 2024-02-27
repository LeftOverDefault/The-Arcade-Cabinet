import arcade.top_down as top_down

world = {
    "0;0": {
        "0;0": -1, "1;0": -1, "2;0": -1, "3;0": -1, "4;0": -1, "5;0": -1, "6;0": -1, "7;0": -1,
        # "0;1": -1, "1;1": -1, "2;1": -1, "3;1": -1, "4;1": -1, "5;1": -1, "6;1": -1, "7;1": -1,
        # "0;2": -1, "1;2": -1, "2;2": -1, "3;2": -1, "4;2": -1, "5;2": -1, "6;2": -1, "7;2": -1,
        # "0;3": -1, "1;3": -1, "2;3": -1, "3;3": -1, "4;3": -1, "5;3": -1, "6;3": -1, "7;3": -1,
        # "0;4": -1, "1;4": -1, "2;4": -1, "3;4": -1, "4;4": -1, "5;4": -1, "6;4": -1, "7;4": -1,
        # "0;5": -1, "1;5": -1, "2;5": -1, "3;5": -1, "4;5": -1, "5;5": -1, "6;5": -1, "7;5": -1,
        # "0;6": -1, "1;6": -1, "2;6": -1, "3;6": -1, "4;6": -1, "5;6": -1, "6;6": -1, "7;6": -1,
        # "0;7": 0, "1;7": 0, "2;7": 0, "3;7": 0, "4;7": 0, "5;7": 0, "6;7": 0, "7;7": 0,
    }
}

config = {
    "name": "Arcade Test v0.1.0",
    "resolution": [int(192 * 1.25), int(108 * 1.25)],
    "scale_factor": 5,
    "tile_size": 16,
    "chunk_size": 8,
    "camera_delay": 25,
    "fps": 60,
    "fullscreen": False,
    "worlds": [
        world
    ]
}


if __name__ == "__main__":
    top_down.create_config(configuration=config)
    window = top_down.Window()
    window.run()