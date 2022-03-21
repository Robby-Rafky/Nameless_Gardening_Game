from Garden.Plants.basePlant import *


class Plant2(Plant):

    def __init__(self):
        Plant.__init__(self)
        self.colour = BLUE
        self.adult_age = 2
        self.decay_age = 4