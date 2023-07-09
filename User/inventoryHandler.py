import random

from useful_functions import *
from Items.plantItem import PlantItem



class InventoryHandler:
    """
    Handles the inventory functionality in the game.

    The InventoryHandler class manages the player's inventory, including adding and removing items, updating inventory size, and retrieving item information.

    Attributes:
        game (Game): The game instance.
        inventory (list): The list of items in the inventory.
        inventory_size (int): The total size of the inventory.
        visible_size_full (int): The full visible size of the inventory.
        visible_size_limit (int): The limited visible size of the inventory.

    Methods:
        __init__(game):
            Initializes a new instance of the InventoryHandler class.
        starting_inventory():
            Adds initial items to the inventory for testing purposes.
        update_inventory():
            Updates the inventory size and visible size.
        add_item(item):
            Adds an item to the inventory.
        remove_item(item):
            Removes an item from the inventory.
        get_item_title(item_index):
            Retrieves the title of an item based on its index.

    """
    def __init__(self, game):
        """
        Initializes a new instance of the InventoryHandler class.

        Args:
            game (Game): The game instance.
        """
        self.game = game
        self.inventory = []

        self.inventory_size = None
        self.visible_size_full = None
        self.visible_size_limit = None

        self.starting_inventory()
        self.update_inventory()

    # test stuff
    def starting_inventory(self):
        """
        Adds initial items to the inventory for testing purposes.

        Args:
            None

        Returns:
            None
        """
        self.inventory.append(PlantItem(0, 0, 0, 0, "Verdant", "Verdant", self.game))
        self.inventory.append(PlantItem(10, 10, 10, 10, "Verdant", "Verdant", self.game))
        self.inventory.append(PlantItem(20, 20, 20, 20, "Verdant", "Verdant", self.game))
        self.inventory.append(PlantItem(30, 30, 30, 30, "Verdant", "Verdant", self.game))
        self.inventory.append(PlantItem(40, 40, 40, 40, "Verdant", "Verdant", self.game))
        self.inventory.append(PlantItem(50, 50, 50, 50, "Verdant", "Verdant", self.game))
        self.inventory.append(PlantItem(60, 60, 60, 60, "Vermilion", "Vermilion", self.game))
        self.inventory.append(PlantItem(70, 70, 70, 70, "Inked", "Inked", self.game))
        self.inventory.append(PlantItem(80, 80, 80, 80, "Pale", "Pale", self.game))
        self.inventory.append(PlantItem(90, 90, 90, 90, "Azure", "Azure", self.game))
        for _ in range(10):
            self.add_item(PlantItem(100, 100, 100, 100, "Verdant", "Verdant", self.game))
            self.add_item(PlantItem(100, 100, 100, 100, "Azure", "Azure", self.game))
            self.add_item(PlantItem(100, 100, 100, 100, "Vermilion", "Vermilion", self.game))

        # for _ in range(200):
        #     self.inventory.append(PlantItem(0, 0, 0, 0, "Verdant", "Verdant", self.game))
        # pass

    def update_inventory(self):
        """Updates the inventory size and visible size."""
        self.inventory_size = len(self.inventory)
        self.visible_size_full = clamp(math.ceil(self.inventory_size / 11) * 100, 700, 0)

    def add_item(self, item):
        """
        Adds an item to the inventory.

        Args:
            item (PlantItem): The item to be added.
        """
        item_found = False
        for x in self.inventory:
            if x.item_ID == item.item_ID:
                x.stack_size += 1
                item_found = True
        if not item_found:
            self.inventory.append(item)
        self.update_inventory()

    def remove_item(self, item):
        """
        Removes an item from the inventory.

        Args:
            item (PlantItem): The item to be removed.
        """
        item.stack_size -= 1
        if item.stack_size == 0:
            self.inventory.remove(item)
            self.game.menu_handler.inventory_menu.clicked_item = None
        self.update_inventory()

    def get_item_title(self, item_index):
        """NOT FINISHED
        Retrieves the title of an item based on its index.

        Args:
            item_index (int): The index of the item.

        Returns:
            str: The title of the item.
        """
        return "Item info"
