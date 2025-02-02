from classes.Colors import Color
from classes.Game import Game
import pygame


if __name__ == '__main__':
    # Initialize Pygame.
    pygame.init()
    screen_width, screen_height = 800, 600
    screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Board Game Prototype")
    
    colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    game = Game(screen, colors, 4)
    # Set up a clock to control the framerate.
    clock = pygame.time.Clock()

    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            game.swapButton.handle_event(event)
            
            if game.is_swapping and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                clicked_cell = game.board.find_clicked_cell(event.pos)
                if clicked_cell is  None:
                    continue
                else:  
                    game.handle_swap(clicked_cell, screen)                  

                
        # Clear the screen.
        screen.fill((30, 30, 30))  # A dark background.
        # --- Draw the Main Board ---
        game.draw(screen)
        
        # Update the display.
        pygame.display.flip()
        # Cap the framerate.
        clock.tick(60)

    pygame.quit()

    
    
    