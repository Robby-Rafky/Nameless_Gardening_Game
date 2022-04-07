import pygame

from Menus.baseMenu import Menu
from button import Button
from textBox import TextBox
from useful_functions import *


class ShopMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.currency_text = TextBox(" ", (725, 760), (350, 40), (60, 150), True, True, 22, MENU_GREY)
        self.garden_shop_text = TextBox("Garden Shop", (10, 10), (860, 40), (70, 160), True, True, 26, LIME_GREEN)
        self.expand_v_price = 100
        self.expand_h_price = 100
        self.expand_button_v = Button("Add row (" + str(self.expand_v_price) + " $)",
                                      (20, 60), (380, 40), (70, 160), True, True, 20,
                                      self.afford_colour(self.expand_v_price))
        self.expand_button_h = Button("Add column (" + str(self.expand_h_price) + " $)",
                                      (480, 60), (380, 40), (70, 160), True, True, 20,
                                      self.afford_colour(self.expand_h_price))
        # find a better way to store price info
        self.surface_garden = pygame.Surface((880, 200))

        self.surface_mutate = pygame.Surface((880, 200))

    def afford_colour(self, price):
        if self.game.user.cash >= price:
            return L_ORANGE
        else:
            return RED

    def shop_menu_events(self):
        if self.expand_button_v.button_event(self.game.mouse_position) and self.game.garden_handler.garden.size_y < 9:
            if self.game.user.purchase_check(self.expand_v_price):
                self.game.garden_handler.expand_vertical()
        if self.expand_button_h.button_event(self.game.mouse_position) and self.game.garden_handler.garden.size_x < 15:
            if self.game.user.purchase_check(self.expand_h_price):
                self.game.garden_handler.expand_horizontal()

    def draw_garden_shop(self):
        pygame.draw.rect(self.surface_garden, BLACK, (0, 0, 880, 200), 2)
        self.expand_h_price = self.game.garden_handler.garden.size_y * self.game.garden_handler.garden.size_x * 100
        self.expand_v_price = self.game.garden_handler.garden.size_y * self.game.garden_handler.garden.size_x * 100
        if self.game.garden_handler.garden.size_y < 9:
            self.expand_button_v.update_button("Add row (" + str(self.expand_v_price) + " $)",
                                               self.afford_colour(self.expand_v_price))
        else:
            self.expand_button_v.update_button("Max rows purchased", GREY)

        if self.game.garden_handler.garden.size_x < 15:
            self.expand_button_h.update_button("Add column (" + str(self.expand_h_price) + " $)",
                                               self.afford_colour(self.expand_h_price))
        else:
            self.expand_button_h.update_button("Max columns purchased", GREY)
        self.garden_shop_text.draw_on_surface(self.surface_garden)
        self.expand_button_v.draw_on_surface(self.surface_garden)
        self.expand_button_h.draw_on_surface(self.surface_garden)

    def draw_shop_items(self):
        self.surface_garden.fill(MENU_GREY)
        self.surface_mutate.fill(MENU_GREY)

        self.draw_garden_shop()

        self.currency_text.update_textbox("Cash: " + str(self.game.user.cash) + " $", MENU_GREY)
        self.currency_text.draw_on_surface(self.surface)
        self.surface.blit(self.surface_garden, (10, 10))
        self.surface.blit(self.surface_mutate, (910, 10))
