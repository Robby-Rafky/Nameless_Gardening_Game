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
        self.inv_surface = pygame.Surface((1150, 720))
        self.inv_information_surface = pygame.Surface((520, 720))
        self.font = pygame.font.SysFont("Arial", 20)
        self.scroll_offset = 10
        self.scroll_percentage = 0
        self.mouse_valid = False
        self.inv_cursor_x, self.inv_cursor_y = None, None
        self.inv_clicked_x, self.inv_clicked_y = None, None
        self.inv_index = None
        self.clicked_inv_item = None

    def inv_menu_events(self):
        if self.clicked_inv_item is not None:
            if self.place_item_button.button_event_check(self.game.mouse_position):
                self.game.inventory_handler.add_item(self.clicked_inv_item)
            if self.sell_item_button.button_event_check(self.game.mouse_position):
                self.game.inventory_handler.remove_item(self.clicked_inv_item)

    def draw_inv(self):
        self.inv_surface.fill(MENU_GREY)
        x = -1
        y = 0
        for item in self.game.inventory_handler.inventory:
            if item is not None:
                x += 1
                if x == 11:
                    y += 1
                    x = 0
                if item == self.clicked_inv_item:
                    pygame.draw.rect(self.inv_surface, D_GREY, (10 + x * 100,
                                                              self.scroll_offset + y * 100,
                                                              100, 100))
                pygame.draw.rect(self.inv_surface, GREY, (10 + x * 100,
                                                          self.scroll_offset + y * 100,
                                                          100, 100), 2)
                stack = self.font.render(str(item.stack_size), True, BLACK)
                item.draw_item(60 + x * 100, 50 + self.scroll_offset + y * 100, self.inv_surface, 1)
                self.inv_surface.blit(stack, (105 - stack.get_width() + x * 100,
                                              100 - stack.get_height() +
                                              self.scroll_offset + y * 100))

        pygame.draw.rect(self.inv_surface, BLACK, (0, 0, 1150, 720), 4)
        pygame.draw.rect(self.inv_surface, L_GREY, (1120, 10, 20, 700), 0)
        pygame.draw.rect(self.inv_surface, GREY, (1120, 10 + self.scroll_percentage * 640, 20, 60), 0)

    def draw_inv_overlay(self):
        if self.mouse_valid:
            if self.inv_cursor_x == self.inv_clicked_x and self.inv_cursor_y == self.inv_clicked_y:
                colour = D_GREY
            else:
                colour = MENU_GREY
            pygame.draw.rect(self.inv_surface, colour, (self.inv_cursor_x * 100,
                                                           self.scroll_offset + self.inv_cursor_y * 100 - 10,
                                                           120, 120))
            pygame.draw.rect(self.inv_surface, BLACK, (self.inv_cursor_x * 100,
                                                       self.scroll_offset + self.inv_cursor_y * 100 - 10,
                                                       120, 120), 2)
            self.game.inventory_handler.inventory[self.inv_index].draw_item(60 + self.inv_cursor_x * 100,
                                                                            50 + self.scroll_offset + self.inv_cursor_y
                                                                            * 100, self.inv_surface, 1.2)
            self.font = pygame.font.SysFont("Arial", 24)
            stack = self.font.render(str(self.game.inventory_handler.inventory[self.inv_index].stack_size), True, BLACK)
            self.inv_surface.blit(stack, (115 - stack.get_width() + self.inv_cursor_x * 100,
                                          110 - stack.get_height() + self.scroll_offset + self.inv_cursor_y * 100))
            self.font = pygame.font.SysFont("Arial", 20)

    def mouse_within_inv_limits(self):
        if (0 <= self.game.mouse_position[0] - 110 <= 1100 and
                1 <= self.game.mouse_position[1] - 200 <= self.game.inventory_handler.visible_size_full):
            self.inv_cursor_x = int((self.game.mouse_position[0] - 111) / 100)
            self.inv_cursor_y = int((self.game.mouse_position[1] - 191 - self.scroll_offset) / 100)
            self.inv_index = self.inv_cursor_x + self.inv_cursor_y * 11
            if self.inv_index < self.game.inventory_handler.inventory_size:
                if pygame.mouse.get_pressed()[0]:
                    self.clicked_inv_item = self.game.inventory_handler.inventory[self.inv_index]
                    self.inv_clicked_x = self.inv_cursor_x
                    self.inv_clicked_y = self.inv_cursor_y
                self.mouse_valid = True
            else:
                self.mouse_valid = False
        else:
            self.mouse_valid = False

    def side_inventory_panel(self):
        self.place_item_button.update_button(self.place_item_button.text, GREY)
        self.place_item_button.pack_button(self.inv_information_surface)

        self.sell_item_button.update_button(self.sell_item_button.text, GREY)
        self.sell_item_button.pack_button(self.inv_information_surface)

        self.item_view.update_button_multiline(self.clicked_inv_item.item_description, MENU_GREY)
        self.item_view.pack_button(self.inv_information_surface)


    def draw_inv_information(self):
        self.inv_information_surface.fill(MENU_GREY)

        if self.clicked_inv_item is not None:
            self.side_inventory_panel()
        self.draw_inv_overlay()

        pygame.draw.rect(self.inv_information_surface, BLACK, (0, 0, 520, 720), 4)
        self.surface.blit(self.inv_surface, (40, 40))
        self.surface.blit(self.inv_information_surface, (1240, 40))
