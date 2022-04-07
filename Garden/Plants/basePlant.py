from useful_functions import *
from datetime import timedelta

class Plant:
    def __init__(self, growth, mutation, seed_yield, lifespan, value, plant_type_1, plant_type_2, description):
        self.plant_age = 0
        self.adult_age = 5
        self.decay_age = 20
        self.tick_rate = 1
        self.stat_growth = growth
        self.stat_mutation = mutation
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.plant_type_1 = plant_type_1
        self.plant_type_2 = plant_type_2
        self.plant_description = description
        # test
        self.colour = L_ORANGE

    def tick_plant(self):
        self.plant_age += self.tick_rate
        if self.plant_age >= self.decay_age:
            return True

    def draw_plant(self, surface, pos_x, pos_y):
        size = clamp((self.plant_age / self.adult_age)*100, 100, 0)
        pygame.draw.rect(surface, self.colour, (pos_x + 50 - size/2, pos_y + 50 - size/2, size, size))

    def is_adult(self):
        if self.plant_age >= self.adult_age:
            return True

    def get_time_to_adult(self):
        time = self.adult_age - self.plant_age
        return str(timedelta(seconds=time))

    def get_time_to_death(self):
        time = self.decay_age - self.plant_age
        return str(timedelta(seconds=time))
