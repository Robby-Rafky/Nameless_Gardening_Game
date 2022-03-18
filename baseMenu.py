from useful_functions import *
from button import Button


class Menu:

    def __init__(self, game, colour):
        self.game = game
        self.visible_state = False
        self.surface = pygame.Surface((1800, 800))
        self.background_colour = colour

    def show_menu_background(self):
        self.surface.fill(self.background_colour)
        self.game.game_space.blit(self.surface, self.game.garden_offset)
