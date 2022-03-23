from useful_functions import *
from Items.item1 import Item1
from Items.item2 import Item2
from Items.item3 import Item3


class InventoryHandler:

    def __init__(self, game):
        self.game = game
        self.inventory = [Item1(), Item2(), Item3()]
        # update this
        self.inventory_size = len(self.inventory)

    def update_inventory(self):
        self.inventory_size = len(self.inventory)

    def mouse_within_inventory_limits(self):
        if 110 <= self.game.mouse_position[0] <= 1210 and 200 <= self.game.mouse_position[1] <= 900:
            # many clamps + add scroll offset to gridx/y
            pass
