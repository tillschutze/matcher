from classes.Colors import Color
from classes.Card import Card
from classes.Deck import Deck
from classes.Board import Board
import pygame


if __name__ == '__main__':
    # Initialize Pygame.
    pygame.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Board Game Prototype")

    # Define a mapping from Color enum to RGB tuples.
    color_to_rgb = {
        Color.RED: (255, 0, 0),
        Color.BLUE: (0, 0, 255),
        Color.GREEN: (0, 255, 0),
        Color.YELLOW: (255, 255, 0)
    }
    
    colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    board = Board(4, colors)
    print(board)
    deck = Deck(colors)
    print(deck)
    
    # Set up a clock to control the framerate.
    clock = pygame.time.Clock()

    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                clicked_cell = board.find_clicked_cell(pos)
                print(clicked_cell)

        # Clear the screen.
        screen.fill((30, 30, 30))  # A dark background.

        # --- Draw the Main Board ---
        # Define where the board will be drawn.
        board_origin = (50, 50)  # Top-left corner of the board on the screen.
        cell_size = 50           # Each cell will be 50x50 pixels.
        
        board.draw_board(screen)
        # Loop through each cell and draw its rectangle.
        # for row in range(board.rows):
            # for col in range(board.cols):
            #     # Get the color value from the board's grid.
            #     # (Assuming board.grid is a NumPy array of integers)
            #     cell_value = board.board[row][col]
            #     # Convert integer to Color enum.
            #     cell_color_enum = Color(cell_value)
            #     cell_color = color_to_rgb[cell_color_enum]
                
            #     # Define the cell rectangle.
            #     cell_rect = pygame.Rect(
            #         board_origin[0] + col * cell_size,
            #         board_origin[1] + row * cell_size,
            #         cell_size,
            #         cell_size
            #     )
            #     # Draw the cell.
            #     pygame.draw.rect(screen, cell_color, cell_rect)
            #     # Draw a border for clarity.
            #     pygame.draw.rect(screen, (0, 0, 0), cell_rect, 2)

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
        deck_count_text = font.render(str(len(deck.cards)), True, (255, 255, 255))
        # Position the text to the right of the deck card.
        text_pos = (deck_origin[0] + deck_card_width + 10, deck_origin[1] + deck_card_height // 2 - 18)
        screen.blit(deck_count_text, text_pos)

        # Update the display.
        pygame.display.flip()
        # Cap the framerate.
        clock.tick(60)

    pygame.quit()

    
    
    