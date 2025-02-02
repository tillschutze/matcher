from classes.Colors import Color, COLOR_NAMES, color_to_rgb
from classes.Cell import MainBoardCell, Cell, PlayerBoardCell, CellType
from classes.Deck import Deck
import random
import numpy as np
import pygame
from typing import List, Optional, Generic

class Board(Generic[CellType]):
    def __init__(self, dimension, origin=(50, 50), cell_size=50):
        self.dimension = dimension
        self.rows = dimension
        self.cols = dimension
        self.origin = origin
        self.cell_size = cell_size
        self.cells: List[CellType] = []
        self.create_board()
       
    def create_board(self):
        pass
    
    def draw_board(self, screen):
        pass

    def create_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_rect = pygame.Rect(
                    self.origin[0] + col * self.cell_size,
                    self.origin[1] + row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                cell = self.create_cell(cell_rect, row, col)
                self.cells.append(cell)
                
    def create_cell(self):
        pass        
    
    def find_clicked_cell(self, pos) -> Optional[CellType]:
        for cell in self.cells:
            if cell.rect.collidepoint(pos):
                return cell
        return None
    

class MainBoard(Board[MainBoardCell]):
    def __init__(self, dimension, colors: Color, origin=(50, 50), cell_size=50):
        self.colors = colors
        super().__init__(dimension, origin, cell_size)
        
    def create_board(self):
        stones = []
        for color in self.colors:
            stones.extend([color.value] * self.dimension)
        random.shuffle(stones)
        self.board = np.array(stones).reshape(self.rows, self.cols)
        self.create_cells()
        
    def create_cell(self, rect, row, col) -> MainBoardCell:
        cell_color_enum = Color(self.board[row][col])
        cell_color = color_to_rgb[cell_color_enum]
        return MainBoardCell(rect, cell_color, row, col)
          
    def draw_board(self, screen):
        for cell in self.cells:
            pygame.draw.rect(screen, cell.color, cell.rect)
            pygame.draw.rect(screen, cell.highlight_color, cell.rect, 3)
                  
    def toggle_highlight(self, screen, cell: MainBoardCell, highlight: bool):
        cell.highlight_color = (255, 0, 255) if highlight else (0, 0, 0) 
        
class PlayerBoard(Board[PlayerBoardCell]):
    def __init__(self, dimension, deck: Deck, origin=(300, 50), cell_size=80):
        self.deck = deck
        super().__init__(dimension, origin, cell_size)
        
    def create_board(self):
        self.create_cells()
        
    def create_cell(self, rect, row, col) -> PlayerBoardCell:
        return PlayerBoardCell(rect, row, col, 'swap', self.deck.draw(), 1)
    
    def draw_board(self, screen):
        for i, cell in enumerate(self.cells):
            if i % 4 == 0:
                cell.card.isFaceUp = True
            cell.card.draw(screen, cell.rect.x,cell.rect.y)
