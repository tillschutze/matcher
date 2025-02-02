from classes.Colors import Color, COLOR_NAMES, color_to_rgb
from classes.Cell import Cell
import random
import numpy as np
import pygame
from typing import List, Optional

class Board:
    def __init__(self, dimension, colors: Color, origin=(50, 50), cell_size=50):
        self.dimension = dimension
        self.colors = colors
        self.rows = dimension
        self.cols = dimension
        self.origin = origin
        self.cell_size = cell_size
        self.cells: List[Cell] = []
        self.create_main_board()
    
    def create_main_board(self):
        # Create a list of stone numbers (each stone is represented by its integer value)
        stones = []
        for color in self.colors:
            stones.extend([color.value] * self.dimension)
        
        assert len(stones) == self.dimension ** 2, "The total number of stones must equal rows * cols."
        
        # Shuffle and create a NumPy array
        random.shuffle(stones)
        self.board = np.array(stones).reshape(self.rows, self.cols)
        self.create_cells()
    
    
    
    def create_cells(self):
        for row in range(self.rows):
            for col in range(self.cols):
                cell_rect = pygame.Rect(
                    self.origin[0] + col * self.cell_size,
                    self.origin[1] + row * self.cell_size,
                    self.cell_size,
                    self.cell_size
                )
                cell_color_enum = Color(self.board[row][col])
                cell_color = color_to_rgb[cell_color_enum]
                cell = Cell(cell_rect, cell_color)
                self.cells.append(cell)
            
            
    def draw_board(self, screen):
        for cell in self.cells:
            pygame.draw.rect(screen, cell.color, cell.rect)
            pygame.draw.rect(screen, (0, 0, 0), cell.rect, 2)
            
    def find_clicked_cell(self, pos) -> Optional[Cell]:
        for cell in self.cells:
            if cell.rect.collidepoint(pos):
                return cell
        return None
    

    def __repr__(self):
        board_str = "Main Board:\n"
        for row in self.board:
            board_str += " | ".join(COLOR_NAMES[val] for val in row) + "\n"
        return board_str