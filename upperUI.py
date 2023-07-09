from useful_functions import *
from button import Button


class MenuSwitcher:
    """
    Handles the menu switching functionality.

    Attributes:
        game (Game): The game instance.
        surface (pygame.Surface): The surface for rendering the top buttons.
        top_buttons (list): The list of top buttons.

    Methods:
        draw_buttons():
            Draws the top buttons on the game surface.
        menu_switching():
            Handles the menu switching based on button clicks.
    """
    def __init__(self, game):
        """
        Initializes a new instance of the MenuSwitcher class.

        Args:
            game (Game): The game instance.
        """
        self.game = game
        self.surface = None
        self.top_buttons = []
        self.top_buttons.append(Button("Inventory", (0, 0), (300, 50), (60, 10), True, True, 25, L_ORANGE))
        self.top_buttons.append(Button("Shop", (375, 0), (300, 50), (60, 10), True, True, 25, L_ORANGE))
        self.top_buttons.append(Button("Skill Tree", (750, 0), (300, 50), (60, 10), True, True, 25, L_ORANGE))
        self.top_buttons.append(Button("Crafting", (1125, 0), (300, 50), (60, 10), True, True, 25, L_ORANGE))
        self.top_buttons.append(Button("Plants", (1500, 0), (300, 50), (60, 10), True, True, 25, L_ORANGE))

    def draw_buttons(self):
        """Draws the top buttons on the game surface."""
        self.surface = pygame.Surface((1800, 70))
        self.surface.fill(GREEN)
        for button in self.top_buttons:
            button.draw_on_surface(self.surface)
            button.update_button(button.text, L_ORANGE)
        if self.game.menu_handler.current_menu == "Inventory":
            self.top_buttons[0].update_button("[Inventory]", MENU_GREY)
        if self.game.menu_handler.current_menu == "Shop":
            self.top_buttons[1].update_button("[Shop]", MENU_GREY)
        if self.game.menu_handler.current_menu == "SkillTree":
            self.top_buttons[2].update_button("[Skill Tree]", MENU_GREY)
        if self.game.menu_handler.current_menu == "Crafting":
            self.top_buttons[3].update_button("[Crafting]", MENU_GREY)
        if self.game.menu_handler.current_menu == "Stats":
            self.top_buttons[4].update_button("[Plants]", MENU_GREY)
        self.game.game_space.blit(self.surface, (60, 10))

    def menu_switching(self):
        """
        Handles the menu switching based on button clicks.

        Returns:
            str or None: The name of the menu to switch to, or None if no switch is required.
        """
        if self.top_buttons[0].button_event(self.game.mouse_pos):
            return "Inventory"
        if self.top_buttons[1].button_event(self.game.mouse_pos):
            return "Shop"
        if self.top_buttons[2].button_event(self.game.mouse_pos):
            return "SkillTree"
        if self.top_buttons[3].button_event(self.game.mouse_pos):
            return "Crafting"
        if self.top_buttons[4].button_event(self.game.mouse_pos):
            return "Stats"
        if 60 <= self.game.mouse_pos[0] <= 1860:
            if 150 <= self.game.mouse_pos[1] <= 950:
                return self.game.menu_handler.current_menu
        else:
            return None

