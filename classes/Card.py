from classes.Colors import Color, COLOR_NAMES
from typing import List
from utils.PygameUtils import draw_rect

class Card: 
    def __init__(self, pattern: List[List[Color]],  points: int = 2, orientation: str = "base", isFaceUp: bool = False, width: int = 40, height: int = 40):
        self.pattern: List[List[Color]] = pattern
        self.isFaceUp = isFaceUp
        self.points = points
        self.orientation = orientation
        self.width = width
        self.height = height
        
    def __repr__(self):
        return f"Card(pattern={COLOR_NAMES[self.pattern[0][0]], COLOR_NAMES[self.pattern[0][1]], COLOR_NAMES[self.pattern[1][0]], COLOR_NAMES[self.pattern[1][1]]}, isFaceUp={self.isFaceUp})"
      
    def draw(self, screen, x, y):
        if self.isFaceUp:
            for i in range(2):
                for j in range(2):
                    draw_rect(screen, COLOR_NAMES[self.pattern[i][j]], (x + j * self.width, y + i * self.height, self.width, self.height))
                    draw_rect(screen, (0, 0, 0), (x + j * self.width, y + i * self.height, self.width, self.height), 1)
        else:
            draw_rect(screen, (255, 0, 255), (x, y, self.width * 2, self.height * 2))
        draw_rect(screen, (0, 0, 0), (x, y, self.width * 2, self.height * 2), 3)

    def rotate(self, screen, x, y):
        rotated_pattern: List[List[Color]] = [[self.pattern[1][0], self.pattern[0][0]], [self.pattern[1][1], self.pattern[0][1]]]
        self.pattern = rotated_pattern
        self.draw(screen, x, y)


    def flip(self):
        self.isFaceUp = not self.isFaceUp
        
    

