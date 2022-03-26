from useful_functions import *


class Plant:
    def __init__(self):
        self.plant_age = 0
        self.adult_age = 1
        self.decay_age = 1
        self.tick_rate = 1

    def tick_plant(self):
        self.plant_age += self.tick_rate
        if self.plant_age >= self.decay_age:
            return True

    def draw_plant(self, surface, pos_x, pos_y, colour=BROWN):
        size = clamp((self.plant_age / self.adult_age)*100, 100, 0)
        pygame.draw.rect(surface, colour, (pos_x + 50 - size/2, pos_y + 50 - size/2, size, size))

