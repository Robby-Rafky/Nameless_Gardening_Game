from useful_functions import *


class Button:

    def __init__(self, text, position, size, offset, outline, centered, font_size, colour=GREY):
        self.rect, self.text_visual = None, None
        self.x, self.y = position
        self.offset_x, self.offset_y = offset
        self.size = size
        self.font = pygame.font.SysFont("Arial", font_size)
        self.outline = outline
        self.centered = centered
        self.text = text
        self.surface = pygame.Surface(self.size)
        self.update_button(text, colour)

    def update_button(self, text, colour=WHITE):
        self.surface.fill(colour)
        self.text_visual = self.font.render(text, True, BLACK)
        if self.centered:
            self.surface.blit(self.text_visual, (self.size[0]/2 - self.text_visual.get_width()/2,
                                                 self.size[1]/2 - self.text_visual.get_height()/2))
        else:
            self.surface.blit(self.text_visual, (10, 10))
        if self.outline:
            pygame.draw.rect(self.surface, BLACK, (0, 0, self.size[0], self.size[1]), 2)
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])

    def update_button_multiline(self, text, colour=WHITE):
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
        self.rect = pygame.Rect(self.x + self.offset_x, self.y + self.offset_y, self.size[0], self.size[1])



    def button_event_check(self, mouse_coordinates):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_coordinates):
                return True
                pass
            return False

    def pack_button(self, surface):
        surface.blit(self.surface, (self.x, self.y))




