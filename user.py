import pygame


class User:

    def __init__(self):
        self.cash = 10000

    def purchase_check(self, cost):
        if self.cash - cost < 0:
            return False
        else:
            self.cash -= cost
            print(self.cash)
            return True
