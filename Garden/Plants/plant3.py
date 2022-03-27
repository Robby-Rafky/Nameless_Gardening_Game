from Garden.Plants.basePlant import *


class Plant3(Plant):

    def __init__(self):
        Plant.__init__(self,1,2,3,4,5,6,7)
        self.colour = GREY
        self.adult_age = 3
        self.decay_age = 10
