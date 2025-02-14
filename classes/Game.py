from classes.Board import MainBoard, PlayerBoard, Pattern
from classes.Deck import Deck
from classes.ActionButton import ActionButton
from classes.Cell import Cell, PlayerBoardCell
from typing import Dict, Optional, List
import pygame

class Game:
    def __init__(self, screen, colors, dimension):
        self.screen: pygame.Surface = screen
        self.board: MainBoard = MainBoard(dimension, colors)
        self.deck: Deck = Deck(colors)
        self.playerBoard: PlayerBoard = PlayerBoard(dimension, self.deck)
        self.swapButton: ActionButton = ActionButton((50, 500, 150, 50), "Swap", self.start_swap)
        self.revealButton: ActionButton = ActionButton((50, 400, 150, 50), "Reveal", self.start_reveal)
        self.is_swapping: bool = False
        self.is_revealing: bool = False
        self.swapState: Optional[Dict] = None
        
        
    def draw(self, screen):
        self.board.draw_board(screen)
        self.playerBoard.draw_board(screen)
        self.swapButton.draw(screen)
        self.revealButton.draw(screen)
        
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
                    self.board.toggle_highlight(cell, True)
        
        else:
            # Second click: if clicked cell is one of the highlighted adjacent cells, perform the swap.
            if clicked_cell in self.swapState["adjacent"]:
                source = self.swapState["source"]
                target = clicked_cell
                # Swap their values.
                source.color, target.color = target.color, source.color
                print(f"Swapped cell at ({source.row}, {source.col}) with cell at ({target.row}, {target.col}).")
                for cell in self.swapState["adjacent"]:
                    self.board.toggle_highlight(cell, False)
                self.board.generate_pattern_list()
            else:
                print("Invalid target cell. Swap cancelled.")
            # Reset swap mode regardless of whether swap was successful.
            self.is_swapping = False
            self.swapState = None
            self.find_matching_patterns()

    def start_reveal(self):
        self.is_revealing = True

    def handle_reveal(self, clicked_cell: PlayerBoardCell):
        if clicked_cell.card.isFaceUp:
            return
        for cell in self.playerBoard.cells:
            if cell.row == clicked_cell.row and cell.col == clicked_cell.col -1 and cell.card.isFaceUp:
                clicked_cell.card.flip()
                self.is_revealing = False
            else: continue

    def find_matching_patterns(self):
        cells: List[PlayerBoardCell] = self.playerBoard.cells
        for cell in cells:
            if not cell.card.isFaceUp:
                continue
            print(cell.card)
            pattern = cell.card.pattern
            rotations: List[Pattern] = [
                pattern,
                [[pattern[1][0], pattern[0][0]], [pattern[1][1], pattern[0][1]]],
                [[pattern[1][1], pattern[1][0]], [pattern[0][1], pattern[0][0]]],
                [[pattern[0][1], pattern[1][1]], [pattern[0][0], pattern[1][0]]],
            ]

            for rotation in rotations:
                if rotation in self.board.patterns:
                    cell.card.highlight = True

                    print("this pattern is in the mainboard: ", pattern)

        
        
