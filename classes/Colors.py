from enum import Enum

class Color(Enum):
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    
COLOR_NAMES = {
    0: "red",
    1: "blue",
    2: "green",
    3: "yellow"
}

color_to_rgb = {
        Color.RED: (255, 0, 0),
        Color.BLUE: (0, 0, 255),
        Color.GREEN: (0, 255, 0),
        Color.YELLOW: (255, 255, 0)
    }

rgb_to_color = {v: k for k, v in color_to_rgb.items()}
