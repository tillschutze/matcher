from classes.Board import MainBoard, PlayerBoard, Pattern
from classes.Card import Card
from classes.Deck import Deck
from classes.ActionButton import ActionButton
from classes.Cell import Cell, PlayerBoardCell
from typing import Dict, Optional, List
import pygame

from classes.Player import Player


class Game:
    def __init__(self, screen, colors, dimension, player_count = 2):
        self.screen: pygame.Surface = screen
        self.board: MainBoard = MainBoard(dimension, colors)
        self.deck: Deck = Deck(colors)
        self.players: List[Player] = [Player(self.deck) for _ in range(player_count)]
        self.active_index = 0
        self.endTurnButton: ActionButton = ActionButton((50, 300, 150, 50), "End Turn", self.end_turn)
        self.swapButton: ActionButton = ActionButton((50, 360, 150, 50), "Swap Stones", self.start_swapping_stones)
        self.revealButton: ActionButton = ActionButton((50, 420, 150, 50), "Reveal", self.start_reveal)
        self.resolveButton: ActionButton = ActionButton((50, 480, 150, 50), "Resolve", self.start_resolving_card)
        self.cardSwapButton: ActionButton = ActionButton((50, 540, 150, 50), "Swap Cards", self.start_swapping_card)
        self.is_swapping_stones: bool = False
        self.is_swapping_cards: bool = False
        self.is_revealing: bool = False
        self.is_resolving_card: bool = False
        self.stone_swap_state: Optional[Dict] = None
        self.card_swap_state: Optional[Dict] = None

    @property
    def active_player(self):
        return self.players[self.active_index]

    def end_turn(self):
        self.active_index = (self.active_index + 1) % len(self.players)

    def draw(self, screen):
        self.board.draw_board(screen)
        self.active_player.player_board.draw_board(screen)
        self.swapButton.draw(screen)
        self.revealButton.draw(screen)
        self.resolveButton.draw(screen)
        self.cardSwapButton.draw(screen)
        self.endTurnButton.draw(screen)
        
    def start_swapping_stones(self):
        self.is_swapping_stones = True
        self.stone_swap_state = None
        
    def handle_swapping_stones(self, clicked_cell: Cell):
        if self.stone_swap_state is None:
            self.stone_swap_state = {"source": clicked_cell, "adjacent": []}
            for cell in self.board.cells:
                if cell == clicked_cell:
                    continue
                if (cell.row == clicked_cell.row and abs(cell.col - clicked_cell.col) == 1) or (cell.col == clicked_cell.col and abs(cell.row - clicked_cell.row) == 1):
                    self.stone_swap_state["adjacent"].append(cell)
                    self.board.toggle_highlight(cell, True)
        
        else:
            if clicked_cell == self.stone_swap_state["source"]:
                for cell in self.stone_swap_state["adjacent"]:
                    self.board.toggle_highlight(cell, False)
                self.stone_swap_state = None
                return
            if clicked_cell in self.stone_swap_state["adjacent"]:
                source = self.stone_swap_state["source"]
                target = clicked_cell
                source.color, target.color = target.color, source.color
                for cell in self.stone_swap_state["adjacent"]:
                    self.board.toggle_highlight(cell, False)
                self.board.generate_pattern_list()
                self.is_swapping_stones = False
                self.stone_swap_state = None

    def start_swapping_card(self):
        self.is_swapping_cards = True
        self.card_swap_state = None

    def handle_swapping_cards(self, clicked_cell: PlayerBoardCell):
        if self.card_swap_state is None:
            self.card_swap_state = {"source": clicked_cell, "adjacent": []}
            row = clicked_cell.row
            for cell in self.active_player.player_board.board[row]:
                if cell == clicked_cell:
                    continue
                if cell.card and cell.card.isFaceUp:
                    self.card_swap_state["adjacent"].append(cell)
                    cell.card.highlight = True
        else:
            if clicked_cell == self.card_swap_state["source"]:
                for cell in self.card_swap_state["adjacent"]:
                    cell.card.highlight = False
                self.card_swap_state = None
                return
            if clicked_cell in self.card_swap_state["adjacent"]:
                source = self.card_swap_state["source"]
                target = clicked_cell
                source.card, target.card = target.card, source.card
                for cell in self.card_swap_state["adjacent"]:
                    cell.card.highlight = False
                source.card.highlight = False
                self.board.generate_pattern_list()
                self.is_swapping_cards = False
                self.card_swap_state = None

    def start_reveal(self):
        self.is_revealing = True

    def handle_reveal(self, clicked_cell: PlayerBoardCell):
        if not clicked_cell.card or clicked_cell.card.isFaceUp:
            return
        for cell in self.active_player.player_board.cells:
            if cell.row == clicked_cell.row and cell.col == clicked_cell.col -1 and (not cell.card or cell.card.isFaceUp):
                clicked_cell.card.flip()
                self.is_revealing = False
            else: continue

    def start_resolving_card(self):
        self.is_resolving_card = True

    def handle_resolving_card(self, clicked_cell: PlayerBoardCell):
        if clicked_cell.card.isFaceUp and clicked_cell.card.highlight:
            clicked_cell.card = None
            self.is_resolving_card = False

    def find_matching_patterns(self):
        cells: List[PlayerBoardCell] = self.active_player.player_board.cells
        for cell in cells:
            if not cell.card or not cell.card.isFaceUp:
                continue

            if cell.col > 0 and  self.active_player.player_board.board[cell.row][cell.col -1].card:
                continue

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
