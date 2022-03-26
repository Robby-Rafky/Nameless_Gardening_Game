# All external libraries
import math
import pygame

# Colour definitions
BLACK = (0, 0, 0)
BLUE = (4, 18, 105)
GREY = (105, 105, 105)
L_GREY = (160, 160, 160)
D_GREY = (87, 87, 87)
GREEN = (40, 87, 23)
BROWN = (51, 30, 4)
WHITE = (255, 255, 255)
RED = (117, 13, 13)
L_ORANGE = (235, 169, 94)
MENU_GREY = (194, 194, 194)
# Fonts
PIXEL_FONT = "pixelFont.ttf"
# Global use functions


def clamp(n, upper, lower):
    return max(min(upper, n), lower)


