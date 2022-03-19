# All external libraries
import pygame

# Colour definitions
BLACK = (0, 0, 0)
BLUE = (4, 18, 105)
GREY = (105, 105, 105)
LIGHT_GREY = (199, 199, 199)
GREEN = (40, 87, 23)
BROWN = (51, 30, 4)
WHITE = (255, 255, 255)
RED = (117, 13, 13)
LIGHT_ORANGE = (235, 169, 94)
MENU_GREY = (194, 194, 194)


# Global use functions


def clamp(n, upper, lower):
    return max(min(upper, n), lower)


