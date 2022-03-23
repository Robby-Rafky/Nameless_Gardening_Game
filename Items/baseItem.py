from useful_functions import *


class BaseItem:

    def __init__(self):
        self.stack_size = 0
        self.sell_price = 0
        self.buy_price = 0
        self.colour = RED

    def draw_item(self, pos_x, pos_y, surface, size):
        pygame.draw.circle(surface, self.colour, (pos_x, pos_y), 30 * size)

