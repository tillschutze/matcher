import pygame


class Cell: 
    def __init__(self, rect: pygame.Rect, color):
        self.rect: pygame.rect = rect
        self.color = color
        
    def __repr__(self):
        return f"Cell(rect={self.rect.x},{self.rect.y}, color={self.color})"