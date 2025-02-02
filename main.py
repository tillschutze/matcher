from classes.Colors import Color
from classes.Card import Card
from classes.Deck import Deck
from classes.Board import Board


if __name__ == '__main__':
    colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    board = Board(4, colors)
    board.create_main_board()
    print(board)
    deck = Deck(colors)
    print(deck)
    
    