from typing import Optional
import Constants
from classes.Cell import PlayerBoardCell, MainBoardCell
from classes.Colors import Color
from classes.Game import Game
import pygame


if __name__ == '__main__':
    # Initialize Pygame.
    pygame.init()
    screen_width, screen_height = Constants.GAME_BOARD_WIDTH, Constants.GAME_BOARD_HEIGHT
    screen: pygame.Surface = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Board Game Prototype")
    
    colors = [Color.RED, Color.BLUE, Color.GREEN, Color.YELLOW]
    game = Game(screen, colors, Constants.DIMENSIONS)
    # Set up a clock to control the framerate.
    clock = pygame.time.Clock()

    running = True
    while running:
        # Event handling.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            game.endTurnButton.handle_event(event)
            game.swapButton.handle_event(event)
            game.revealButton.handle_event(event)
            game.resolveButton.handle_event(event)
            game.cardSwapButton.handle_event(event)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if game.is_swapping_stones:
                    clicked_cell: Optional[MainBoardCell] = game.board.find_clicked_cell(event.pos)
                    if clicked_cell is None:
                        continue
                    else:
                        game.handle_swapping_stones(clicked_cell)
                elif game.is_revealing:
                    clicked_cell: Optional[PlayerBoardCell] = game.active_player.player_board.find_clicked_cell(event.pos)
                    if clicked_cell is None:
                        continue
                    else:
                        game.handle_reveal(clicked_cell)
                elif game.is_resolving_card:
                    clicked_cell: Optional[PlayerBoardCell] = game.active_player.player_board.find_clicked_cell(event.pos)
                    if clicked_cell is None:
                        continue
                    else:
                        game.handle_resolving_card(clicked_cell)
                elif game.is_swapping_cards:
                    clicked_cell: Optional[PlayerBoardCell] = game.active_player.player_board.find_clicked_cell(event.pos)
                    if clicked_cell is None:
                        continue
                    else:
                        game.handle_swapping_cards(clicked_cell)
                else:
                    clicked_cell: Optional[PlayerBoardCell] = game.active_player.player_board.find_clicked_cell(event.pos)
                    if clicked_cell is None:
                        continue
                    else:
                        clicked_cell.rotate_card(game.screen)




                
        # Clear the screen.
        screen.fill(Constants.BACKGROUND_COLOR)  # A dark background.
        # --- Draw the Main Board ---
        game.draw(screen)
        game.find_matching_patterns()

        # Update the display.
        pygame.display.flip()
        # Cap the framerate.
        clock.tick(60)

    pygame.quit()

    
    
    