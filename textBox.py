from useful_functions import *


class TextBox:
    """Represents a text box.

    Attributes:
        text_visual (pygame.Surface): The rendered text surface.
        x (int): The x-coordinate of the text box.
        y (int): The y-coordinate of the text box.
        size (tuple): The size of the text box.
        font (pygame.font.Font): The font used for the text.
        outline (bool): Indicates whether the text box has an outline.
        centered (bool): Indicates whether the text is centered within the text box.
        text (str): The text content of the text box.
        surface (pygame.Surface): The surface of the text box.
        text_colour (tuple): The colour of the text.

    Methods:
        update_textbox(text, colour=WHITE):
            Updates the content and colour of the text box.
        update_textbox_multiline(text, colour=WHITE):
            Updates the multiline content and colour of the text box.
        draw_on_surface(surface):
            Draws the text box on a given surface.
    """
    def __init__(self, text, position, size, outline, centered, font_size, colour=GREY):
        """
        Initializes a new instance of the TextBox class.

        Args:
            text (str): The text content of the text box.
            position (tuple): The position of the text box (x, y).
            size (tuple): The size of the text box (width, height).
            outline (bool): Indicates whether the text box has an outline.
            centered (bool): Indicates whether the text is centered within the text box.
            font_size (int): The font size of the text.
            colour (tuple, optional): The colour of the text box. Defaults to GREY.
        """
        self.text_visual = None
        self.x, self.y = position
        self.size = size
        self.font = pygame.font.Font(PIXEL_FONT, font_size)
        self.outline = outline
        self.centered = centered
        self.text = text
        self.surface = pygame.Surface(self.size)
        self.text_colour = BLACK
        self.update_textbox(text, colour)

    def update_textbox(self, text, colour=WHITE):
        """
        Updates the content and colour of the text box.

        Args:
            text (str): The text content of the text box.
            colour (tuple, optional): The colour of the text box. Defaults to WHITE.
        """
        self.surface.fill(colour)
        self.text_visual = self.font.render(text, True, self.text_colour)
        if self.centered:
            self.surface.blit(self.text_visual, (self.size[0]/2 - self.text_visual.get_width()/2,
                                                 self.size[1]/2 - self.text_visual.get_height()/2))
        else:
            self.surface.blit(self.text_visual, (10, 10))
        if self.outline:
            pygame.draw.rect(self.surface, BLACK, (0, 0, self.size[0], self.size[1]), 2)

    def update_textbox_multiline(self, text, colour=WHITE):
        """
        Updates the multiline content and colour of the text box.

        Args:
            text (str): The multiline text content of the text box.
            colour (tuple, optional): The colour of the text box. Defaults to WHITE.
        """
        self.surface.fill(colour)
        self.text = text
        for x in range(len(text)):
            self.text_visual = self.font.render(text[x], True, self.text_colour)
            if self.centered:
                self.surface.blit(self.text_visual, (self.size[0] / 2 - self.text_visual.get_width() / 2,
                                                     self.size[1] / 2 - self.text_visual.get_height() / 2
                                                     + self.text_visual.get_height() * x))
            else:
                self.surface.blit(self.text_visual, (10, 10 + self.text_visual.get_height() * x))
        if self.outline:
            pygame.draw.rect(self.surface, BLACK, (0, 0, self.size[0], self.size[1]), 2)

    def draw_on_surface(self, surface):
        """
        Draws the text box on a given surface.

        Args:
            surface (pygame.Surface): The surface to draw the text box on.
        """
        surface.blit(self.surface, (self.x, self.y))
