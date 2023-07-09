from Menus.baseMenu import Menu
from button import Button
from useful_functions import *


class Menu4(Menu):
    """
    A class representing a menu.

    Attributes:
        game (Game): The game instance.
        visible_state (bool): True if the menu is visible, False otherwise.
        surface (Surface): The surface of the menu.
        background_colour (Tuple[int, int, int]): The RGB color value for the menu background.

    Methods:
        __init__(self, game): Initialize a Menu4 object.
        menu4_menu_events(self): Placeholder method for handling menu events.
    """

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)

    def menu4_menu_events(self):
        pass
