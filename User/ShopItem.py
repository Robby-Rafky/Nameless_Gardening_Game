from button import Button
from useful_functions import *


class ShopItem(Button):
    """Represents an item in the shop.

    The ShopItem class extends the functionality of a Button and represents an item available for purchase in the shop.

    Attributes:
        text (str): The text displayed on the shop item button.
        position (tuple): The position of the shop item button.
        size (tuple): The size of the shop item button.
        offset (tuple): The offset of the shop item button.
        price (int): The price of the shop item.
        item_name (str): The name of the shop item.
        sold_out (bool): Indicates if the shop item is sold out.
        item (object): The item associated with the shop item.

    Methods:
        __init__(text, position, size, offset, price, item=None):
            Initializes a new instance of the ShopItem class.
        update_colour(wallet):
            Updates the color of the shop item based on the player's wallet.
        update_shop(wallet):
            Updates the shop item, including its text and color, based on the player's wallet.
        update_price(price=None):
            Updates the price of the shop item.
        draw_shop_on_surface(surface):
            Draws the shop item on a given surface.

    """
    def __init__(self, text, position, size, offset, price, item=None):
        """
        Initializes a new instance of the ShopItem class.

        Args:
            text (str): The text displayed on the shop item button.
            position (tuple): The position of the shop item button.
            size (tuple): The size of the shop item button.
            offset (tuple): The offset of the shop item button.
            price (int): The price of the shop item.
            item (object): The item associated with the shop item.
        """
        Button.__init__(self, text, position, size, offset, True, True, 20, L_ORANGE)
        self.price = price
        self.item_name = text
        self.sold_out = False
        self.item = item
        self.update_price(price)

    def update_colour(self, wallet):
        """
        Updates the color of the shop item based on the player's wallet.

        Args:
            wallet (int): The player's wallet amount.

        Returns:
            tuple: The color of the shop item.
        """
        if self.sold_out:
            return GREY
        elif wallet >= self.price:
            return L_ORANGE
        else:
            return RED

    def update_shop(self, wallet):
        """
        Updates the shop item, including its text and color, based on the player's wallet.

        Args:
            wallet (int): The player's wallet amount.
        """
        if self.price is not None:
            self.update_textbox(self.text, self.update_colour(wallet))

    def update_price(self, price=None):
        """
        Updates the price of the shop item.

        Args:
            price (int, optional): The price of the shop item. If not provided, the shop item is marked as sold out.
        """
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
        """
        Draws the shop item on a given surface.

        Args:
            surface (pygame.Surface): The surface to draw the shop item on.
        """
        if self.item is not None:
            pygame.draw.rect(surface, BLACK, (self.x + self.size[0]/2 - 50, self.y - 110, 100, 100), 2)
            self.item.draw_seed(self.x + self.size[0]/2 - 40, self.y - 100, surface)
        self.draw_on_surface(surface)
