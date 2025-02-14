import pygame


def draw_rect (screen: pygame.Surface, color, rect, width = 0, border_radius = -1, border_tlr = -1, border_trr = -1, border_blr = -1, border_brr = -1):
    pygame.draw.rect(screen, color, rect, width, border_radius, border_tlr, border_trr, border_blr, border_brr)