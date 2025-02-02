from classes.Board import MainBoard, PlayerBoard
from classes.Deck import Deck
from classes.ActionButton import ActionButton
from classes.Cell import Cell
from typing import Dict, Optional
import pygame

class Game:
    def __init__(self, screen, colors, dimension):
        self.screen: pygame.Surface = screen
        self.board: MainBoard = MainBoard(dimension, colors)
        self.deck: Deck = Deck(colors)
        self.playerBoard: PlayerBoard = PlayerBoard(dimension, self.deck)
        self.swapButton: ActionButton = ActionButton((50, 500, 150, 50), "Swap", self.start_swap)
        self.is_swapping: bool = False
        self.swapState: Optional[Dict] = None
        
        
    def draw(self, screen):
        self.board.draw_board(screen)
        self.playerBoard.draw_board(screen)
        self.swapButton.draw(screen)
        
    def start_swap(self):
        print("Swapping!")
        self.is_swapping = True
        self.swapState = None
        
    def handle_swap(self, clicked_cell: Cell, screen):
        if self.swapState is None:
            # First click: choose the source cell.
            self.swapState = {"source": clicked_cell, "adjacent": []}
            # Find all orthogonally adjacent cells.
            for cell in self.board.cells:
                if cell == clicked_cell:
                    continue
                # Check if the cell is directly to the left/right or above/below.
                if (cell.row == clicked_cell.row and abs(cell.col - clicked_cell.col) == 1) or (cell.col == clicked_cell.col and abs(cell.row - clicked_cell.row) == 1):
                    self.swapState["adjacent"].append(cell)
                    self.board.toggle_highlight(screen, cell, True)
        
        else:
            # Second click: if clicked cell is one of the highlighted adjacent cells, perform the swap.
            if clicked_cell in self.swapState["adjacent"]:
                source = self.swapState["source"]
                target = clicked_cell
                # Swap their values.
                source.color, target.color = target.color, source.color
                print(f"Swapped cell at ({source.row}, {source.col}) with cell at ({target.row}, {target.col}).")
                for cell in self.swapState["adjacent"]:
                    self.board.toggle_highlight(screen, cell, False)
            else:
                print("Invalid target cell. Swap cancelled.")
            # Reset swap mode regardless of whether swap was successful.
            self.is_swapping = False
            self.swapState = None

        
        
