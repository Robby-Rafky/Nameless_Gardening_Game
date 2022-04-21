from useful_functions import *


class Targeter:
    def __init__(self, game):
        self.game = game
        self.limit_x = 0
        self.limit_y = 0

    def within_limits(self, x, y):
        if 0 <= x <= self.limit_x and 0 <= y <= self.limit_y:
            return True
        else:
            return False

    def target_area(self, radius, x, y):
        targets = []
        diameter = 1 + radius * 2
        for a in range(diameter):
            for b in range(diameter):
                coord_x = (x - radius) + a
                coord_y = (y - radius) + b
                if self.within_limits(coord_x, coord_y):
                    if coord_y != y or coord_x != x:
                        targets.append((coord_x, coord_y))
        return targets
