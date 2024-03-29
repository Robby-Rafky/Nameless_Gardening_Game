from Menus.baseMenu import Menu
from datetime import timedelta
from button import Button
from textBox import TextBox
from useful_functions import *


class StatsMenu(Menu):
    """
    A class representing the stats menu.

    The StatsMenu class extends the base Menu class and provides functionality for displaying and interacting with the
    stats menu. It allows the player to view information about plant types, such as primary and secondary stats,
    resistance, mutation recipe, and images.

    Attributes:
        game (Game): The game instance.
        primary_title (TextBox): The text box for displaying the title of the primary stats section.
        primary_info (TextBox): The text box for displaying the primary stats information.
        primary_desc (TextBox): The text box for displaying the description of the primary stats.
        secondary_title (TextBox): The text box for displaying the title of the secondary stats section.
        secondary_info (TextBox): The text box for displaying the secondary stats information.
        secondary_desc (TextBox): The text box for displaying the description of the secondary stats.
        seed_title (TextBox): The text box for displaying the title of the pure seed section.
        plant_title (TextBox): The text box for displaying the title of the pure plant section.
        type_title (TextBox): The text box for displaying the title of the plant type.
        recipe_title (TextBox): The text box for displaying the title of the mutation recipe section.
        recipe_details (TextBox): The text box for displaying the details of the mutation recipe.
        error_text (TextBox): The text box for displaying error messages.
        unlock_details (TextBox): The text box for displaying the details of how to unlock a plant type.
        mutation_info (TextBox): The text box for displaying the chance to mutate information.
        res_title (TextBox): The text box for displaying the title of the resistance section.
        font (Font): The font used for rendering text.
        scroll_offset (int): The vertical scroll offset for the plant type buttons.
        button_collection (list): A list of all plant type buttons.
        type_list_surface (Surface): The surface for rendering the plant type buttons.
        type_information_surface (Surface): The surface for rendering the plant type information.
        clicked_item (dict): The currently clicked plant type.
        types (dict): The data for all plant types.

    Methods:
        __init__(self, game): Initializes the StatsMenu instance.
        stats_menu_events(self): Handles the events in the stats menu.
        construct_type_info(self, switch): Constructs the information for the plant type based on the given switch.
        draw_primary_info(self): Draws the primary stats information on the stats menu surface.
        draw_secondary_info(self): Draws the secondary stats information on the stats menu surface.
        draw_resistance_info(self): Draws the resistance information on the stats menu surface.
        draw_image_info(self): Draws the image information on the stats menu surface.
        draw_recipe_info(self): Draws the mutation recipe information on the stats menu surface.
        draw_plant_type_info(self): Draws the plant type information on the stats menu surface.
        draw_plant_types(self): Draws the plant type buttons on the stats menu surface.
    """

    def __init__(self, game):
        """
        Initialize the StatsMenu instance.

        Args:
            game (Game): The game instance.
        """
        Menu.__init__(self, game, MENU_GREY)
        self.primary_title = TextBox("Primary", (300, 60), (1160, 40), True, False, 26)
        self.primary_info = TextBox(" ", (890, 110), (570, 180), True, False, 24)
        self.primary_desc = TextBox(" ", (300, 110), (580, 180), True, False, 24)
        self.secondary_title = TextBox("Secondary", (300, 300), (1160, 40), True, False, 26)
        self.secondary_info = TextBox(" ", (890, 350), (570, 180), True, False, 24)
        self.secondary_desc = TextBox(" ", (300, 350), (580, 180), True, False, 24)
        self.seed_title = TextBox("Pure Seed", (70, 320), (160, 40), False, True, 24, MENU_GREY)
        self.plant_title = TextBox("Pure Plant", (70, 470), (160, 40), False, True, 24, MENU_GREY)
        self.type_title = TextBox(" ", (10, 10), (1450, 40), True, False, 26)
        self.recipe_title = TextBox(" ", (10, 60), (280, 40), True, False, 26)
        self.recipe_details = TextBox(" ", (10, 100), (280, 210), True, False, 24)
        self.error_text = TextBox(" ", (500, 550), (450, 80), False, True, 38)
        self.unlock_details = TextBox(" ", (500, 630), (450, 40), False, True, 26)
        self.mutation_info = TextBox(" ", (300, 540), (1160, 40), True, False, 26, MENU_GREY)
        self.res_title = TextBox("Resistance", (10, 690), (300, 40), False, False, 26, MENU_GREY)
        self.font = pygame.font.Font(PIXEL_FONT, 24)
        self.scroll_offset = 0
        self.button_collection = []
        self.type_list_surface = pygame.Surface((300, 780))
        self.type_information_surface = pygame.Surface((1470, 780))
        self.clicked_item = None
        self.types = self.game.data_handler.plant_types
        counter = 0
        current_tier = -1
        for item in self.types:
            # --------------------------------------- TESTING
            self.types[item]["is_unlocked"] = True
            # ---------------------------------------
            position = (current_tier + 1) * 30 + counter * 50
            if self.types[item]["tier"] == current_tier:
                self.button_collection.append(Button(item, (0, position), (300, 50), (
                    70, 160), True, True, 26, MENU_GREY))
            else:
                current_tier += 1
                self.button_collection.append(
                    Button("Tier " + str(current_tier), (0, position), (300, 30), (70, 160), True, True, 26, BLACK))
                self.button_collection[counter + current_tier].text_colour = WHITE
                self.button_collection[counter + current_tier].update_textbox(str(current_tier), BLACK)
                self.button_collection.append(Button(item, (0, position + 30), (300, 50), (
                    70, 160), True, True, 26, MENU_GREY))
            counter += 1
        self.scroll_max = (len(self.button_collection) * 50 - current_tier * 20) - 800

    def stats_menu_events(self):
        """Handle the events in the stats menu."""
        for item in self.button_collection:
            if item.button_event(self.game.mouse_pos) and item.text.split()[0] != "Tier":
                self.clicked_item = self.types[item.text]

    def construct_type_info(self, switch):
        """
        Construct the information for the plant type based on the given switch.

        Args:
            switch (int): The switch value (0 for primary stats, 1 for secondary stats).

        Returns:
            list: The list of strings containing the plant type information.
        """
        a = self.clicked_item
        return ["Adult age time: " + get_time(a["adult_age"][switch]) + "[x" + str(a["adult_mult"][switch]) + "]",
                "Death age time: " + get_time(a["death_age"][switch]) + "[x" + str(a["death_mult"][switch]) + "]",
                "Growth rate: x" + str(a["growth_mult"][switch]),
                "Yields: " + str(int(a["yield_mult"][switch])) + " seeds",
                str(int(100 * (a["yield_mult"][switch] % 1))) + "% chance to gain an additional seed",
                "Seeds sell for: $" + str(a["value_base"][switch]) + "[x" + str(a["value_mult"][switch]) + "]",
                "Extractable Essence: " + str(a["essence_base"][switch]) + " units"]

    def draw_primary_info(self):
        """Draw the primary stats information on the stats menu surface."""
        self.primary_desc.update_textbox_multiline(self.clicked_item["primary_desc"], MENU_GREY)

        self.primary_info.update_textbox_multiline(self.construct_type_info(0), MENU_GREY)

        self.primary_info.draw_on_surface(self.type_information_surface)
        self.primary_desc.draw_on_surface(self.type_information_surface)
        self.primary_title.draw_on_surface(self.type_information_surface)

    def draw_secondary_info(self):
        """Draw the secondary stats information on the stats menu surface."""
        self.secondary_desc.update_textbox_multiline(self.clicked_item["second_desc"], MENU_GREY)

        self.secondary_info.update_textbox_multiline(self.construct_type_info(1), MENU_GREY)

        self.secondary_info.draw_on_surface(self.type_information_surface)
        self.secondary_desc.draw_on_surface(self.type_information_surface)
        self.secondary_title.draw_on_surface(self.type_information_surface)

    def draw_resistance_info(self):
        """Draw the resistance information on the stats menu surface."""
        self.res_title.update_textbox("Resistance", tier_colours[self.clicked_item["tier"]])
        self.res_title.draw_on_surface(self.type_information_surface)
        res_clamp = clamp(self.clicked_item["resistance"], self.clicked_item["resistance_cap"], 0)
        res_info = self.font.render(str(res_clamp) + "/" + str(self.clicked_item["resistance_cap"]), True, BLACK)
        pygame.draw.rect(self.type_information_surface, RES_COLOUR,
                         (10, 730, 1450 * res_clamp / self.clicked_item["resistance_cap"], 40))
        pygame.draw.rect(self.type_information_surface, MENU_GREY, (10, 730, 1450, 40), 0)
        pygame.draw.rect(self.type_information_surface, BLACK, (10, 730, 1450, 40), 2)
        self.type_information_surface.blit(res_info, (735 - res_info.get_width(), 740,
                                                      res_info.get_width(), res_info.get_height()))

    def draw_image_info(self):
        """Draw the image information on the stats menu surface."""
        pygame.draw.rect(self.type_information_surface, MENU_GREY, (60, 320, 180, 140), 0)
        pygame.draw.rect(self.type_information_surface, MENU_GREY, (60, 470, 180, 140), 0)

        # self.clicked_item.draw_seed(110, 370, self.type_information_surface)

        self.seed_title.update_textbox("Pure Seed", MENU_GREY)
        self.plant_title.update_textbox("Pure Plant", MENU_GREY)
        self.seed_title.draw_on_surface(self.type_information_surface)

        pygame.draw.rect(self.type_information_surface, BLACK, (60, 320, 180, 140), 2)
        self.plant_title.draw_on_surface(self.type_information_surface)
        pygame.draw.rect(self.type_information_surface, BLACK, (60, 470, 180, 140), 2)

    def draw_recipe_info(self):
        """Draw the mutation recipe information on the stats menu surface."""
        if self.clicked_item["mutation_recipe"][0] is not None:
            self.recipe_details.update_textbox_multiline(self.clicked_item["mutation_recipe"], MENU_GREY)
            self.recipe_title.update_textbox("Recipe", MENU_GREY)
            self.mutation_info.update_textbox("Chance to mutate: " + str(self.clicked_item["mutation_chance"][0]) + "%",
                                              MENU_GREY)
        else:
            self.recipe_details.update_textbox(" ", GREY)
            self.recipe_title.update_textbox("No Recipe", MENU_GREY)
            self.mutation_info.update_textbox("Cannot be mutated into", MENU_GREY)

        self.mutation_info.draw_on_surface(self.type_information_surface)
        self.recipe_title.draw_on_surface(self.type_information_surface)
        self.recipe_details.draw_on_surface(self.type_information_surface)

    def draw_plant_type_info(self):
        """Draw the plant type information on the stats menu surface."""
        self.type_information_surface.fill(MENU_GREY)
        if self.clicked_item is not None:
            self.type_information_surface.fill(tier_colours[self.clicked_item["tier"]])
            if self.clicked_item["is_unlocked"]:
                self.type_title.update_textbox(self.clicked_item["type_name"], MENU_GREY)
                tier_title = self.font.render("Tier " + str(self.clicked_item["tier"]), True, BLACK)
                tier_title.get_rect().right = 150

                self.draw_primary_info()
                self.draw_secondary_info()
                self.draw_recipe_info()
                self.draw_resistance_info()
                self.draw_image_info()

                self.type_title.draw_on_surface(self.type_information_surface)
                self.type_information_surface.blit(tier_title, (1450 - tier_title.get_width(), 20))
            else:
                pygame.draw.rect(self.type_information_surface, GREY, (0, 0, 1470, 780), 0)
                self.error_text.update_textbox("Locked", GREY)
                self.unlock_details.update_textbox("Unlocked via: Mutation", GREY)
                self.error_text.draw_on_surface(self.type_information_surface)
                self.unlock_details.draw_on_surface(self.type_information_surface)
        else:
            self.unlock_details.update_textbox("Select a plant species", MENU_GREY)
            self.unlock_details.draw_on_surface(self.type_information_surface)

        pygame.draw.rect(self.type_information_surface, BLACK, (0, 0, 1470, 780), 2)
        self.surface.blit(self.type_information_surface, (320, 10))

    def draw_plant_types(self):
        """Draw the plant type buttons on the stats menu surface."""
        self.type_list_surface.fill(MENU_GREY)
        for item in self.button_collection:
            if item.text.split()[0] == "Tier":
                item.update_button_position(item.text, BLACK, item.x, item.y_init - self.scroll_offset)
            elif self.types[item.text] == self.clicked_item:
                item.update_button_position(item.text, GREY, item.x, item.y_init - self.scroll_offset)
            else:
                item.update_button_position(item.text, MENU_GREY, item.x, item.y_init - self.scroll_offset)
            item.draw_on_surface(self.type_list_surface)
        pygame.draw.rect(self.type_list_surface, BLACK, (0, 0, 300, 780), 2)
        self.surface.blit(self.type_list_surface, (10, 10))
