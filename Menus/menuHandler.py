from useful_functions import *
from Menus.InventoryMenu import InventoryMenu
from Menus.ShopMenu import ShopMenu
from Menus.SkillsMenu import SkillTreeMenu
from Menus.Menu4 import Menu4
from Menus.StatsMenu import StatsMenu


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
            self.inventory_menu.surface.fill(self.inventory_menu.background_colour)
            self.inventory_menu.draw_inventory()
            self.inventory_menu.draw_inventory_information()
            self.inventory_menu.show_menu()
        if self.current_menu == "Shop":
            self.shop_menu.surface.fill(self.shop_menu.background_colour)
            self.shop_menu.show_menu()
        if self.current_menu == "SkillTree":
            self.skill_tree_menu.surface.fill(self.skill_tree_menu.background_colour)
            self.skill_tree_menu.show_menu()
        if self.current_menu == "4":
            self.menu_4.surface.fill(self.menu_4.background_colour)
            self.menu_4.show_menu()
        if self.current_menu == "Stats":
            self.stats_menu.surface.fill(self.stats_menu.background_colour)
            self.stats_menu.show_menu()

    def scroll_menu(self, scroll):
        if self.current_menu == "Inventory":
            if self.game.inventory_handler.inventory_size >= 77:
                scroll_max = -int(math.ceil(self.game.inventory_handler.inventory_size/11) - 7) * 100 + 10

                self.inventory_menu.scroll_offset += scroll * 20
                self.inventory_menu.scroll_offset = clamp(self.inventory_menu.scroll_offset, 10, scroll_max)

                self.inventory_menu.scroll_percentage = clamp((self.inventory_menu.scroll_offset/scroll_max), 1, 0)

        if self.current_menu == "Shop":
            pass
        if self.current_menu == "SkillTree":
            pass
        if self.current_menu == "4":
            pass
        if self.current_menu == "Stats":
            pass
