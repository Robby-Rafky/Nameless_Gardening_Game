from Garden.Plants.basePlant import *


class Plant1(Plant):

    def __init__(self):
        Plant.__init__(self)
        self.colour = RED
        self.adult_age = 5
        self.decay_age = 10
