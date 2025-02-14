import pygame
from classes.Card import Card
from typing import TypeVar, Optional


class Cell: 
    def __init__(self, rect: pygame.Rect, row, col):
        self.rect: pygame.rect = rect
        self.row = row
        self.col = col
        
    def __repr__(self):
        return f"Cell(rect={self.rect.x},{self.rect.y})"
    
class MainBoardCell(Cell):
    def __init__(self, rect, color, row, col): 
        super().__init__(rect, row, col)
        self.color = color
        self.highlight_color = (0, 0, 0)
        
class  PlayerBoardCell(Cell):
    def __init__(self, rect, row, col, action: str, card: Card, strength: int): 
        super().__init__(rect, row, col)
        self.card: Optional[Card] = card
        self.action = action
        self.strength = strength

    def rotate_card(self, screen):
        if self.card:
            self.card.rotate(screen, self.rect.x, self.rect.y)

        
CellType = TypeVar('CellType', bound=Cell)

 