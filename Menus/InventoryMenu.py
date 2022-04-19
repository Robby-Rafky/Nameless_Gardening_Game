from Menus.baseMenu import Menu
from textBox import TextBox
from button import Button
from useful_functions import *
from Garden.Plants.plantSpecies import plant_species as ps
from datetime import timedelta


class InventoryMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.place_item_button = Button("Place", (20, 650), (200, 50), (1300, 190), True, True, 30, GREY)
        self.sell_item_button = Button("Sell", (300, 650), (200, 50), (1300, 190), True, True, 30, GREY)
        self.sell_price = TextBox(" ", (10, 600), (500, 40), True, True, 24, MENU_GREY)
        self.item_title = TextBox(" ", (10, 10), (500, 40), True, True, 26, MENU_GREY)
        self.item_data_view = TextBox(" ", (10, 330), (500, 160), True, False, 24, MENU_GREY)
        self.inv_surface = pygame.Surface((1150, 720))
        self.inv_information_surface = pygame.Surface((520, 720))
        self.font = pygame.font.Font(PIXEL_FONT, 24)
        self.scroll_offset = 10
        self.scroll_percentage = 0
        self.mouse_valid = False
        self.inv_cursor_x, self.inv_cursor_y = None, None
        self.inv_clicked_x, self.inv_clicked_y = None, None
        self.inv_index, self.clicked_index = None, None
        self.clicked_item = None

    def inv_menu_events(self):
        if self.clicked_item is not None:
            if self.place_item_button.button_event(self.game.mouse_pos):
                self.game.garden_handler.planting = self.clicked_item
                self.game.garden_handler.garden.clicked_plot = None
                self.game.menu_handler.current_menu = None
                self.game.garden_handler.garden.clicked_plot_index = None
            if self.sell_item_button.button_event(self.game.mouse_pos):
                self.game.inventory_handler.remove_item(self.clicked_item)

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
                if item == self.clicked_item:
                    pygame.draw.rect(self.inv_surface, D_GREY, (10 + x * 100,
                                                                self.scroll_offset + y * 100,
                                                                100, 100))
                    pygame.draw.rect(self.inv_surface, BLACK, (10 + x * 100,
                                                               self.scroll_offset + y * 100,
                                                               100, 100), 2)
                else:
                    pygame.draw.rect(self.inv_surface, GREY, (10 + x * 100,
                                                              self.scroll_offset + y * 100,
                                                              100, 100), 2)
                stack = self.font.render(str(item.stack_size), True, BLACK)
                item.draw_seed(20 + x * 100, 10 + self.scroll_offset + y * 100, self.inv_surface)
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
            self.game.inventory_handler.inventory[self.inv_index].draw_seed(20 + self.inv_cursor_x * 100,
                                                                            10 + self.scroll_offset + self.inv_cursor_y
                                                                            * 100, self.inv_surface)
            stack = self.font.render(str(self.game.inventory_handler.inventory[self.inv_index].stack_size), True, BLACK)
            self.inv_surface.blit(stack, (115 - stack.get_width() + self.inv_cursor_x * 100,
                                          110 - stack.get_height() + self.scroll_offset + self.inv_cursor_y * 100))

    def mouse_within_inv_limits(self):
        if (0 <= self.game.mouse_pos[0] - 110 <= 1100 and
                1 <= self.game.mouse_pos[1] - 200 <= self.game.inventory_handler.visible_size_full):
            self.inv_cursor_x = int((self.game.mouse_pos[0] - 111) / 100)
            self.inv_cursor_y = int((self.game.mouse_pos[1] - 191 - self.scroll_offset) / 100)
            self.inv_index = self.inv_cursor_x + self.inv_cursor_y * 11
            if self.inv_index < self.game.inventory_handler.inventory_size:
                if pygame.mouse.get_pressed()[0]:
                    self.clicked_index = self.inv_index
                    self.clicked_item = self.game.inventory_handler.inventory[self.clicked_index]
                    self.inv_clicked_x = self.inv_cursor_x
                    self.inv_clicked_y = self.inv_cursor_y
                self.mouse_valid = True
            else:
                self.mouse_valid = False
        else:
            self.mouse_valid = False

    def draw_inv_buttons(self):
        self.place_item_button.update_button(self.place_item_button.text, GREY)
        self.place_item_button.draw_on_surface(self.inv_information_surface)

        self.sell_item_button.update_button(self.sell_item_button.text, GREY)
        self.sell_item_button.draw_on_surface(self.inv_information_surface)

    def draw_single_stat(self, stat, value, pos_y, colour):
        pygame.draw.rect(self.inv_information_surface, colour, (10, pos_y, 10 + 490 * value / 100, 30), 0)
        pygame.draw.rect(self.inv_information_surface, BLACK, (10, pos_y, 10 + 490 * value / 100, 30), 1)
        self.inv_information_surface.blit(self.font.render(stat, True, BLACK), (20, pos_y + 5))
        if value == 100:
            value_text = self.font.render("[Max]", True, BLACK)
        else:
            value_text = self.font.render(str(value) + "%", True, BLACK)

        value_text.get_rect().right = 150
        self.inv_information_surface.blit(value_text, (500 - value_text.get_width(), pos_y + 5))

    def draw_stats_view(self):
        self.draw_single_stat("Growth", self.clicked_item.stat_growth, 175, GROWTH_COLOUR)
        self.draw_single_stat("Seed Yield", self.clicked_item.stat_yield, 205, YIELD_COLOUR)
        self.draw_single_stat("Lifespan", self.clicked_item.stat_lifespan, 235, LIFESPAN_COLOUR)
        self.draw_single_stat("Value", self.clicked_item.stat_value, 265, VALUE_COLOUR)
        self.draw_single_stat("Resistivity", int(self.clicked_item.res), 295, RES_COLOUR)

    def draw_seed_data(self):
        final_adult = "Fully grown in: " + str(timedelta(seconds=self.clicked_item.final_adult))
        final_death = "Full lifespan: " + str(timedelta(seconds=self.clicked_item.final_death))
        if self.clicked_item.final_rate > 1:
            final_rate = "Grows: " + str(self.clicked_item.final_rate) + "x faster"
        elif self.clicked_item.final_rate == 1.0:
            final_rate = "Grows: Default Speed"
        else:
            final_rate = "Grows: " + str(self.clicked_item.final_rate) + "x slower"
        final_value = str(self.clicked_item.final_value) + " $"
        final_ability_eff = "Ability Potency: " + str(self.clicked_item.final_ability_eff) + "%"
        final_yield = "Yield: " + str(int(self.clicked_item.final_yield / 100)
                                      ) + " seeds +" + str(round(self.clicked_item.final_yield % 100,
                                                                 1)) + "% for 1 extra"
        self.item_data_view.update_textbox_multiline(["Tier: "+str(self.clicked_item.tier),
                                                      final_adult,
                                                      final_death,
                                                      final_rate,
                                                      final_yield,
                                                      final_ability_eff], MENU_GREY)

        self.sell_price.update_textbox(final_value, MENU_GREY)

        self.sell_price.draw_on_surface(self.inv_information_surface)
        self.item_data_view.draw_on_surface(self.inv_information_surface)

    def side_inventory_panel(self):
        self.clicked_item.draw_seed(220, 70, self.inv_information_surface)

        self.item_title.update_textbox(construct_title(self.clicked_item), MENU_GREY)
        self.item_title.draw_on_surface(self.inv_information_surface)

        self.draw_seed_data()
        self.draw_inv_buttons()
        self.draw_stats_view()

    def draw_inv_information(self):
        self.inv_information_surface.fill(MENU_GREY)

        if self.clicked_item is not None:
            self.side_inventory_panel()
        self.draw_inv_overlay()

        pygame.draw.rect(self.inv_information_surface, BLACK, (0, 0, 520, 720), 4)
        self.surface.blit(self.inv_surface, (40, 40))
        self.surface.blit(self.inv_information_surface, (1240, 40))
