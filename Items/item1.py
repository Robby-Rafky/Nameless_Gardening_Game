from useful_functions import *
from Items.baseItem import BaseItem


class Item1(BaseItem):

    def __init__(self):
        BaseItem.__init__(self)
        self.colour = GREEN

