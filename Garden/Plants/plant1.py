from Garden.Plants.basePlant import *


class Plant1(Plant):

    def __init__(self):
        Plant.__init__(self,1,2,3,4,5,6,7)
        self.colour = RED
        self.adult_age = 5
        self.decay_age = 10
