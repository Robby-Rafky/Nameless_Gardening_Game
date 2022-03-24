from useful_functions import *
from Items.plantItem import PlantItem
from Items.item2 import Item2
from Items.item3 import Item3


class InventoryHandler:

    def __init__(self, game):
        self.game = game
        self.inventory = [Item2() for _ in range(120)]

        self.inventory_size = None
        self.visible_size_full = None
        self.visible_size_limit = None
        self.inventory.append(PlantItem(4, 0, 9, 3, 5, "crimson"))
        self.inventory.append(PlantItem(1, 0, 9, 3, 5, "verdant"))
        self.inventory.append(PlantItem(2, 0, 3, 3, 5, "crystalline"))
        self.inventory.append(PlantItem(2, 0, 9, 3, 3, "decaying"))

        self.update_inventory()

    def update_inventory(self):
        self.inventory_size = len(self.inventory)
        self.visible_size_full = clamp(math.ceil(self.inventory_size / 11) * 100, 700, 0)

    def add_item(self, item):
        item_found = False
        for x in self.inventory:
            if x.item_ID == item.item_ID:
                x.stack_size += 1
                item_found = True
        if not item_found:
            self.inventory.append(item)
        self.update_inventory()

    def remove_item(self, item):
        item.stack_size -= 1
        if item.stack_size == 0:
            self.inventory.remove(item)
            self.game.menu_handler.inventory_menu.clicked_inv_item = None
        self.update_inventory()





