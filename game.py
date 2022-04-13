from useful_functions import *
from Garden.gardenHandler import GardenHandler
from Menus.menuHandler import MenuHandler
from upperUI import MenuSwitcher
from UserData.inventoryHandler import InventoryHandler
from UserData.user import User


class Game:

    def __init__(self):
        pygame.init()
        self.tick_time = pygame.USEREVENT
        pygame.time.set_timer(self.tick_time, 1000)
        self.running = True
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 1920, 1080
        self.game_space = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.game_window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        self.game_clock = pygame.time.Clock()
        self.base_background_colour = GREEN
        self.mouse_pos = [0, 0]
        self.user = User()
        # all menu references go here.

        self.garden_handler = GardenHandler(self)
        self.menu_selector = MenuSwitcher(self)
        self.menu_handler = MenuHandler(self)
        self.inventory_handler = InventoryHandler(self)

    def testing_stuff(self):
        self.garden_handler.expand_vertical()
        self.garden_handler.expand_horizontal()
        pass

    def screen_layering(self):
        self.game_space.fill(GREEN)

        self.garden_handler.mouse_within_garden_limits()
        self.garden_handler.draw_garden()

        self.menu_selector.draw_buttons()
        self.menu_handler.show_current_menu()

    def event_checking(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == self.tick_time:
                self.garden_handler.tick_garden()
                pass

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.menu_handler.current_menu is None:
                    if pygame.mouse.get_pressed()[0] and self.garden_handler.mouse_valid:
                        self.garden_handler.place_on_garden_tile()
                self.menu_handler.current_menu = self.menu_selector.menu_switching()
                self.menu_handler.current_menu_event_check()
                self.garden_handler.garden.garden_button_events()

            if event.type == pygame.MOUSEWHEEL:
                self.menu_handler.scroll_menu(event.y)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_handler.close_current_menu()
                    self.garden_handler.planting = None
                    self.garden_handler.garden.clicked_plot_index = None
                    self.garden_handler.garden.clicked_plot = None

                if event.key == pygame.K_SPACE:
                    self.testing_stuff()

    def game_loop(self):
        self.mouse_pos = pygame.mouse.get_pos()

        self.event_checking()
        self.screen_layering()

        self.game_window.blit(self.game_space, (0, 0))
        self.game_clock.tick(60)
        pygame.display.flip()
