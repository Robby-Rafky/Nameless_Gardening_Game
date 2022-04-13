from useful_functions import *
from Items.seedGen import create_seed_image


class PlantType:
    def __init__(self, type_name, base_starting_age, base_adult_age, base_death_age, base_mutation_chance,
                 base_yield, base_value, mult_adult_age, mult_death_age, mult_growth_speed,
                 mult_yield, mult_value, mutation_recipe, colour, is_unlocked,
                 primary_description, secondary_description):
        self.type_name = type_name
        self.base_starting_age = base_starting_age
        self.base_adult_age = base_adult_age
        self.base_death_age = base_death_age
        self.mutation_chance = base_mutation_chance
        self.base_yield = base_yield
        self.base_value = base_value
        self.mult_adult_age = mult_adult_age
        self.mult_death_age = mult_death_age
        self.mult_growth_speed = mult_growth_speed
        self.mult_yield = mult_yield
        self.mult_value = mult_value
        self.recipe = mutation_recipe
        self.colour = colour
        self.is_unlocked = is_unlocked
        self.primary_desc = primary_description
        self.secondary_desc = secondary_description
        self.pure_seed_image = create_seed_image(self.colour)

    def draw_seed(self, pos_x, pos_y, surface):
        surface.blit(self.pure_seed_image, (pos_x, pos_y))
