from Menus.baseMenu import Menu
from textBox import TextBox
from button import Button
from useful_functions import *


class InventoryMenu(Menu):
    """
    A class representing the inventory menu.

    Attributes:
        game (Game): The game instance.
        place_item_button (Button): The button for placing an item from the inventory.
        sell_item_button (Button): The button for selling an item from the inventory.
        sell_price (TextBox): The text box for displaying the sell price of the selected item.
        item_title (TextBox): The text box for displaying the title of the selected item.
        item_data_view (TextBox): The text box for displaying the data of the selected item.
        inv_surface (Surface): The surface for drawing the inventory grid.
        inv_information_surface (Surface): The surface for drawing the information of the selected item.
        font (Font): The font used for rendering text.
        scroll_offset (int): The vertical scroll offset of the inventory grid.
        scroll_percentage (float): The scroll position percentage of the inventory grid.
        mouse_valid (bool): True if the mouse is within the inventory limits, False otherwise.
        inv_cursor_x (int): The x-coordinate of the cursor in the inventory grid.
        inv_cursor_y (int): The y-coordinate of the cursor in the inventory grid.
        inv_clicked_x (int): The x-coordinate of the clicked item in the inventory grid.
        inv_clicked_y (int): The y-coordinate of the clicked item in the inventory grid.
        inv_index (int): The index of the cursor position in the inventory.
        clicked_index (int): The index of the clicked item in the inventory.
        clicked_item (PlantItem): The clicked item in the inventory.

    Methods:
        __init__(self, game): Initialize the InventoryMenu instance.
        inv_menu_events(self): Handle the events in the inventory menu.
        draw_inv(self): Draw the inventory grid on the inventory surface.
        draw_inv_overlay(self): Draw the overlay for the selected inventory item.
        mouse_within_inv_limits(self): Check if the mouse is within the inventory limits.
        draw_inv_buttons(self): Draw the buttons for placing and selling items in the inventory.
        draw_single_stat(self, stat, value, pos_y, colour): Draw a single statistic on the inventory information surface.
        draw_stats_view(self): Draw the statistics view for the selected inventory item.
        draw_seed_data(self): Draw the seed data for the selected inventory item.
        side_inventory_panel(self): Draw the side panel of the inventory menu.
        draw_inv_information(self): Draw the inventory grid, overlay, and information on the inventory surface.
    """

    def __init__(self, game):
        """Initialize the InventoryMenu instance.

            Args:
                game (Game): The game instance.
        """
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
        """Handle the events in the inventory menu."""
        if self.clicked_item is not None:
            if self.place_item_button.button_event(self.game.mouse_pos):
                self.game.garden_handler.planting = self.clicked_item
                self.game.garden_handler.garden.clicked_plot = None
                self.game.menu_handler.current_menu = None
                self.game.garden_handler.garden.clicked_plot_index = None
            if self.sell_item_button.button_event(self.game.mouse_pos):
                self.game.inventory_handler.remove_item(self.clicked_item)

    def draw_inv(self):
        """Draw the inventory grid on the inventory surface."""
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
        """Draw the overlay for the selected inventory item."""
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
        """Check if the mouse is within the inventory limits."""
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
        """Draw the buttons for placing and selling items in the inventory."""
        self.place_item_button.update_button(self.place_item_button.text, GREY)
        self.place_item_button.draw_on_surface(self.inv_information_surface)

        self.sell_item_button.update_button(self.sell_item_button.text, GREY)
        self.sell_item_button.draw_on_surface(self.inv_information_surface)

    def draw_single_stat(self, stat, value, pos_y, colour):
        """Draw a single statistic on the inventory information surface.

            Args:
                stat (str): The name of the statistic.
                value (int): The value of the statistic.
                pos_y (int): The y-coordinate position to draw the statistic.
                colour (tuple): The color of the statistic bar.
        """
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
        """Draw the statistics view for the selected inventory item."""
        self.draw_single_stat("Growth", self.clicked_item.stat_growth, 175, GROWTH_COLOUR)
        self.draw_single_stat("Seed Yield", self.clicked_item.stat_yield, 205, YIELD_COLOUR)
        self.draw_single_stat("Lifespan", self.clicked_item.stat_lifespan, 235, LIFESPAN_COLOUR)
        self.draw_single_stat("Value", self.clicked_item.stat_value, 265, VALUE_COLOUR)
        self.draw_single_stat("Resistivity", int(self.clicked_item.res), 295, RES_COLOUR)

    def draw_seed_data(self):
        """Draw the seed data for the selected inventory item."""
        final_adult = "Fully grown in: " + get_time(self.clicked_item.final_adult)
        final_death = "Full lifespan: " + get_time(self.clicked_item.final_death)
        if self.clicked_item.final_rate > 1:
            final_rate = "Grows: " + str(self.clicked_item.final_rate) + "x faster"
        elif self.clicked_item.final_rate == 1.0:
            final_rate = "Grows: Default Speed"
        else:
            final_rate = "Grows: " + str(self.clicked_item.final_rate) + "x slower"
        final_value = str(self.clicked_item.final_value) + " $"
        final_ability_eff = "Extractable Essence: " + str(self.clicked_item.final_essence) + " units"
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
        """Draw the side panel of the inventory menu."""
        self.clicked_item.draw_seed(220, 70, self.inv_information_surface)

        self.item_title.update_textbox(construct_title(self.clicked_item), MENU_GREY)
        self.item_title.draw_on_surface(self.inv_information_surface)

        self.draw_seed_data()
        self.draw_inv_buttons()
        self.draw_stats_view()

    def draw_inv_information(self):
        """Draw the inventory grid, overlay, and information on the inventory surface."""
        self.inv_information_surface.fill(MENU_GREY)

        if self.clicked_item is not None:
            self.side_inventory_panel()
        self.draw_inv_overlay()

        pygame.draw.rect(self.inv_information_surface, BLACK, (0, 0, 520, 720), 4)
        self.surface.blit(self.inv_surface, (40, 40))
        self.surface.blit(self.inv_information_surface, (1240, 40))
