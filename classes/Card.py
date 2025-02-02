from classes.Colors import Color, COLOR_NAMES
from typing import List

class Card: 
    def __init__(self, pattern: List[List[Color]],  points: int = 2, orientation: str = "base", isFaceUp: bool = False, width: int = 60, height: int = 80):
        self.pattern = pattern
        self.isFaceUp = isFaceUp
        self.points = points
        self.orientation = orientation
        self.width = width
        self.height = height
        
    def __repr__(self):
        return f"Card(pattern={COLOR_NAMES[self.pattern[0][0]], COLOR_NAMES[self.pattern[0][1]], COLOR_NAMES[self.pattern[1][0]], COLOR_NAMES[self.pattern[1][1]]}, isFaceUp={self.isFaceUp})"
        
    def flip(self):
        self.isFaceUp = not self.isFaceUp
        
    

