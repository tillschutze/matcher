from classes.Colors import Color, COLOR_NAMES
from typing import List
from utils.PygameUtils import draw_rect
import Constants

class Card: 
    def __init__(self, pattern: List[List[Color]],  isFaceUp: bool = False, width: int = Constants.CARD_WIDTH, height: int = Constants.CARD_WIDTH):
        self.pattern: List[List[Color]] = pattern
        self.isFaceUp = isFaceUp
        self.width = width
        self.height = height
        self.highlight: bool = False
        
    def __repr__(self):
        return f"Card(pattern={COLOR_NAMES[self.pattern[0][0]], COLOR_NAMES[self.pattern[0][1]], COLOR_NAMES[self.pattern[1][0]], COLOR_NAMES[self.pattern[1][1]]}, isFaceUp={self.isFaceUp})"
      
    def draw(self, screen, x, y):
        if self.isFaceUp:
            for i in range(Constants.CARD_DIMENSIONS):
                for j in range(Constants.CARD_DIMENSIONS):
                    draw_rect(screen, COLOR_NAMES[self.pattern[i][j]], (x + j * self.width, y + i * self.height, self.width, self.height))
                    draw_rect(screen, Constants.HIGHLIGHT_COLOR if self.highlight else  Constants.OUTLINE_COLOR, (x + j * self.width, y + i * self.height, self.width, self.height), Constants.CARD_BORDER_WIDTH)
        else:
            draw_rect(screen, Constants.HIGHLIGHT_COLOR, (x, y, self.width * Constants.CARD_DIMENSIONS, self.height * Constants.CARD_DIMENSIONS))
        draw_rect(screen, Constants.HIGHLIGHT_COLOR if self.highlight else  Constants.OUTLINE_COLOR, (x, y, self.width * Constants.CARD_DIMENSIONS, self.height * Constants.CARD_DIMENSIONS), Constants.BORDER_WIDTH)

    def rotate(self, screen, x, y):
        rotated_pattern: List[List[Color]] = [[self.pattern[1][0], self.pattern[0][0]], [self.pattern[1][1], self.pattern[0][1]]]
        self.pattern = rotated_pattern
        self.draw(screen, x, y)


    def flip(self):
        self.isFaceUp = not self.isFaceUp
        
    

