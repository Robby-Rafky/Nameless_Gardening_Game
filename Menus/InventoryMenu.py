import pygame

from Menus.baseMenu import Menu
from button import Button
from useful_functions import *


class InventoryMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.place_item_button = Button("Place", (20, 600), (200, 70), (1300, 190), True, True, 30, GREY)
        self.sell_item_button = Button("Sell", (300, 600), (200, 70), (1300, 190), True, True, 30, GREY)
        # fake button, just text, no events
        self.item_view = Button(" ", (10, 10), (500, 580), (1300, 190), True, False, 20, MENU_GREY)
        self.inventory_surface = pygame.Surface((1150, 720))
        self.inventory_information_surface = pygame.Surface((520, 720))
        self.scroll_offset = 10
        self.scroll_percentage = 0

    def inventory_menu_events(self):
        if self.place_item_button.button_event_check(self.game.mouse_position):
            print("place")
        if self.sell_item_button.button_event_check(self.game.mouse_position):
            print("sell")

    def draw_inventory(self):
        self.inventory_surface.fill(MENU_GREY)

        x = -1
        y = 0
        for item in self.game.inventory_handler.inventory:
            if item is not None:
                x += 1
                if x == 11:
                    y += 1
                    x = 0
                pygame.draw.rect(self.inventory_surface, GREY, (10 + x * 100,
                                                                self.scroll_offset + y * 100,
                                                                100, 100), 2)
                item.draw_item(60 + x * 100, 50 + self.scroll_offset + y * 100, self.inventory_surface)
        pygame.draw.rect(self.inventory_surface, BLACK, (0, 0, 1150, 720), 4)

        pygame.draw.rect(self.inventory_surface, LIGHT_GREY, (1120, 10, 20, 700), 0)
        pygame.draw.rect(self.inventory_surface, GREY, (1120, 10 + self.scroll_percentage * 640, 20, 60), 0)
        self.surface.blit(self.inventory_surface, (40, 40))

    def draw_inventory_information(self):
        self.inventory_information_surface.fill(MENU_GREY)

        self.place_item_button.update_button(self.place_item_button.text, GREY)
        self.place_item_button.pack_button(self.inventory_information_surface)

        self.sell_item_button.update_button(self.sell_item_button.text, GREY)
        self.sell_item_button.pack_button(self.inventory_information_surface)

        self.item_view.update_button(self.item_view.text, MENU_GREY)
        self.item_view.pack_button(self.inventory_information_surface)

        pygame.draw.rect(self.inventory_information_surface, BLACK, (0, 0, 520, 720), 4)
        self.surface.blit(self.inventory_information_surface, (1240, 40))
