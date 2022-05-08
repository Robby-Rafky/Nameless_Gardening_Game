import pygame
from useful_functions import *


class User:

    def __init__(self):
        self.cash = 1000000

    def purchase_check(self, cost):
        if self.cash - cost < 0:
            return False
        else:
            self.cash -= cost
            return True

