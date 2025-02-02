from classes.Board import Board
from classes.Deck import Deck
from classes.ActionButton import ActionButton

class Game:
    def __init__(self, screen, colors, dimension):
        self.board = Board(dimension, colors)
        self.deck = Deck(colors)
        self.swapButton = ActionButton((50, 500, 150, 50), "Swap", self.swap)
        
        
    def draw(self, screen):
        self.board.draw_board(screen)
        self.swapButton.draw(screen)
        
    def swap(self):
        print("Swapping!")

        
