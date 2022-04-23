from Menus.baseMenu import Menu
from UserData.ShopItem import ShopItem
from textBox import TextBox
from useful_functions import *
from Items.plantItem import PlantItem
from Garden.PlantManipulation.mutation import Mutator


class ShopMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.currency_text = TextBox(" ", (725, 760), (350, 40), True, True, 22, MENU_GREY)

        self.garden_shop_text = TextBox("Garden Shop", (10, 10), (860, 40), True, True, 26, LIME_GREEN)
        self.buy_expand_garden_v = ShopItem("Add row", (20, 60), (380, 40), (70, 160), 100)
        self.buy_expand_garden_h = ShopItem("Add column", (480, 60), (380, 40), (70, 160), 100)

        self.seed_shop_text = TextBox("Seeds Shop", (10, 10), (1760, 40), True, True, 26, LIME_GREEN)
        self.buy_verdant_seed = ShopItem("Verdant Seed", (10, 170), (260, 40), (70, 370), 0,
                                         PlantItem(0, 0, 0, 0, "Verdant", "Verdant"))

        self.manip_shop_text = TextBox("Plant Manipulation Shop", (10, 10), (860, 40), True, True, 26, L_BLUE)
        self.buy_mutator = ShopItem("Mutator", (60, 60), (350, 40), (970, 160), 100)
        self.buy_cross_pollinator = ShopItem("Cross Pollinator", (470, 60), (350, 40), (970, 160), 100)
        self.buy_genetic_combiner = ShopItem("Genetic Combiner", (60, 140), (350, 40), (970, 160), 100)

        # find a better way to store price info
        self.surface_garden = pygame.Surface((880, 200))
        self.surface_seed = pygame.Surface((1780, 220))
        self.surface_mutate = pygame.Surface((880, 200))

    def shop_expand_column_event(self):
        if self.buy_expand_garden_h.button_event(self.game.mouse_pos) and self.game.garden_handler.garden.size_x < 15:
            if self.game.user.purchase_check(self.buy_expand_garden_h.price):
                self.game.garden_handler.expand_horizontal()
                self.buy_expand_garden_h.update_price(self.game.garden_handler.garden.size_y
                                                      * self.game.garden_handler.garden.size_x * 100)
                self.buy_expand_garden_v.update_price(self.game.garden_handler.garden.size_y
                                                      * self.game.garden_handler.garden.size_x * 100)
        elif self.game.garden_handler.garden.size_x == 15:
            self.buy_expand_garden_h.update_price()

    def shop_expand_row_event(self):
        if self.buy_expand_garden_v.button_event(self.game.mouse_pos) and self.game.garden_handler.garden.size_y < 9:
            if self.game.user.purchase_check(self.buy_expand_garden_v.price):
                self.game.garden_handler.expand_vertical()
                self.buy_expand_garden_h.update_price(self.game.garden_handler.garden.size_y
                                                      * self.game.garden_handler.garden.size_x * 100)
                self.buy_expand_garden_v.update_price(self.game.garden_handler.garden.size_y
                                                      * self.game.garden_handler.garden.size_x * 100)
        elif self.game.garden_handler.garden.size_y == 9:
            self.buy_expand_garden_v.update_price()

    def permanent_shop_plot_events(self):
        if self.buy_verdant_seed.button_event(self.game.mouse_pos):
            if self.game.user.purchase_check(self.buy_verdant_seed.price):
                self.game.inventory_handler.add_item(self.buy_verdant_seed.item)

        if self.buy_mutator.button_event(self.game.mouse_pos):
            if self.game.user.purchase_check(self.buy_mutator.price):
                self.game.user.cash += self.buy_mutator.price
                self.game.garden_handler.planting = Mutator(0, 0, self.game, 1)
                self.game.menu_handler.current_menu = None

        if self.buy_genetic_combiner.button_event(self.game.mouse_pos):
            if self.game.user.purchase_check(self.buy_genetic_combiner.price):
                print("comb")

        if self.buy_cross_pollinator.button_event(self.game.mouse_pos):
            if self.game.user.purchase_check(self.buy_cross_pollinator.price):
                print("pol")

    def shop_menu_events(self):
        self.shop_expand_column_event()
        self.shop_expand_row_event()
        self.permanent_shop_plot_events()

    def draw_garden_shop(self):
        pygame.draw.rect(self.surface_garden, BLACK, (0, 0, 880, 200), 2)

        self.buy_expand_garden_h.update_shop(self.game.user.cash)
        self.buy_expand_garden_v.update_shop(self.game.user.cash)

        self.garden_shop_text.draw_on_surface(self.surface_garden)
        self.buy_expand_garden_v.draw_shop_on_surface(self.surface_garden)
        self.buy_expand_garden_h.draw_shop_on_surface(self.surface_garden)

    def draw_seed_shop(self):
        pygame.draw.rect(self.surface_seed, BLACK, (0, 0, 1780, 220), 2)

        self.buy_verdant_seed.update_shop(self.game.user.cash)

        self.seed_shop_text.draw_on_surface(self.surface_seed)
        self.buy_verdant_seed.draw_shop_on_surface(self.surface_seed)

    def draw_mutate_shop(self):
        pygame.draw.rect(self.surface_mutate, BLACK, (0, 0, 880, 200), 2)

        self.buy_mutator.update_shop(self.game.user.cash)
        self.buy_genetic_combiner.update_shop(self.game.user.cash)
        self.buy_cross_pollinator.update_shop(self.game.user.cash)

        self.buy_mutator.draw_on_surface(self.surface_mutate)
        self.buy_cross_pollinator.draw_on_surface(self.surface_mutate)
        self.buy_genetic_combiner.draw_on_surface(self.surface_mutate)
        self.manip_shop_text.draw_on_surface(self.surface_mutate)

    def draw_shop_items(self):
        self.surface_garden.fill(MENU_GREY)
        self.surface_mutate.fill(MENU_GREY)
        self.surface_seed.fill(MENU_GREY)

        self.draw_garden_shop()
        self.draw_seed_shop()
        self.draw_mutate_shop()

        self.currency_text.update_textbox("Cash: " + str(self.game.user.cash) + " $", MENU_GREY)
        self.currency_text.draw_on_surface(self.surface)
        self.surface.blit(self.surface_garden, (10, 10))
        self.surface.blit(self.surface_seed, (10, 220))
        self.surface.blit(self.surface_mutate, (910, 10))
