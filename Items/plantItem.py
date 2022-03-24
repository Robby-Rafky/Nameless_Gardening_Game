from useful_functions import *
from Items.baseItem import BaseItem


class PlantItem(BaseItem):
    # stats 0-9
    def __init__(self, growth, mutation, seed_yield, lifespan, value, plant_type):
        BaseItem.__init__(self)
        self.colour = GREEN
        self.stat_growth = growth
        self.stat_mutation = mutation
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.plant_type = plant_type
        self.item_ID = (self.plant_type+str(self.stat_growth)+str(self.stat_mutation)+str(
            self.stat_yield)+str(self.stat_lifespan)+str(self.stat_value))
        self.stack_size = 1
        self.item_description = ["Seed Type: "+self.plant_type,
                                 "Growth Rate: "+str(self.stat_growth),
                                 "Mutation Rate: "+str(self.stat_mutation),
                                 "Yield: "+str(self.stat_yield),
                                 "Lifespan: "+str(self.stat_lifespan),
                                 "Value: "+str(self.stat_value)]
        # maybe visual hex for stats?
        # visual for item based on stats

