import pygame
from useful_functions import *


class User:
    """Represents a user in the game.

    The User class represents a user in the game, including their cash balance and methods for purchasing items.

    Attributes:
        cash (int): The cash balance of the user.

    Methods:
        __init__():
            Initializes a new instance of the User class.
        purchase_check(cost):
            Checks if the user can make a purchase based on the cost of the item.

    """

    def __init__(self):
        """
        Initializes a new instance of the User class.
        """
        self.cash = 1000000

    def purchase_check(self, cost):
        """
        Checks if the user can make a purchase based on the cost of the item.

        Args:
            cost (int): The cost of the item.

        Returns:
            bool: True if the user can make the purchase, False otherwise.
        """
        if self.cash - cost < 0:
            return False
        else:
            self.cash -= cost
            return True

