from useful_functions import *
from Garden.Plants.plantSpecies import plant_species as ps
from Items.seedGen import create_seed_image
from Garden.gardenGlobals import garden_global as gs


class PlantItem:
    def __init__(self, growth, seed_yield, lifespan, value, plant_type_1, plant_type_2):
        self.colour = ps[plant_type_1].colour
        self.stat_growth = growth
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.type1 = plant_type_1
        self.type2 = plant_type_2
        self.tier = max(ps[plant_type_1].tier, ps[plant_type_2].tier)
        self.item_ID = (self.type1 + str(self.stat_growth) + str(self.stat_yield) +
                        str(self.stat_lifespan) + str(self.stat_value) + self.type2)
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
        self.final_ability_eff = None
        self.calc_seed_final()
        self.seed_image = create_seed_image(self.colour)
        # maybe visual hex for stats?
        # visual for item based on stats

    def draw_seed(self, pos_x, pos_y, surface):
        surface.blit(self.seed_image, (pos_x, pos_y))

    def calc_seed_final(self):
        a = ps[self.type1]
        b = ps[self.type2]
        self.final_adult = calc_stats([a.base_adult[0]], [a.mult_adult[0]], [b.base_adult[1]], [b.mult_adult[1]])
        self.final_death = calc_stats([a.base_death[0]], [a.mult_death[0]], [b.base_death[1]], [b.mult_death[1]]) * (1+(
                4 * gs["stat_magnitude"] * self.stat_lifespan / 100))
        self.final_rate = calc_stats([1], [a.mult_rate[0]], [1], [b.mult_rate[1]]) * (1 + (
                2 * gs["stat_magnitude"] * self.stat_growth/100))
        self.final_yield = calc_stats([a.base_yield[0]], [a.mult_yield[0]], [b.base_yield[1]], [b.mult_yield[1]]) * (1+(
                2 * gs["stat_magnitude"] * self.stat_yield/100))
        self.final_value = calc_stats([a.base_value[0]], [a.mult_value[0]], [b.base_value[1]], [b.mult_value[1]]) * (1+(
                4 * gs["stat_magnitude"] * self.stat_value/100))
        self.final_ability_eff = calc_stats([a.ability_eff[0]], [1], [b.ability_eff[1]], [1])

        self.final_yield = round(self.final_yield, 1)
        self.final_ability_eff = int(self.final_ability_eff)
        self.final_value = int(self.final_value)
        self.final_adult = int(self.final_adult)
        self.final_death = int(self.final_death)
        self.final_rate = round(self.final_rate, 2)
