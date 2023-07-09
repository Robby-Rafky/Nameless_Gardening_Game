# All external libraries
import math
import pygame
from random import randint
from datetime import timedelta

# General Colours
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
# Tier colours
tier_colours = {
    0: (160, 159, 161),
    1: GREEN,
    2: (35, 68, 219),
    3: (80, 28, 201),
    4: (217, 168, 9),
    5: (220, 129, 247),
    6: (14, 215, 237),
    7: (184, 0, 0)
}

# Menu/UI Colours
MENU_GREY = (194, 194, 194)
GROWTH_COLOUR = (18, 184, 0)
YIELD_COLOUR = (150, 184, 0)
LIFESPAN_COLOUR = (135, 71, 209)
VALUE_COLOUR = (232, 184, 102)
RES_COLOUR = (122, 200, 204)
SKILL_ALLOCATED = (255, 236, 5)
SKILL_HOVER = (237, 231, 121)
SKILL_AVAILABLE = (122, 118, 50)
SKILL_UNAVAILABLE = (150, 150, 150)
# Fonts
PIXEL_FONT = "ModernDOS9x16.ttf"


# Global use functions


def clamp(n, upper, lower):
    """Clamps a value between an upper and lower limit.

    Args:
        n (float): The value to clamp.
        upper (float): The upper limit.
        lower (float): The lower limit.

    Returns:
        float: The clamped value.
    """
    return max(min(upper, n), lower)


def chance_to_occur(chance):
    """Determines if an event occurs based on a probability.

    Args:
        chance (float): The probability of the event occurring, range from 0 to 1.

    Returns:
        bool: True if the event occurs, False otherwise.
    """
    return randint(0, 99) < chance


def small_chance_to_occur(chance):
    """Determines if an event occurs based on a small probability.

    Args:
        chance (float): The probability of the event occurring, range from 0 to 1.

    Returns:
        bool: True if the event occurs, False otherwise.
    """
    chance = chance * 1000
    return randint(0, 99999) < chance


def get_time(time):
    """Converts a time value to a human-readable format.

    Args:
        time (int): The time value in seconds.

    Returns:
        str: The formatted time string.
    """
    if time >= 0:
        return str(timedelta(seconds=time))
    else:
        return "Infinite"


def construct_title(item):
    """Constructs a title for an item.

    Args:
        item: The item object.

    Returns:
        str: The constructed title string.
    """
    title = item.type1["type_name"]
    if item.is_pure:
        title = "[Pure] " + title
    else:
        title = title + " " + item.type2["type_name"]
    if item.is_max:
        title = title + " [Max]"
    return title


def calc_stats(flat, mult, flat_2, mult_2):
    """Calculates the stats based on given values.

        Args:
            flat (list): List of flat values.
            mult (list): List of multiplier values.
            flat_2 (list): List of additional flat values.
            mult_2 (list): List of additional multiplier values.

        Returns:
            float: The calculated product of the stats.
        """
    sum_flat = (sum(flat) + sum(flat_2)) / 2
    prod_mult = 1
    for i in range(len(mult)):
        num = (mult[i] + mult_2[i]) / 2
        prod_mult = prod_mult * num

    return sum_flat * prod_mult
