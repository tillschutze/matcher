from classes.Board import PlayerBoard
from classes.Deck import Deck


class Player:
    def __init__(self, deck: Deck):
        self.player_board: PlayerBoard = PlayerBoard(4, deck)
        self.is_active: bool = False
