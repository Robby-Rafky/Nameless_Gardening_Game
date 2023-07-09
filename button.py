from useful_functions import *
from textBox import TextBox


class Button(TextBox):
    """Represents a button in the game.

    The Button class extends the TextBox class and provides functionality for creating interactive buttons.

    Attributes:
        y_init (int): The initial y-coordinate of the button.
        x_init (int): The initial x-coordinate of the button.
        offset_x (int): The x-offset for positioning the button.
        offset_y (int): The y-offset for positioning the button.
        rect (pygame.Rect): The rectangular area enclosing the button.

    Methods:
        __init__(text, position, size, offset, outline, centered, font_size, colour=GREY):
            Initializes a new instance of the Button class.
        update_button(text, colour):
            Updates the text and colour of the button.
        update_button_position(text, colour, x, y):
            Updates the position, text, and colour of the button.
        update_button_multiline(text, colour):
            Updates the multiline text and colour of the button.
        button_event(mouse_coordinates):
            Checks if a button event has occurred.

    """

    def __init__(self, text, position, size, offset, outline, centered, font_size, colour=GREY):
        """
        Initializes a new instance of the Button class.

        Args:
            text (str): The text displayed on the button.
            position (tuple): The position of the button (x, y).
            size (tuple): The size of the button (width, height).
            offset (tuple): The offset for positioning the button (offset_x, offset_y).
            outline (bool): Specifies whether the button has an outline.
            centered (bool): Specifies whether the text is centered on the button.
            font_size (int): The font size of the text.
            colour (tuple, optional): The colour of the button. Defaults to GREY.
        """
        TextBox.__init__(self, text, position, size, outline, centered, font_size, colour)
        self.y_init = self.y
        self.x_init = self.x
        self.offset_x, self.offset_y = offset
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def update_button(self, text, colour):
        """
        Updates the text and colour of the button.

        Args:
            text (str): The new text for the button.
            colour (tuple): The new colour for the button.
        """
        self.update_textbox(text, colour)
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def update_button_position(self, text, colour, x, y):
        """
        Updates the position, text, and colour of the button.

        Args:
            text (str): The new text for the button.
            colour (tuple): The new colour for the button.
            x (int): The new x-coordinate of the button.
            y (int): The new y-coordinate of the button.
        """
        self.x = x
        self.y = y
        self.update_button(text, colour)

    def update_button_multiline(self, text, colour):
        """
        Updates the multiline text and colour of the button.

        Args:
            text (list): The new multiline text for the button.
            colour (tuple): The new colour for the button.
        """
        self.update_textbox_multiline(text, colour)
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def button_event(self, mouse_coordinates):
        """
        Checks if a button event has occurred.

        Args:
            mouse_coordinates (tuple): The coordinates of the mouse (x, y).

        Returns:
            bool: True if a button event has occurred, False otherwise.
        """
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_coordinates):
                return True
            return False






