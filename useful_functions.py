# All external libraries
import math
import pygame

# Colour definitions
BLACK = (0, 0, 0)
BLUE = (4, 18, 105)
L_BLUE = (125, 173, 250)
GREY = (105, 105, 105)
L_GREY = (160, 160, 160)
D_GREY = (87, 87, 87)
GREEN = (40, 87, 23)
LIME_GREEN = (4, 212, 84)
BROWN = (51, 30, 4)
WHITE = (255, 255, 255)
RED = (117, 13, 13)
L_ORANGE = (235, 169, 94)

MENU_GREY = (194, 194, 194)
GROWTH_COLOUR = (18, 184, 0)
YIELD_COLOUR = (150, 184, 0)
LIFESPAN_COLOUR = (135, 71, 209)
VALUE_COLOUR = (232, 184, 102)
RES_COLOUR = (122, 200, 204)
# Fonts
PIXEL_FONT = "ModernDOS9x16.ttf"


# Global use functions


def clamp(n, upper, lower):
    return max(min(upper, n), lower)


def construct_title(item):
    title = item.type1
    if item.is_pure:
        title = "[Pure] " + title
    else:
        title = title + " " + item.type2
    if item.is_max:
        title = title + " [Max]"
    return title


# Takes a list of values, averages them on a per-value basis, sums the flat values, multiplies the multipliers
# and returns the product.
def calc_stats(flat, mult, flat_2, mult_2):
    sum_flat = (sum(flat) + sum(flat_2))/2
    prod_mult = 1
    for i in range(len(mult)):
        num = (mult[i] + mult_2[i])/2
        prod_mult = prod_mult * num

    return sum_flat * prod_mult
