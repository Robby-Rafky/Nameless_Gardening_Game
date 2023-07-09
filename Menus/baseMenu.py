from useful_functions import *


class Menu:
    """
    A class representing a menu.

    Attributes:
        game (Game): The game instance.
        visible_state (bool): True if the menu is visible, False otherwise.
        surface (Surface): The surface of the menu.
        background_colour (Tuple[int, int, int]): The RGB color value for the menu background.

    Methods:
        __init__(self, game): Initialize a Menu4 object.
        menu4_menu_events(self): Placeholder method for handling menu events.
    """

    def __init__(self, game, colour):
        """Initialize a Menu object.

        Args:
            game (Game): The game instance.
            colour (Tuple[int, int, int]): The RGB color value for the menu background.
        """
        self.game = game
        self.visible_state = False
        self.surface = pygame.Surface((1800, 800))
        self.background_colour = colour

    def show_menu(self):
        """Display the menu on the game screen."""
        pygame.draw.rect(self.surface, BLACK, (0, 0, 1800, 800), 4)

        self.game.game_space.blit(self.surface, (60, 150))


