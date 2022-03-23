from useful_functions import *
from Items.item1 import Item1
from Items.item2 import Item2
from Items.item3 import Item3


class InventoryHandler:

    def __init__(self, game):
        self.game = game
        self.inventory = [Item1() for _ in range(133)]

        self.inventory_size = None
        self.visible_size_full = None
        self.visible_size_limit = None

        self.update_inventory()

    def update_inventory(self):
        self.inventory_size = len(self.inventory)
        self.visible_size_full = clamp(math.ceil(self.inventory_size / 11) * 100, 700, 0)
        self.visible_size_limit = 100 * (self.inventory_size % 11)




