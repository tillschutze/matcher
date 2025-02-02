from classes.Colors import Color
from classes.Card import Card
from classes.Deck import Deck
from classes.Board import Board
from classes.ActionButton import ActionButton
from classes.Game import Game
from actions.swap import swap
import pygame


if __name__ == '__main__':
    # Initialize Pygame.
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Board Game Prototype")
    
    colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    game = Game(screen, colors, 4)
    # Create buttons for actions.
    swapButton = ActionButton((50, 500, 150, 50), "Action 1", swap)
    # Set up a clock to control the framerate.
    clock = pygame.time.Clock()

    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            game.swapButton.handle_event(event)
                
         

        # Clear the screen.
        screen.fill((30, 30, 30))  # A dark background.
        # --- Draw the Main Board ---
        game.draw(screen)

        # --- Draw the Deck ---
        # We'll display a single "card back" rectangle representing the deck,
        # along with the number of cards remaining.
        deck_origin = (400, 50)      # Position of the deck on the screen.
        deck_card_width = 60
        deck_card_height = 80
        
        # Define a rectangle for the deck's card back.
        deck_rect = pygame.Rect(deck_origin[0], deck_origin[1], deck_card_width, deck_card_height)
        pygame.draw.rect(screen, (200, 200, 200), deck_rect)  # A light gray color for the back.
        pygame.draw.rect(screen, (0, 0, 0), deck_rect, 2)       # Black border.

        # Render the deck count (number of cards left).
        font = pygame.font.Font(None, 36)
        deck_count_text = font.render(str(len(game.deck.cards)), True, (255, 255, 255))
        # Position the text to the right of the deck card.
        text_pos = (deck_origin[0] + deck_card_width + 10, deck_origin[1] + deck_card_height // 2 - 18)
        screen.blit(deck_count_text, text_pos)

        # Update the display.
        pygame.display.flip()
        # Cap the framerate.
        clock.tick(60)

    pygame.quit()

    
    
    