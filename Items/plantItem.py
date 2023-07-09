from useful_functions import *
from Items.seedGen import create_seed_image


class PlantItem:
    """
    A class representing a plant item.

    Attributes:
        game (Game): The game instance.
        type1 (dict): The data dictionary for the first plant type.
        type2 (dict): The data dictionary for the second plant type.
        colour (tuple): The colour of the plant item.
        stat_growth (int): The growth stat of the plant item.
        stat_yield (int): The seed yield stat of the plant item.
        stat_lifespan (int): The lifespan stat of the plant item.
        stat_value (int): The value stat of the plant item.
        tier (int): The tier of the plant item.
        item_ID (str): The unique ID of the plant item.
        stack_size (int): The number of items in the stack.
        is_pure (bool): True if the plant item is a pure type, False otherwise.
        is_max (bool): True if the plant item has maximum stats, False otherwise.
        res (float): The resistivity stat of the plant item.
        final_adult (int): The final adult age of the plant item's seed.
        final_death (int): The final death age of the plant item's seed.
        final_rate (float): The final growth rate of the plant item's seed.
        final_yield (float): The final seed yield of the plant item's seed.
        final_value (int): The final value of the plant item's seed.
        final_essence (int): The final essence value of the plant item's seed.
        seed_image (Surface): The seed image of the plant item.

    Methods:
        __init__(self, growth, seed_yield, lifespan, value, plant_type_1, plant_type_2, game): Initialize the PlantItem instance.
        draw_seed(self, pos_x, pos_y, surface): Draw the seed image of the plant item on the specified surface.
        calc_seed_final(self): Calculate the final stats of the plant item's seed based on its growth, seed yield, lifespan, and value stats.
    """

    def __init__(self, growth, seed_yield, lifespan, value, plant_type_1, plant_type_2, game):
        """Initialize the PlantItem instance.

        Args:
            growth (int): The growth stat of the plant item.
            seed_yield (int): The seed yield stat of the plant item.
            lifespan (int): The lifespan stat of the plant item.
            value (int): The value stat of the plant item.
            plant_type_1 (str): The type name of the first plant type.
            plant_type_2 (str): The type name of the second plant type.
            game (Game): The game instance.
        """
        self.game = game
        self.type1 = self.game.data_handler.plant_types[plant_type_1]
        self.type2 = self.game.data_handler.plant_types[plant_type_2]
        self.colour = self.type1["colour"]
        self.stat_growth = growth
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.tier = max(self.type1["tier"], self.type2["tier"])
        self.item_ID = (plant_type_1 + str(self.stat_growth) + str(self.stat_yield) +
                        str(self.stat_lifespan) + str(self.stat_value) + plant_type_2)
        self.stack_size = 1
        if plant_type_1 == plant_type_2:
            self.is_pure = True
        else:
            self.is_pure = False
        if growth + seed_yield + lifespan + value == 400:
            self.is_max = True
        else:
            self.is_max = False
        self.res = (growth + seed_yield + lifespan + value) / 4
        self.final_adult = None
        self.final_death = None
        self.final_rate = None
        self.final_yield = None
        self.final_value = None
        self.final_essence = None
        self.calc_seed_final()
        self.seed_image = create_seed_image(self.colour)

    def draw_seed(self, pos_x, pos_y, surface):
        """Draw the seed image of the plant item on the specified surface.

        Args:
            pos_x (int): The x-coordinate of the position to draw the seed image.
            pos_y (int): The y-coordinate of the position to draw the seed image.
            surface (Surface): The surface on which to draw the seed image.
        """
        surface.blit(self.seed_image, (pos_x, pos_y))

    def calc_seed_final(self):
        """Calculate the final stats of the plant item's seed based on its growth,
        seed yield, lifespan, and value stats."""
        a = self.type1
        b = self.type2
        c = self.game.data_handler.garden_globals["stat"]["stat_magnitude"]
        self.final_adult = calc_stats([a["adult_age"][0]], [a["adult_mult"][0]],
                                      [b["adult_age"][1]], [b["adult_mult"][1]])
        self.final_death = calc_stats([a["death_age"][0]], [a["death_mult"][0]],
                                      [b["death_age"][1]], [b["death_mult"][1]]) * (
                1+(4 * c * self.stat_lifespan / 100))
        self.final_rate = calc_stats([1], [a["growth_mult"][0]], [1], [b["growth_mult"][1]]) * (
                1 + (2 * c * self.stat_growth/100))
        self.final_yield = 100 * calc_stats([1], [a["yield_mult"][0]], [1], [b["yield_mult"][1]]) * (
                1+(2 * c * self.stat_yield/100))
        self.final_value = calc_stats([a["value_base"][0]], [a["value_mult"][0]],
                                      [b["value_base"][1]], [b["value_mult"][1]]) * (
                1+(4 * c * self.stat_value/100))
        self.final_essence = calc_stats([a["essence_base"][0]], [1], [b["essence_base"][1]], [1])

        self.final_yield = round(self.final_yield, 1)
        self.final_essence = int(self.final_essence)
        self.final_value = int(self.final_value)
        self.final_adult = int(self.final_adult)
        self.final_death = int(self.final_death)
        self.final_rate = round(self.final_rate, 2)
