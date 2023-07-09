from useful_functions import *
from textBox import TextBox
from button import Button
from datetime import timedelta
from Garden.Plants.basePlant import Plant
from Items.plantItem import PlantItem
from Garden.PlantManipulation.mutation import Mutator
from User.ShopItem import ShopItem


class GardenSpace:
    """
    A class representing the garden space in the game.

    Attributes:
        size_x (int): The size of the garden in the x-axis.
        size_y (int): The size of the garden in the y-axis.
        offset_x (int): The x-coordinate offset of the garden space.
        offset_y (int): The y-coordinate offset of the garden space.
        grid_x (int): The current grid x-coordinate.
        grid_y (int): The current grid y-coordinate.
        clicked_plot: The plot that was clicked.
        clicked_plot_index: The index of the clicked plot.
        action_box (TextBox): The text box for displaying action-related information.
        timers_box (TextBox): The text box for displaying timer-related information.
        stats_box (TextBox): The text box for displaying plant statistics.
        info_box (TextBox): The text box for displaying information about the selected plant or mutator.
        harvest_button (Button): The button for harvesting a plant.
        upgrade_button (ShopItem): The button for upgrading a mutator.
        font (pygame.font.Font): The font used for rendering text.
        game (Game): The game instance.
        side_surface (pygame.Surface): The surface for drawing the side information.
        mutator_asset (Mutator): The mutator asset used for displaying mutators on the garden grid.

    Methods:
        __init__(self, game): Initialize the GardenSpace instance.
        draw_base_garden(self): Draw the base garden grid on the game space.
        draw_overlay_garden(self): Draw the overlay on the garden grid indicating the selected plot or the placement of a new plant.
        garden_button_events(self): Handle the button events in the garden space.
        draw_plant_timer(self): Draw the timer for the selected plant indicating the time to adulthood or decay.
        draw_seed_info(self): Draw the information related to the seed being placed in the garden.
        draw_plant_info(self): Draw the information related to the selected plant in the garden.
        draw_single_stat(self, stat, value, pos_y, colour): Draw a single stat bar with its value on the side surface.
        draw_all_stats(self, item): Draw all the stats of the item (seed or plant) on the side surface.
        draw_mutator_info(self, item): Draw the information related to the selected mutator in the garden.
        draw_side_garden_info(self): Draw the side surface of the garden space with all the relevant information.
    """

    def __init__(self, game):
        """Initialize the GardenSpace instance.

        Args:
            game (Game): The game instance.
        """
        self.size_x, self.size_y = 1, 1
        self.offset_x, self.offset_y = None, None
        self.grid_x, self.grid_y = None, None
        self.clicked_plot = None
        self.clicked_plot_index = None
        self.action_box = TextBox(" ", (10, 10), (320, 40), True, True, 20, MENU_GREY)
        self.timers_box = TextBox(" ", (10, 190), (320, 60), True, False, 20, MENU_GREY)
        self.stats_box = TextBox(" ", (10, 420), (320, 120), True, False, 20, MENU_GREY)
        self.info_box = TextBox(" ", (10, 240), (320, 250), True, False, 20, MENU_GREY)
        self.harvest_button = Button("Growing", (180, 550), (150, 40), (1560, 120), True, True, 26, RED)
        self.upgrade_button = ShopItem("Upgrade", (10, 190), (320, 40), (1560, 120), 0)
        self.font = pygame.font.Font(PIXEL_FONT, 20)
        self.game = game
        self.side_surface = pygame.Surface((340, 920))
        self.mutator_asset = Mutator(0, 0, game, 1, False)

    def draw_base_garden(self):
        """Draw the base garden grid on the game space."""
        for x in range(self.size_x):
            for y in range(self.size_y):
                pygame.draw.rect(self.game.game_space, BLACK, (self.offset_x + x * 100,
                                                               self.offset_y + y * 100,
                                                               100, 100), 1)
        pygame.draw.rect(self.game.game_space, BLACK, (20, 120, 1520, 920), 2)

    def draw_overlay_garden(self):
        """Draw the overlay on the garden grid indicating the selected plot or the placement of a new plant."""
        if self.game.garden_handler.mouse_valid:
            pos_x = self.offset_x + self.grid_x * 100
            pos_y = self.offset_y + self.grid_y * 100
            if pygame.mouse.get_pressed()[0] and self.game.menu_handler.current_menu is None:
                if self.game.garden_handler.planting is None:
                    self.clicked_plot = self.game.garden_handler.garden_contents[self.grid_y][self.grid_x]
                    self.clicked_plot_index = [self.grid_x, self.grid_y]
            else:
                pygame.draw.rect(self.game.game_space, GREY, (pos_x, pos_y, 100, 100), 2)
            if self.game.garden_handler.planting is not None:
                if self.game.garden_handler.garden_contents[self.grid_y][self.grid_x] is not None:
                    pygame.draw.rect(self.game.game_space, RED, (pos_x, pos_y, 100, 100), 4)
                else:
                    if isinstance(self.game.garden_handler.planting, Mutator):
                        self.mutator_asset.draw_mutator(self.game.game_space, pos_x, pos_y)
                    pygame.draw.rect(self.game.game_space, LIME_GREEN, (pos_x, pos_y, 100, 100), 2)
        if self.clicked_plot_index is not None:
            pygame.draw.rect(self.game.game_space, WHITE, (self.offset_x + self.clicked_plot_index[0] * 100,
                                                           self.offset_y + self.clicked_plot_index[1] * 100,
                                                           100, 100), 3)

    def garden_button_events(self):
        """Handle the button events in the garden space."""
        if self.harvest_button.button_event(self.game.mouse_pos):
            if isinstance(self.clicked_plot, Plant):
                if self.clicked_plot.is_adult:
                    self.game.garden_handler.harvest_plant(self.clicked_plot, self.clicked_plot_index)
                    self.clicked_plot = None
        if self.upgrade_button.button_event(self.game.mouse_pos):
            if isinstance(self.clicked_plot, Mutator):
                if self.clicked_plot.tier < 7:
                    if self.game.user.purchase_check(self.upgrade_button.price):
                        self.clicked_plot.tier += 1
                        self.clicked_plot.image = self.clicked_plot.create_image()

    def draw_plant_timer(self):
        """Draw the timer for the selected plant indicating the time to adulthood or decay."""
        if self.clicked_plot.is_adult:
            self.timers_box.update_textbox_multiline(["       Dies in: " + self.clicked_plot.get_time_to_death(),
                                                      "Effective time: " + self.clicked_plot.get_time_to_death(True)],
                                                     MENU_GREY)
            self.harvest_button.update_button("Harvest", LIME_GREEN)
        else:
            self.timers_box.update_textbox_multiline(["      Grown in: " + self.clicked_plot.get_time_to_adult(),
                                                      "Effective time: " + self.clicked_plot.get_time_to_adult(True)],
                                                     MENU_GREY)
            self.harvest_button.update_button("Growing", RED)
        self.timers_box.draw_on_surface(self.side_surface)

    def draw_seed_info(self):
        """Draw the information related to the seed being placed in the garden."""
        pygame.draw.rect(self.side_surface, BLACK, (0, 0, 340, 920), 2)
        self.game.garden_handler.planting.draw_seed(130, 90, self.side_surface)
        self.action_box.update_textbox(construct_title(self.game.garden_handler.planting), MENU_GREY)
        self.timers_box.update_textbox("Currently Placing", MENU_GREY)

        self.timers_box.draw_on_surface(self.side_surface)
        self.action_box.draw_on_surface(self.side_surface)

    def draw_plant_info(self):
        """Draw the information related to the selected plant in the garden."""
        self.clicked_plot.draw_plant(self.side_surface, 120, 70)
        pygame.draw.rect(self.side_surface, BLACK, (0, 0, 340, 920), 2)
        self.action_box.update_textbox(construct_title(self.clicked_plot), MENU_GREY)

        self.stats_box.update_textbox_multiline([
            "Growth Rate: " + str(self.clicked_plot.final_rate) + "x",
            "Sell price: " + str(self.clicked_plot.final_value) + " $",
            "Essence: " + str(self.clicked_plot.final_essence) + " units",
            "Yields: " + str(int(self.clicked_plot.final_yield / 100)) + " seeds",
            str(self.clicked_plot.final_yield % 100) + "% for an extra seed"], MENU_GREY)

        self.harvest_button.draw_on_surface(self.side_surface)
        self.stats_box.draw_on_surface(self.side_surface)
        self.action_box.draw_on_surface(self.side_surface)

    def draw_single_stat(self, stat, value, pos_y, colour):
        """Draw a single stat bar with its value on the side surface.

        Args:
            stat (str): The name of the stat.
            value (int): The value of the stat.
            pos_y (int): The y-coordinate position of the stat bar.
            colour (tuple): The color of the stat bar.
        """
        pygame.draw.rect(self.side_surface, colour, (10, pos_y, 10 + 310 * value / 100, 30), 0)
        pygame.draw.rect(self.side_surface, BLACK, (10, pos_y, 10 + 310 * value / 100, 30), 1)
        self.side_surface.blit(self.font.render(stat, True, BLACK), (20, pos_y + 5))
        if value == 100:
            value_text = self.font.render("[Max]", True, BLACK)
        else:
            value_text = self.font.render(str(value) + "%", True, BLACK)

        value_text.get_rect().right = 150
        self.side_surface.blit(value_text, (320 - value_text.get_width(), pos_y + 5))

    def draw_all_stats(self, item):
        """Draw all the stats of the item (seed or plant) on the side surface.

        Args:
            item (PlantItem or Plant): The item to display the stats for.
        """
        pygame.draw.rect(self.side_surface, MENU_GREY, (10, 260, 320, 150), 0)
        self.draw_single_stat("Growth", item.stat_growth, 260, GROWTH_COLOUR)
        self.draw_single_stat("Seed Yield", item.stat_yield, 290, YIELD_COLOUR)
        self.draw_single_stat("Lifespan", item.stat_lifespan, 320, LIFESPAN_COLOUR)
        self.draw_single_stat("Value", item.stat_value, 350, VALUE_COLOUR)
        self.draw_single_stat("Resistivity", int(item.res), 380, RES_COLOUR)
        pygame.draw.rect(self.side_surface, BLACK, (10, 260, 320, 150), 2)

    def draw_mutator_info(self, item):
        """Draw the information related to the selected mutator in the garden.

        Args:
            item (Mutator): The selected mutator instance.
        """
        if item.tier < 7:
            self.action_box.update_textbox("Mutator "+"[Tier "+str(item.tier)+"]", MENU_GREY)
        else:
            self.action_box.update_textbox("Mutator [Max]", MENU_GREY)

        item.draw_mutator(self.side_surface, 120, 70)

        self.upgrade_button.sold_out = False
        self.upgrade_button.update_price(item.get_price())
        self.upgrade_button.update_shop(self.game.user.cash)

        text = ["Currently Mutating:"]
        for outcome in item.can_mutate:
            text.append(outcome)

        self.info_box.update_textbox_multiline(text, MENU_GREY)

        self.info_box.draw_on_surface(self.side_surface)
        self.upgrade_button.draw_on_surface(self.side_surface)
        self.action_box.draw_on_surface(self.side_surface)

    def draw_side_garden_info(self):
        """Draw the side surface of the garden space with all the relevant information."""
        self.side_surface.fill(GREEN)
        if isinstance(self.game.garden_handler.planting, PlantItem):
            self.draw_seed_info()
            self.draw_all_stats(self.game.garden_handler.planting)

        elif isinstance(self.clicked_plot, Plant):
            self.draw_plant_timer()
            self.draw_plant_info()
            self.draw_all_stats(self.clicked_plot)

        elif isinstance(self.clicked_plot, Mutator):
            self.draw_mutator_info(self.clicked_plot)

        self.game.game_space.blit(self.side_surface, (1560, 120))
