from useful_functions import *


class Plant:
    def __init__(self, growth, seed_yield, lifespan, value, x, y, plant_type_1, plant_type_2, game):
        self.game = game
        self.type1 = self.game.data_handler.plant_types[plant_type_1]
        self.type2 = self.game.data_handler.plant_types[plant_type_2]
        self.externals = self.game.data_handler.garden_globals
        pygame.event.post(pygame.event.Event(self.game.planted, message=[(x, y)]))
        self.plant_age = 0
        self.adult_age = None
        self.decay_age = None

        self.final_adult = None
        self.final_death = None
        self.final_rate = None
        self.final_yield = None
        self.final_value = None
        self.final_essence = None

        self.internal_adult = None
        self.internal_death = None
        self.internal_rate = None
        self.internal_yield = None
        self.internal_value = None
        self.internal_essence = None

        # multiplicative with internal stats
        self.external_adult = None
        self.external_death = None
        self.external_rate = None
        self.external_yield = None
        self.external_value = None
        self.external_essence = None

        self.x = x
        self.y = y
        self.stat_growth = growth
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.res = (growth + seed_yield + lifespan + value) / 4

        self.tier = max(self.type1["tier"], self.type2["tier"])
        self.colour = self.type1["colour"]

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
        self.assign_static_values()


    def tick_plant(self):
        self.plant_age += self.final_rate
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

    def get_time_to_adult(self, eff=False):
        if eff:
            time = int((self.adult_age - self.plant_age) / self.final_rate)
        else:
            time = int(self.adult_age - self.plant_age)
        return get_time(time)

    def get_time_to_death(self, eff=False):
        if eff:
            time = int((self.decay_age - self.plant_age)/self.final_rate)
        else:
            time = int(self.decay_age - self.plant_age)
        return get_time(time)

    def calc_static_values(self):
        a = self.type1
        b = self.type2
        self.internal_adult = calc_stats([a["adult_age"][0]], [a["adult_mult"][0]], [b["adult_age"][1]], [b["adult_mult"][1]])
        self.internal_death = calc_stats([a["death_age"][0]], [a["death_mult"][0]], [b["death_age"][1]], [b["death_mult"][1]])

        self.external_adult = self.externals["total"]["adult"]
        self.external_death = self.externals["total"]["death"]

        self.final_adult = self.external_adult * self.internal_adult
        self.final_death = self.external_death * self.internal_death * (1 + (4 * self.externals["stat"]["mult"] *
                                                                        self.stat_lifespan/100))

        self.final_adult = int(self.final_adult)
        self.final_death = int(self.final_death)

    def update_internal_plant(self):
        a = self.type1
        b = self.type2
        self.internal_rate = calc_stats([1], [a["growth_mult"][0]], [1], [b["growth_mult"][1]])
        self.internal_yield = calc_stats([1], [a["yield_mult"][0]], [1], [b["yield_mult"][1]])
        self.internal_value = calc_stats([a["value_base"][0]], [a["value_mult"][0]],
                                         [b["value_base"][1]], [b["value_mult"][1]])
        self.internal_essence = calc_stats([a["essence_base"][0]], [1], [b["essence_base"][1]], [1])

    def update_external_info(self):
        self.external_rate = self.externals["total"]["rate"]
        self.external_yield = self.externals["total"]["yield"]
        self.external_value = self.externals["total"]["value"]
        self.external_essence = self.externals["total"]["essence"]

    def update_final_values(self):
        self.update_internal_plant()
        self.update_external_info()
        stat_mag = self.externals["stat"]["mult"]
        self.final_rate = self.external_rate * self.internal_rate * (1 + (2 * stat_mag *
                                                                          self.stat_growth/100))
        self.final_yield = 100 * self.external_yield * self.internal_yield * (1 + (2 * stat_mag *
                                                                             self.stat_yield/100))
        self.final_value = self.external_value * self.internal_value * (1 + (4 * stat_mag *
                                                                             self.stat_value/100))
        self.final_essence = self.external_essence * self.internal_essence

        self.final_yield = round(self.final_yield, 1)
        self.final_essence = int(self.final_essence)
        self.final_death = int(self.final_death)
        self.final_rate = 20 * round(self.final_rate, 2)
        self.final_value = int(self.final_value)

    def assign_static_values(self):
        self.adult_age = self.final_adult
        self.decay_age = self.final_death

