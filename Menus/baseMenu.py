from useful_functions import *


class Menu:

    def __init__(self, game, colour):
        self.game = game
        self.visible_state = False
        self.surface = pygame.Surface((1800, 800))
        self.background_colour = colour
        self.buttons = []

    def show_menu(self):
        self.surface.fill(self.background_colour)
        pygame.draw.rect(self.surface, BLACK, (0, 0, 1800, 800), 4)
        self.draw_buttons()
        self.game.game_space.blit(self.surface, (60, 150))

    def handle_events(self):
        pass

    def draw_buttons(self):
        for button in self.buttons:
            button.pack_button(self.surface)
