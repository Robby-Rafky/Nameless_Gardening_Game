from useful_functions import *
from Menus.InventoryMenu import InventoryMenu
from Menus.ShopMenu import ShopMenu
from Menus.SkillsMenu import SkillTreeMenu
from Menus.CraftingMenu import Menu4
from Menus.StatsMenu import StatsMenu


class MenuHandler:
    """Handles menus in the game.

    The MenuHandler class manages the various menus available in the game, including the inventory menu, shop menu,
    skill tree menu, crafting menu, and stats menu. It provides methods to handle events in the current menu, close
    the current menu, show the current menu on the game screen, and scroll/zoom the current menu.

    Attributes:
        game (Game): The game instance.
        current_menu (str or None): The currently active menu. Can be "Inventory", "Shop", "SkillTree", "Crafting",
            "Stats", or None if no menu is currently active.
        inventory_menu (InventoryMenu): The inventory menu instance.
        shop_menu (ShopMenu): The shop menu instance.
        skill_tree_menu (SkillTreeMenu): The skill tree menu instance.
        menu_4 (Menu4): The crafting menu instance.
        stats_menu (StatsMenu): The stats menu instance.

    Methods:
        __init__(self, game): Initialize a MenuHandler object.
        current_menu_event_check(self): Check for events in the current menu and handle them accordingly.
        close_current_menu(self): Close the current menu.
        show_current_menu(self): Display the current menu on the game screen.
        scroll_menu(self, scroll, zoom=0, x=0, y=0): Scroll or zoom the current menu based on the given parameters.
    """

    def __init__(self, game):
        """Initialize a MenuHandler object.

        Args:
            game (Game): The game instance.
        """
        self.game = game
        self.current_menu = None
        self.inventory_menu = InventoryMenu(self.game)
        self.shop_menu = ShopMenu(self.game)
        self.skill_tree_menu = SkillTreeMenu(self.game)
        self.menu_4 = Menu4(self.game)
        self.stats_menu = StatsMenu(self.game)

    def current_menu_event_check(self):
        """Check for events in the current menu and handle them accordingly."""
        if self.current_menu == "Inventory":
            self.inventory_menu.inv_menu_events()
        if self.current_menu == "Shop":
            self.shop_menu.shop_menu_events()
        if self.current_menu == "SkillTree":
            self.skill_tree_menu.skill_tree_menu_events()
        if self.current_menu == "Crafting":
            self.menu_4.menu4_menu_events()
        if self.current_menu == "Stats":
            self.stats_menu.stats_menu_events()

    def close_current_menu(self):
        """Close the current menu."""
        self.current_menu = None

    def show_current_menu(self):
        """Display the current menu on the game screen."""
        if self.current_menu == "Inventory":
            self.inventory_menu.surface.fill(self.inventory_menu.background_colour)
            self.inventory_menu.mouse_within_inv_limits()
            self.inventory_menu.draw_inv()
            self.inventory_menu.draw_inv_information()
            self.inventory_menu.show_menu()
        if self.current_menu == "Shop":
            self.shop_menu.surface.fill(self.shop_menu.background_colour)
            self.shop_menu.draw_shop_items()
            self.shop_menu.show_menu()
        if self.current_menu == "SkillTree":
            self.skill_tree_menu.surface.fill(self.skill_tree_menu.background_colour)
            self.skill_tree_menu.draw_skill_tree()
            self.skill_tree_menu.show_menu()
        if self.current_menu == "Crafting":
            self.menu_4.surface.fill(self.menu_4.background_colour)
            self.menu_4.show_menu()
        if self.current_menu == "Stats":
            self.stats_menu.surface.fill(self.stats_menu.background_colour)
            self.stats_menu.draw_plant_type_info()
            self.stats_menu.draw_plant_types()
            self.stats_menu.show_menu()
        if self.current_menu is not None:
            self.game.garden_handler.planting = None

    def scroll_menu(self, scroll, zoom=0, x=0, y=0):
        """Scroll or zoom the current menu based on the given parameters.

        Args:
            scroll (int): The scroll value (-1 for scrolling up, 1 for scrolling down).
            zoom (int, optional): The zoom value (-1 for zooming out, 1 for zooming in). Defaults to 0.
            x (int, optional): The x-coordinate for scrolling or zooming. Defaults to 0.
            y (int, optional): The y-coordinate for scrolling or zooming. Defaults to 0.
        """
        if self.current_menu == "Inventory":
            if 110 <= self.game.mouse_pos[0] <= 1250:
                if self.game.inventory_handler.inventory_size >= 77:
                    scroll_max = -(math.ceil(self.game.inventory_handler.inventory_size/11) - 7) * 100 + 10

                    self.inventory_menu.scroll_offset += scroll * 20
                    self.inventory_menu.scroll_offset = clamp(self.inventory_menu.scroll_offset, 10, scroll_max)

                    self.inventory_menu.scroll_percentage = clamp((self.inventory_menu.scroll_offset/scroll_max), 1, 0)

        if self.current_menu == "Shop":
            pass
        if self.current_menu == "SkillTree":
            if 100 <= self.game.mouse_pos[0] <= 1820 and 190 <= self.game.mouse_pos[1] <= 910:
                a = self.skill_tree_menu
                a.scroll_x -= 1/a.zoom_scale * x
                a.scroll_y -= 1/a.zoom_scale * y
                a.zoom_scale += zoom * 0.05
                a.zoom_scale = clamp(a.zoom_scale, 2, 0.05)

        if self.current_menu == "Crafting":
            pass
        if self.current_menu == "Stats":
            if self.game.mouse_pos[0] <= 370:
                self.stats_menu.scroll_offset -= scroll * 20
                self.stats_menu.scroll_offset = clamp(self.stats_menu.scroll_offset, self.stats_menu.scroll_max, 0)
