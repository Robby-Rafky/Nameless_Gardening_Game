from useful_functions import *
from Menus.Menu1 import InventoryMenu
from Menus.Menu2 import ShopMenu
from Menus.Menu3 import SkillTreeMenu
from Menus.Menu4 import Menu4
from Menus.Menu5 import StatsMenu


class MenuHandler:

    def __init__(self, game):
        self.game = game
        self.current_menu = None
        self.inventory_menu = InventoryMenu(self.game)
        self.shop_menu = ShopMenu(self.game)
        self.skill_tree_menu = SkillTreeMenu(self.game)
        self.menu_4 = Menu4(self.game)
        self.stats_menu = StatsMenu(self.game)

    def current_menu_event_check(self):
        # event checking in each specific menu
        if self.current_menu == "Inventory":
            self.inventory_menu.inventory_menu_events()
        if self.current_menu == "Shop":
            self.shop_menu.shop_menu_events()
        if self.current_menu == "SkillTree":
            self.skill_tree_menu.skill_tree_menu_events()
        if self.current_menu == "4":
            self.menu_4.menu4_menu_events()
        if self.current_menu == "Stats":
            self.stats_menu.stats_menu_events()

    def close_current_menu(self):
        self.current_menu = None

    def show_current_menu(self):
        if self.current_menu == "Inventory":
            self.inventory_menu.show_menu()
        if self.current_menu == "Shop":
            self.shop_menu.show_menu()
        if self.current_menu == "SkillTree":
            self.skill_tree_menu.show_menu()
        if self.current_menu == "4":
            self.menu_4.show_menu()
        if self.current_menu == "Stats":
            self.stats_menu.show_menu()
