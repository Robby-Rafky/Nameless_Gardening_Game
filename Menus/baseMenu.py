from useful_functions import *


class Menu:

    def __init__(self, game, colour):
        self.game = game
        self.visible_state = False
        self.surface = pygame.Surface((1800, 800))
        self.background_colour = colour

    def show_menu(self):

        pygame.draw.rect(self.surface, BLACK, (0, 0, 1800, 800), 4)

        self.game.game_space.blit(self.surface, (60, 150))


