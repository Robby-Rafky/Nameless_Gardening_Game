from useful_functions import *
from Items.baseItem import BaseItem
from Garden.Plants.plantSpecies import plant_species
from Items.seedGen import create_seed_image

class PlantItem(BaseItem):
    # stats 0-9
    def __init__(self, growth, mutation, seed_yield, lifespan, value, plant_type_1, plant_type_2):
        BaseItem.__init__(self)
        self.colour = plant_species[plant_type_1].colour
        self.stat_growth = growth
        self.stat_mutation = mutation
        self.stat_yield = seed_yield
        self.stat_lifespan = lifespan
        self.stat_value = value
        self.plant_type_1 = plant_type_1
        self.plant_type_2 = plant_type_2
        self.item_ID = (self.plant_type_1 + str(self.stat_growth) + str(self.stat_mutation) + str(
            self.stat_yield) + str(self.stat_lifespan) + str(self.stat_value) + self.plant_type_2)
        self.stack_size = 1
        self.item_stats_description = ["   Growth Rate: " + str(self.stat_growth),
                                       "         Yield: " + str(self.stat_yield),
                                       "      Lifespan: " + str(self.stat_lifespan),
                                       "         Value: " + str(self.stat_value)]

        self.seed_image = create_seed_image(self.colour)
        # maybe visual hex for stats?
        # visual for item based on stats

    def draw_seed(self, pos_x, pos_y, surface):
        surface.blit(self.seed_image, (pos_x, pos_y))
