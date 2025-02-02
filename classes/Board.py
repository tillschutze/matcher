from Colors import Color, COLOR_NAMES
import random
import numpy as np

class Board:
    def __init__(self, dimension, colors: Color):
        self.dimension = dimension
        self.colors = colors
        self.board = self.create_main_board()
    
    def create_main_board(self):
        # Create a list of stone numbers (each stone is represented by its integer value)
        stones = []
        for color in self.colors:
            stones.extend([color.value] * self.dimension)
        
        assert len(stones) == self.dimension ** 2, "The total number of stones must equal rows * cols."
        
        # Shuffle and create a NumPy array
        random.shuffle(stones)
        board = np.array(stones).reshape(self.dimension, self.dimension)
        return board
    
    def print_board(self):
        for row in self.board:
            print(" | ".join(COLOR_NAMES[val] for val in row))