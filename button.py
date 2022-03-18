from useful_functions import *


class Button:

    def __init__(self, text, position, size, font_size, colour=GREY, clicked_text=""):
        self.rect = None
        self.x, self.y = position
        self.size = size
        self.font = pygame.font.SysFont("Arial", font_size)
        self.surface = None
        self.text = text
        if clicked_text == "":
            self.clicked_text = text
        else:
            self.clicked_text = clicked_text
        self.update_button(text, colour)

    def update_button(self, text="", colour=WHITE):
        self.surface = pygame.Surface(self.size)
        self.surface.fill(colour)
        self.surface.blit(self.font.render(text, True, BLACK), (10, 10))
        self.rect = pygame.Rect(self.x, self.y, self.size[0], self.size[1])

    def button_event_check(self, event, mouse_coordinates):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                if self.rect.collidepoint(mouse_coordinates):
                    return True
                    pass
                return False

    def pack_button(self, game_space):
        game_space.blit(self.surface, (self.x, self.y))




