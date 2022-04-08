from useful_functions import *
from Items.baseItem import BaseItem
from random import randint


class PlantItem(BaseItem):
    # stats 0-9
    def __init__(self, growth, mutation, seed_yield, lifespan, value, plant_type_1, plant_type_2):
        BaseItem.__init__(self)
        self.colour = randint(0, 255), randint(0, 255), randint(0, 255)
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
                                       " Mutation Rate: " + str(self.stat_mutation),
                                       "         Yield: " + str(self.stat_yield),
                                       "      Lifespan: " + str(self.stat_lifespan),
                                       "         Value: " + str(self.stat_value)]
        self.seed_image = pygame.image.load("Items\seed.png")
        self.seed_image = pygame.transform.scale(self.seed_image, (80, 80))
        self.seed_image_final = None
        self.create_seed_image()
        # maybe visual hex for stats?
        # visual for item based on stats

    def create_seed_image(self):
        if self.plant_type_1 == "Verdant" and self.plant_type_2 == "Verdant":
            self.colour = GREEN

        seed_colour = pygame.Surface(self.seed_image.get_size())
        seed_colour.fill(self.colour)

        self.seed_image_final = self.seed_image.copy()
        self.seed_image_final.blit(seed_colour, (0, 0), special_flags=pygame.BLEND_MULT)

    def draw_seed(self, pos_x, pos_y, surface):
        surface.blit(self.seed_image_final, (pos_x, pos_y))
