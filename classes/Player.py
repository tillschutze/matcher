from classes.Board import PlayerBoard
from classes.Deck import Deck
import Constants


class Player:
    def __init__(self, deck: Deck):
        self.player_board: PlayerBoard = PlayerBoard(Constants.DIMENSIONS, deck)
        self.is_active: bool = False
