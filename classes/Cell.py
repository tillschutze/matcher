import pygame


class Cell: 
    def __init__(self, rect: pygame.Rect, color, row, col):
        self.rect: pygame.rect = rect
        self.color = color
        self.row = row
        self.col = col
        
    def __repr__(self):
        return f"Cell(rect={self.rect.x},{self.rect.y}, color={self.color})"