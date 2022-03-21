from Garden.Plants.basePlant import *


class Plant3(Plant):

    def __init__(self):
        Plant.__init__(self)
        self.colour = GREY
        self.adult_age = 3
        self.decay_age = 6
