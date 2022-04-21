import random

from useful_functions import *
from Items.plantItem import PlantItem
from Garden.Plants.plantSpecies import plant_species


class InventoryHandler:
    def __init__(self, game):
        self.game = game
        self.inventory = []

        self.inventory_size = None
        self.visible_size_full = None
        self.visible_size_limit = None

        self.starting_inventory()
        self.update_inventory()

    # test stuff
    def starting_inventory(self):
        self.inventory.append(PlantItem(0, 0, 0, 0, "Verdant", "Verdant"))
        self.inventory.append(PlantItem(10, 10, 10, 10, "Verdant", "Verdant"))
        self.inventory.append(PlantItem(20, 20, 20, 20, "Programmed", "Verdant"))
        self.inventory.append(PlantItem(30, 30, 30, 30, "Hollow", "Hollow"))
        self.inventory.append(PlantItem(40, 40, 40, 40, "Lunar", "Solar"))
        self.inventory.append(PlantItem(50, 50, 50, 50, "Celestial", "Celestial"))
        self.inventory.append(PlantItem(60, 60, 60, 60, "Verdant", "Verdant"))
        self.inventory.append(PlantItem(70, 70, 70, 70, "Verdant", "Verdant"))
        self.inventory.append(PlantItem(80, 80, 80, 80, "Verdant", "Verdant"))
        self.inventory.append(PlantItem(90, 90, 90, 90, "Verdant", "Verdant"))
        self.inventory.append(PlantItem(100, 100, 100, 100, "Verdant", "Verdant"))

        # for _ in range(200):
        #     self.inventory.append(PlantItem(0, 0, 0, 0, "Verdant", "Verdant"))
        # pass

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
            self.game.menu_handler.inventory_menu.clicked_item = None
        self.update_inventory()

    def get_item_title(self, item_index):
        # pull a title for each item
        return "Item info"
