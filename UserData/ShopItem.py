from button import Button
from useful_functions import *


class ShopItem(Button):
    def __init__(self, text, position, size, offset, price, item=None):
        Button.__init__(self, text, position, size, offset, True, True, 20, L_ORANGE)
        self.price = price
        self.item_name = text
        self.sold_out = False
        self.item = item
        self.update_price(price)

    def update_colour(self, wallet):
        if self.sold_out:
            return GREY
        elif wallet >= self.price:
            return L_ORANGE
        else:
            return RED

    def update_shop(self, wallet):
        if self.price is not None:
            self.update_textbox(self.text, self.update_colour(wallet))

    def update_price(self, price=None):
        if price is None:
            self.sold_out = True
        if not self.sold_out:
            self.price = price
            if price <= 0:
                self.text = self.item_name + " (Free)"
            else:
                self.text = self.item_name + " (" + str(price) + "$)"
        else:
            self.text = "Sold out"

    def draw_shop_on_surface(self, surface):
        if self.item is not None:
            pygame.draw.rect(surface, BLACK, (self.x + self.size[0]/2 - 50, self.y - 110, 100, 100), 2)
            self.item.draw_seed(self.x + self.size[0]/2 - 40, self.y - 100, surface)
        self.draw_on_surface(surface)
