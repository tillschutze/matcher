from Card import Card
from Colors import Color
from typing import List
import random

class Deck:
    def __init__(self, colors: List[Color]):
        self.colors = colors
        self.cards: List[Card] = self.create_deck()
        self.shuffle()
        
    def __repr__(self):
        return f"Deck(colors={self.colors}, cards={self.cards}) \n"
        
    def create_deck(self) -> List[Card]:
        cards: List[Card] = []
        all_patterns = self.generate_unique_patterns(self.colors)
        for pattern in all_patterns:
            cards.append(Card(pattern))
        return cards
        
    def generate_unique_patterns(self, colors: List[Color]) -> List[List[List[Color]]]:
        all_patterns = []
        seen = set()

        # There are four positions in the 2x2 grid: positions (0,0), (0,1), (1,0), (1,1)
        # Iterate over all possible assignments of colors to these positions.
        for c1 in colors:
            for c2 in colors:
                for c3 in colors:
                    for c4 in colors:
                        # Create the pattern as a tuple of tuples.
                        pattern = ((c1.value, c2.value), (c3.value, c4.value))
                        
                        # Compute rotations: 0, 90, 180, 270 degrees.
                        rotations = [
                            pattern,
                            ((c3.value, c1.value), (c4.value, c2.value)),  # 90 degrees rotation
                            ((c4.value, c3.value), (c2.value, c1.value)),  # 180 degrees rotation
                            ((c2.value, c4.value), (c1.value, c3.value))   # 270 degrees rotation
                        ]
                        # Use the lexicographically smallest rotation as the canonical representation.
                        canonical = min(rotations)
                        if canonical not in seen:
                            seen.add(canonical)
                            print(canonical)
                            # Convert canonical pattern to a list-of-lists format.
                            pattern_list = [list(canonical[0]), list(canonical[1])]
                            all_patterns.append(pattern_list)
        return all_patterns

            
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self):
        pass