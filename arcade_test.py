import arcade


config = {
    "name": "Arcade Test v0.1.0",
    "resolution": [192, 108],
    "scale_factor": 5,
    "fps": 60,
    "fullscreen": False
}


if __name__ == "__main__":
    arcade.create_config(configuration=config)
    window = arcade.Window()
    window.run()