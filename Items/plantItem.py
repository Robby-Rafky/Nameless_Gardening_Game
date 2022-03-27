from useful_functions import *
from Items.baseItem import BaseItem


class PlantItem(BaseItem):
    # stats 0-9
    def __init__(self, growth, mutation, seed_yield, lifespan, value, plant_type_1, plant_type_2):
        BaseItem.__init__(self)
        self.colour = L_ORANGE
        self.stat_growth = growth
        self.stat_mutation = mutation
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.plant_type_1 = plant_type_1
        self.plant_type_2 = plant_type_2
        self.item_ID = (self.plant_type_1 + str(self.stat_growth) + str(self.stat_mutation) + str(
            self.stat_yield) + str(self.stat_lifespan) + str(self.stat_value) + self.plant_type_2)
        self.stack_size = 5
        self.item_stats_description = ["   Growth Rate: " + str(self.stat_growth),
                                       " Mutation Rate: " + str(self.stat_mutation),
                                       "         Yield: " + str(self.stat_yield),
                                       "      Lifespan: " + str(self.stat_lifespan),
                                       "         Value: " + str(self.stat_value)]
        # maybe visual hex for stats?
        # visual for item based on stats