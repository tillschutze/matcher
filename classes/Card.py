from classes.Colors import Color, COLOR_NAMES
from typing import List
import pygame

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
                    pygame.draw.rect(screen, COLOR_NAMES[self.pattern[i][j]], (x + i * self.width, y + j * self.height, self.width, self.height))
                    pygame.draw.rect(screen, (0, 0, 0), (x + i * self.width, y + j * self.height, self.width, self.height), 1)
        else:
            pygame.draw.rect(screen, (255, 0, 255), (x, y, self.width * 2, self.height * 2))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, self.width * 2, self.height * 2), 3)
      
    def flip(self):
        self.isFaceUp = not self.isFaceUp
        
    

