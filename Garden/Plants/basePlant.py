from useful_functions import *
from datetime import timedelta
from Garden.Plants.plantSpecies import plant_species as ps
from Garden.gardenGlobals import garden_global as gs


class Plant:
    def __init__(self, growth, seed_yield, lifespan, value, x, y, plant_type_1, plant_type_2):
        self.plant_age = 0
        self.adult_age = 5
        self.decay_age = 20
        self.tick_rate = 1

        self.final_adult = None
        self.final_death = None
        self.final_rate = None
        self.final_yield = None
        self.final_value = None
        self.final_ability_eff = None

        self.internal_adult = None
        self.internal_death = None
        self.internal_rate = None
        self.internal_yield = None
        self.internal_value = None
        self.internal_ability_eff = None

        # multiplicative with internal stats
        self.external_adult = None
        self.external_death = None
        self.external_rate = None
        self.external_yield = None
        self.external_value = None
        self.external_ability_eff = None

        self.x = x
        self.y = y
        self.stat_growth = growth
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.res = (growth + seed_yield + lifespan + value) / 4

        self.type1 = plant_type_1
        self.type2 = plant_type_2
        self.tier = max(ps[plant_type_1].tier, ps[plant_type_2].tier)

        self.is_adult = False

        if plant_type_1 == plant_type_2:
            self.is_pure = True
        else:
            self.is_pure = False
        if growth + seed_yield + lifespan + value == 400:
            self.is_max = True
        else:
            self.is_max = False

        self.calc_static_values()
        self.update_final_values()


        # test
        self.colour = ps[plant_type_1].colour

    def tick_plant(self):
        self.plant_age += self.tick_rate
        if not self.is_adult and self.plant_age >= self.adult_age:
            self.is_adult = True
            return 0
        elif self.plant_age >= self.decay_age:
            return 1
        else:
            return 2

    def draw_plant(self, surface, pos_x, pos_y):
        size = clamp((self.plant_age / self.adult_age)*100, 100, 0)
        pygame.draw.rect(surface, self.colour, (pos_x + 50 - size/2, pos_y + 50 - size/2, size, size))

    def get_time_to_adult(self):
        time = self.adult_age - self.plant_age
        return str(timedelta(seconds=time))

    def get_time_to_death(self):
        time = self.decay_age - self.plant_age
        return str(timedelta(seconds=time))

    def calc_static_values(self):
        a = ps[self.type1]
        b = ps[self.type2]
        self.internal_adult = calc_stats([a.base_adult[0]], [a.mult_adult[0]], [b.base_adult[1]], [b.mult_adult[1]])
        self.internal_death = calc_stats([a.base_death[0]], [a.mult_death[0]], [b.base_death[1]], [b.mult_death[1]])

        self.external_adult = gs["total_adult"]
        self.external_death = gs["total_death"]

        self.final_adult = self.external_adult * self.internal_adult
        self.final_death = self.external_death * self.internal_death * (1 + (4 * gs["stat_magnitude"] *
                                                                        self.stat_lifespan/100))

        self.final_adult = int(self.final_adult)
        self.final_death = int(self.final_death)

    def update_internal_plant(self):
        a = ps[self.type1]
        b = ps[self.type2]
        self.internal_rate = calc_stats([1], [a.mult_rate[0]], [1], [b.mult_rate[1]])
        self.internal_yield = calc_stats([a.base_yield[0]], [a.mult_yield[0]], [b.base_yield[1]], [b.mult_yield[1]])
        self.internal_value = calc_stats([a.base_value[0]], [a.mult_value[0]], [b.base_value[1]], [b.mult_value[1]])
        self.internal_ability_eff = calc_stats([a.ability_eff[0]], [1], [b.ability_eff[1]], [1])

    def update_external_info(self):
        self.external_rate = gs["total_rate"]
        self.external_yield = gs["total_yield"]
        self.external_value = gs["total_value"]
        self.external_ability_eff = gs["total_ability"]

    def update_final_values(self):
        self.update_internal_plant()
        self.update_external_info()
        self.final_rate = self.external_rate * self.internal_rate * (1 + (2 * gs["stat_magnitude"] *
                                                                          self.stat_growth/100))
        self.final_yield = self.external_yield * self.internal_yield * (1 + (2 * gs["stat_magnitude"] *
                                                                             self.stat_yield/100))
        self.final_value = self.external_value * self.internal_value * (1 + (4 * gs["stat_magnitude"] *
                                                                             self.stat_value/100))
        self.final_ability_eff = self.external_ability_eff * self.internal_ability_eff

        self.final_yield = round(self.final_yield, 1)
        self.final_ability_eff = int(self.final_ability_eff)
        self.final_death = int(self.final_death)
        self.final_rate = round(self.final_rate, 2)
        self.final_value = int(self.final_value)
