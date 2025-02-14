from classes.Colors import Color, rgb_to_color, color_to_rgb
from classes.Cell import MainBoardCell, PlayerBoardCell, CellType
from classes.Deck import Deck
from utils.PygameUtils import draw_rect
import random
import numpy as np
import pygame
import Constants
from typing import List, Optional, Generic, TypeAlias

Pattern: TypeAlias = List[List[Color]]

class Board(Generic[CellType]):
    def __init__(self, dimension, origin, cell_size):
        self.dimension: int = dimension
        self.rows: int = dimension
        self.cols: int = dimension
        self.origin = origin
        self.cell_size = cell_size
        self.cells: List[CellType] = []
        self.board = None
        self.patterns: List[Pattern] = []
        self.board = np.empty((dimension, dimension), dtype=object)
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
                self.board[row, col] = cell
                self.cells.append(cell)
                
    def create_cell(self, rect, row, col) -> CellType:
        pass        
    
    def find_clicked_cell(self, pos) -> Optional[CellType]:
        for cell in self.cells:
            if cell.rect.collidepoint(pos):
                return cell
        return None
    

class MainBoard(Board[MainBoardCell]):
    def __init__(self, dimension, colors: List[Color], origin=Constants.MAIN_BOARD_ORIGIN, cell_size=Constants.MAIN_BOARD_CELL_SIZE):
        self.colors = colors
        self.stones = []
        super().__init__(dimension, origin, cell_size)
        self.generate_pattern_list()
        
    def create_board(self):
        for color in self.colors:
            self.stones.extend([color.value] * self.dimension)
        random.shuffle(self.stones)
        self.create_cells()

    def create_cell(self, rect, row, col) -> MainBoardCell:
        cell_color_enum: Color = Color(self.stones.pop())
        cell_color = color_to_rgb[cell_color_enum]
        return MainBoardCell(rect, cell_color, row, col)
          
    def draw_board(self, screen):
        for cell in self.cells:
            draw_rect(screen, cell.color, cell.rect)
            draw_rect(screen, cell.highlight_color, cell.rect, 2)

    def generate_pattern_list(self):
        patterns: List[Pattern] = []
        for row in range(self.rows - 1):
            for column in range(self.cols -1 ):
                pattern: Pattern = [[Color.RED for _ in range(2)] for _ in range(2)]
                for cell in self.cells:
                    if cell.row == row and cell.col == column:
                        pattern[0][0] = rgb_to_color.get(cell.color, None).value
                    if cell.row == row + 1 and cell.col == column:
                        pattern[1][0] = rgb_to_color.get(cell.color, None).value
                    if cell.row == row + 1 and cell.col == column + 1:
                        pattern[1][1] = rgb_to_color.get(cell.color, None).value
                    if cell.row == row and cell.col == column + 1:
                        pattern[0][1] = rgb_to_color.get(cell.color, None).value
                patterns.append(pattern)
        self.patterns = patterns

    def toggle_highlight(self, cell: MainBoardCell, highlight: bool):
        cell.highlight_color = Constants.HIGHLIGHT_COLOR if highlight else Constants.OUTLINE_COLOR
        
class PlayerBoard(Board[PlayerBoardCell]):
    def __init__(self, dimension, deck: Deck, origin=Constants.PLAYER_BOARD_ORIGIN, cell_size=Constants.PLAYER_BOARD_CELL_SIZE):
        self.deck = deck
        super().__init__(dimension, origin, cell_size)

    def create_board(self):
        self.create_cells()

    def create_cell(self, rect, row, col) -> PlayerBoardCell:
        return PlayerBoardCell(rect, row, col, 'swap', self.deck.draw(), 1)
    
    def draw_board(self, screen):
        for i, cell in enumerate(self.cells):
            if not cell.card:
                draw_rect(screen, Constants.EMPTY_CELL_COLOR, cell.rect)
                continue
            if i % self.dimension == 0:
                cell.card.isFaceUp = True
            cell.card.draw(screen, cell.rect.x,cell.rect.y)

