from useful_functions import *


class TextBox:

    def __init__(self, text, position, size, offset, outline, centered, font_size, colour=GREY):
        self.text_visual = None
        self.x, self.y = position
        self.offset_x, self.offset_y = offset
        self.size = size
        self.font = pygame.font.Font(PIXEL_FONT, font_size)
        self.outline = outline
        self.centered = centered
        self.text = text
        self.surface = pygame.Surface(self.size)
        self.update_textbox(text, colour)

    def update_textbox(self, text, colour=WHITE):
        self.surface.fill(colour)
        self.text_visual = self.font.render(text, True, BLACK)
        if self.centered:
            self.surface.blit(self.text_visual, (self.size[0]/2 - self.text_visual.get_width()/2,
                                                 self.size[1]/2 - self.text_visual.get_height()/2))
        else:
            self.surface.blit(self.text_visual, (10, 10))
        if self.outline:
            pygame.draw.rect(self.surface, BLACK, (0, 0, self.size[0], self.size[1]), 2)

    def update_textbox_multiline(self, text, colour=WHITE):
        self.surface.fill(colour)
        for x in range(len(text)):
            self.text_visual = self.font.render(text[x], True, BLACK)
            if self.centered:
                self.surface.blit(self.text_visual, (self.size[0] / 2 - self.text_visual.get_width() / 2,
                                                     self.size[1] / 2 - self.text_visual.get_height() / 2
                                                     + self.text_visual.get_height() * x))
            else:
                self.surface.blit(self.text_visual, (10, 10 + self.text_visual.get_height() * x))
        if self.outline:
            pygame.draw.rect(self.surface, BLACK, (0, 0, self.size[0], self.size[1]), 2)

    def draw_on_surface(self, surface):
        surface.blit(self.surface, (self.x, self.y))
