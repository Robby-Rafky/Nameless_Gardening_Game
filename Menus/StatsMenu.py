from Menus.baseMenu import Menu
from datetime import timedelta
from button import Button
from textBox import TextBox
from useful_functions import *
from Garden.Plants.plantSpecies import plant_species


class StatsMenu(Menu):

    def __init__(self, game):
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
        counter = 0
        current_tier = -1
        for item in plant_species:
            # --------------------------------------- TESTING
            plant_species[item].is_unlocked = True
            # ---------------------------------------
            position = (current_tier + 1) * 30 + counter * 50
            if plant_species[item].tier == current_tier:
                self.button_collection.append(Button(item, (0, position), (300, 50), (
                    70, 160), True, True, 26, MENU_GREY))
            else:
                current_tier += 1
                self.button_collection.append(
                    Button("Tier " + str(current_tier), (0,  position), (300, 30), (70, 160), True, True, 26, BLACK))
                self.button_collection[counter + current_tier].text_colour = WHITE
                self.button_collection[counter + current_tier].update_textbox(str(current_tier), BLACK)
                self.button_collection.append(Button(item, (0, position + 30), (300, 50), (
                    70, 160), True, True, 26, MENU_GREY))
            counter += 1
        self.scroll_max = (len(self.button_collection) * 50 - current_tier * 20) - 800

    def stats_menu_events(self):
        for item in self.button_collection:
            if item.button_event(self.game.mouse_pos) and item.text.split()[0] != "Tier":
                self.clicked_item = plant_species[item.text]

    def draw_primary_info(self):
        self.primary_desc.update_textbox_multiline(self.clicked_item.primary_desc, MENU_GREY)

        adult_age = str(timedelta(seconds=self.clicked_item.base_adult[0]))
        adult_mult = str(self.clicked_item.mult_adult[0])
        death_age = str(timedelta(seconds=self.clicked_item.base_death[0]))
        death_mult = str(self.clicked_item.mult_death[0])
        value = str(self.clicked_item.base_value[0])
        value_mult = str(self.clicked_item.mult_value[0])
        yield_base = str(int(self.clicked_item.base_yield[0] / 100))
        yield_add = str(self.clicked_item.base_yield[0] % 100)
        yield_mult = str(self.clicked_item.mult_yield[0])
        a_eff = str(self.clicked_item.ability_eff[0])

        self.primary_info.update_textbox_multiline(["Adult age time: " + adult_age + "[x" + adult_mult + "]",
                                                    "Death age time: " + death_age + "[x" + death_mult + "]",
                                                    "Growth rate: x" + str(self.clicked_item.mult_rate[0]),
                                                    "Yields: " + yield_base + "[x" + yield_mult + "] seeds",
                                                    yield_add + "% chance to gain an additional seed",
                                                    "Seeds sell for: $" + value + "[x" + value_mult + "]",
                                                    "Ability Potency: " + a_eff + "%"],
                                                   MENU_GREY)

        self.primary_info.draw_on_surface(self.type_information_surface)
        self.primary_desc.draw_on_surface(self.type_information_surface)
        self.primary_title.draw_on_surface(self.type_information_surface)

    def draw_secondary_info(self):
        self.secondary_desc.update_textbox_multiline(self.clicked_item.secondary_desc, MENU_GREY)

        adult_age = str(timedelta(seconds=self.clicked_item.base_adult[1]))
        adult_mult = str(self.clicked_item.mult_adult[1])
        death_age = str(timedelta(seconds=self.clicked_item.base_death[1]))
        death_mult = str(self.clicked_item.mult_death[1])
        value = str(self.clicked_item.base_value[1])
        value_mult = str(self.clicked_item.mult_value[1])
        yield_base = str(int(self.clicked_item.base_yield[1] / 100))
        yield_add = str(self.clicked_item.base_yield[1] % 100)
        yield_mult = str(self.clicked_item.mult_yield[1])
        a_eff = str(self.clicked_item.ability_eff[1])

        self.secondary_info.update_textbox_multiline(["Adult age time: " + adult_age + "[x" + adult_mult + "]",
                                                      "Death age time: " + death_age + "[x" + death_mult + "]",
                                                      "Growth rate: x" + str(self.clicked_item.mult_rate[0]),
                                                      "Yields: " + yield_base + "[x" + yield_mult + "] seeds",
                                                      yield_add + "% chance to gain an additional seed",
                                                      "Seeds sell for: $" + value + "[x" + value_mult + "]",
                                                      "Ability Potency: " + a_eff + "%"],
                                                     MENU_GREY)

        self.secondary_info.draw_on_surface(self.type_information_surface)
        self.secondary_desc.draw_on_surface(self.type_information_surface)
        self.secondary_title.draw_on_surface(self.type_information_surface)

    def draw_resistance_info(self):
        self.res_title.draw_on_surface(self.type_information_surface)
        res_clamp = clamp(self.clicked_item.res, self.clicked_item.res_cap, 0)
        res_info = self.font.render(str(res_clamp) + "/" + str(self.clicked_item.res_cap), True, BLACK)
        pygame.draw.rect(self.type_information_surface, RES_COLOUR,
                         (10, 730, 1450 * res_clamp / self.clicked_item.res_cap, 40))
        pygame.draw.rect(self.type_information_surface, BLACK, (10, 730, 1450, 40), 2)
        self.type_information_surface.blit(res_info, (735 - res_info.get_width(), 740,
                                                      res_info.get_width(), res_info.get_height()))

    def draw_image_info(self):
        self.clicked_item.draw_seed(110, 370, self.type_information_surface)
        self.seed_title.draw_on_surface(self.type_information_surface)
        pygame.draw.rect(self.type_information_surface, BLACK, (60, 320, 180, 140), 2)
        self.plant_title.draw_on_surface(self.type_information_surface)
        pygame.draw.rect(self.type_information_surface, BLACK, (60, 470, 180, 140), 2)

    def draw_recipe_info(self):
        if len(self.clicked_item.recipe) != 0:
            self.recipe_details.update_textbox_multiline(self.clicked_item.recipe, MENU_GREY)
            self.recipe_title.update_textbox("Recipe", MENU_GREY)
        else:
            self.recipe_details.update_textbox(" ", GREY)
            self.recipe_title.update_textbox("No Recipe", MENU_GREY)

        self.recipe_title.draw_on_surface(self.type_information_surface)
        self.recipe_details.draw_on_surface(self.type_information_surface)

    def draw_misc_info(self):
        self.mutation_info.update_textbox("Mutation Chance: " + str(self.clicked_item.mutation_chance) + "%", MENU_GREY)
        self.mutation_info.draw_on_surface(self.type_information_surface)

    def draw_plant_type_info(self):
        self.type_information_surface.fill(MENU_GREY)
        if self.clicked_item is not None:
            if self.clicked_item.is_unlocked:
                self.type_title.update_textbox(self.clicked_item.type_name, MENU_GREY)
                tier_title = self.font.render("Tier " + str(self.clicked_item.tier), True, BLACK)
                tier_title.get_rect().right = 150

                self.draw_primary_info()
                self.draw_secondary_info()
                self.draw_misc_info()
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
        self.type_list_surface.fill(MENU_GREY)
        for item in self.button_collection:
            if item.text.split()[0] == "Tier":
                item.update_button_position(item.text, BLACK, item.x, item.y_init - self.scroll_offset)
            elif plant_species[item.text] == self.clicked_item:
                item.update_button_position(item.text, GREY, item.x, item.y_init - self.scroll_offset)
            else:
                item.update_button_position(item.text, MENU_GREY, item.x, item.y_init - self.scroll_offset)
            item.draw_on_surface(self.type_list_surface)
        pygame.draw.rect(self.type_list_surface, BLACK, (0, 0, 300, 780), 2)
        self.surface.blit(self.type_list_surface, (10, 10))
