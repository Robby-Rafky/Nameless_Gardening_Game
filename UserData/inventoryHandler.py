import random

from useful_functions import *
from Items.plantItem import PlantItem
from Items.plantSpecies import *
from Items.item2 import Item2


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
        self.inventory.append(PlantItem(0, 0, 0, 0, 0, "Verdant", "Programmed"))
        self.inventory.append(PlantItem(4, 0, 9, 3, 5, "Crimson", "Crystalline"))
        self.inventory.append(PlantItem(1, 0, 9, 3, 5, "Verdant", "Radioactive"))
        self.inventory.append(PlantItem(2, 1, 3, 3, 5, "Crystalline", "Explosive"))
        self.inventory.append(PlantItem(3, 0, 9, 4, 3, "Decaying", "Programmed"))
        self.inventory.append(PlantItem(2, 3, 6, 3, 9, "Eternal", "Deadly"))
        self.inventory.append(PlantItem(4, 3, 5, 9, 3, "Steel", "Hollow"))
        self.inventory.append(PlantItem(2, 3, 4, 3, 3, "Endothermic", "Exothermic"))
        # for _ in range(200):
        #     self.inventory.append(PlantItem(0,0,0,0,0, "Verdant", "Verdant"))

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

    def get_item_title(self, item_index):
        # pull a title for each item
        return "Item info"

    def get_item_description_1(self, item_index):
        if isinstance(self.inventory[item_index], PlantItem):
            return species_primary[self.inventory[item_index].plant_type_1]
        else:
            return [" "]

    def get_item_description_2(self, item_index):
        if isinstance(self.inventory[item_index], PlantItem):
            return species_secondary[self.inventory[item_index].plant_type_2]
        else:
            return [" "]

    def get_item_description_3(self, item_index):
        if isinstance(self.inventory[item_index], PlantItem):
            return self.inventory[item_index].item_stats_description
        else:
            return [" "]

