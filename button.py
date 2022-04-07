from useful_functions import *
from textBox import TextBox


class Button(TextBox):

    def __init__(self, text, position, size, offset, outline, centered, font_size, colour=GREY):
        TextBox.__init__(self, text, position, size, offset, outline, centered, font_size, colour)
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def update_button(self, text, colour):
        self.update_textbox(text, colour)
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def update_button_multiline(self, text, colour):
        self.update_textbox_multiline(text, colour)
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def button_event(self, mouse_coordinates):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_coordinates):
                return True
                pass
            return False






