from Colors import Color
from Card import Card
from Deck import Deck
from Board import Board


if __name__ == '__main__':
    colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    board = Board(4, colors)
    board.create_main_board()
    print(board)
    deck = Deck(colors)
    print(deck)
    
    