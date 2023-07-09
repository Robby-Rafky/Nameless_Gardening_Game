from useful_functions import *
from Garden.gardenHandler import GardenHandler
from Menus.menuHandler import MenuHandler
from upperUI import MenuSwitcher
from User.inventoryHandler import InventoryHandler
from User.user import User
from Data.dataHandler import DataHandler


class Game:
    """Represents the game and its main functionalities.

    Attributes:
        tick_time (int): The custom event type for game ticks.
        planted (int): The custom event type for plant state changes.
        plant_state_changed (int): The custom event type for plant state changes.
        running (bool): Indicates whether the game is running or not.
        scrolling (bool): Indicates whether the game window is being scrolled.
        drag_y (int): The y-coordinate of the drag event.
        drag_x (int): The x-coordinate of the drag event.
        DISPLAY_WIDTH (int): The width of the game display.
        DISPLAY_HEIGHT (int): The height of the game display.
        game_space (pygame.Surface): The surface for the game space.
        game_window (pygame.Surface): The game window surface.
        game_clock (pygame.time.Clock): The clock object for controlling the frame rate.
        base_background_colour (tuple): The base background colour of the game.
        mouse_pos (list): The current position of the mouse.
        user (User): The user object representing the player.
        data_handler (DataHandler): The data handler object for managing game data.
        garden_handler (GardenHandler): The garden handler object for managing the garden.
        menu_selector (MenuSwitcher): The menu switcher object for selecting menus.
        menu_handler (MenuHandler): The menu handler object for managing menus.
        inventory_handler (InventoryHandler): The inventory handler object for managing the inventory.

    Methods:
        testing_stuff():
            Performs testing-related actions.
        screen_layering():
            Draws the game layers on the game space surface.
        event_checking():
            Checks and handles events in the game.
        game_loop():
            The main game loop for updating and rendering the game.
    """
    def __init__(self):
        """Initializes a new instance of the Game class."""
        pygame.init()
        self.tick_time = pygame.USEREVENT
        self.planted = pygame.USEREVENT + 1
        self.plant_state_changed = pygame.USEREVENT + 2
        pygame.time.set_timer(self.tick_time, 1000)
        self.running = True
        self.scrolling = False

        self.drag_y = None
        self.drag_x = None
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 1920, 1080
        self.game_space = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.game_window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        self.game_clock = pygame.time.Clock()
        self.base_background_colour = GREEN
        self.mouse_pos = [0, 0]
        self.user = User()
        self.data_handler = DataHandler()

        self.garden_handler = GardenHandler(self)
        self.menu_selector = MenuSwitcher(self)
        self.menu_handler = MenuHandler(self)
        self.inventory_handler = InventoryHandler(self)

    def testing_stuff(self):
        """TEMP FUNCTION FOR TESTING."""
        self.menu_handler.skill_tree_menu.change_location(200, 300)
        pass

    def screen_layering(self):
        """Draws the game layers on the game space surface."""
        self.game_space.fill(GREEN)

        self.garden_handler.mouse_within_garden_limits()
        self.garden_handler.draw_garden()

        self.menu_selector.draw_buttons()
        self.menu_handler.show_current_menu()

    def event_checking(self):
        """Checks and handles events in the game."""
        for event in pygame.event.get():
            # when the user quits out of the program
            if event.type == pygame.QUIT:
                self.running = False

            # every real world second
            if event.type == self.tick_time:
                self.garden_handler.tick_garden()

            # when any plant in the garden becomes an adult, dies or spawns in
            if event.type == self.plant_state_changed:
                for item in event.message:
                    self.garden_handler.update_non_plants(item[0], item[1])

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.drag_y = self.mouse_pos[1]
                    self.drag_x = self.mouse_pos[0]
                    self.scrolling = True
                if self.menu_handler.current_menu is None:
                    if pygame.mouse.get_pressed()[0] and self.garden_handler.mouse_valid:
                        self.garden_handler.place_on_garden_tile()
                self.menu_handler.current_menu = self.menu_selector.menu_switching()
                self.menu_handler.current_menu_event_check()
                self.garden_handler.garden.garden_button_events()

            if event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    self.scrolling = False

            if event.type == pygame.MOUSEMOTION:
                if self.scrolling:
                    mouse_x, mouse_y = event.pos
                    drag_scroll = (mouse_y - self.drag_y)/20
                    self.menu_handler.scroll_menu(scroll=drag_scroll, x=self.drag_x-mouse_x, y=self.drag_y-mouse_y)
                    self.drag_y = mouse_y
                    self.drag_x = mouse_x

            if event.type == pygame.MOUSEWHEEL:
                self.menu_handler.scroll_menu(scroll=event.y, zoom=event.y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_handler.close_current_menu()
                    self.garden_handler.planting = None
                    self.garden_handler.garden.clicked_plot_index = None
                    self.garden_handler.garden.clicked_plot = None

                if event.key == pygame.K_SPACE:
                    self.testing_stuff()

    def game_loop(self):
        """The main game loop for updating and rendering the game."""
        self.mouse_pos = pygame.mouse.get_pos()

        self.event_checking()
        self.screen_layering()

        self.game_window.blit(self.game_space, (0, 0))
        self.game_clock.tick(60)
        pygame.display.flip()
