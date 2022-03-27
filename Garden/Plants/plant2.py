from Garden.Plants.basePlant import *


class Plant2(Plant):

    def __init__(self):
        Plant.__init__(self,1,2,3,4,5,6,7)
        self.colour = BLUE
        self.adult_age = 2
        self.decay_age = 4