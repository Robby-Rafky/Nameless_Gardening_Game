# All external libraries
import pygame

pygame.init()
# Colour definitions
BLACK = (0, 0, 0)
GREY = (105, 105, 105)
GREEN = (40, 87, 23)
BROWN = (51, 30, 4)
WHITE = (255, 255, 255)

# Global use functions


def clamp(n, upper, lower):
    return max(min(upper, n), lower)
