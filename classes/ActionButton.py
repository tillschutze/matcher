import pygame
import Constants
from utils.PygameUtils import draw_rect


class ActionButton:
    def __init__(self, rect, text, callback):
        """
        :param rect: A tuple (x, y, width, height) defining the button's rectangle.
        :param text: The text to display on the button.
        :param callback: The function to call when the button is clicked.
        """
        self.rect = pygame.Rect(rect)
        self.text = text
        self.callback = callback
        self.font = pygame.font.Font(None, Constants.FONT_SIZE)
    
    def draw(self, surface):
        # Draw the button rectangle.
        draw_rect(surface, Constants.BUTTON_COLOR, self.rect)
        draw_rect(surface, Constants.OUTLINE_COLOR, self.rect, Constants.BORDER_WIDTH)
        
        # Render the text and center it in the button.
        text_surf = self.font.render(self.text, True, Constants.TEXT_COLOR)
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.callback()