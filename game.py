from useful_functions import *
from Garden.gardenHandler import GardenHandler
from Menus.menuHandler import MenuHandler
from upperUI import MenuSwitcher
from UserData.inventoryHandler import InventoryHandler
from UserData.user import User
from Garden.gardenGlobals import *


class Game:

    def __init__(self):
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

        self.garden_handler = GardenHandler(self)
        self.menu_selector = MenuSwitcher(self)
        self.menu_handler = MenuHandler(self)
        self.inventory_handler = InventoryHandler(self)

    def testing_stuff(self):

        pass

    def screen_layering(self):
        self.game_space.fill(GREEN)

        self.garden_handler.mouse_within_garden_limits()
        self.garden_handler.draw_garden()

        self.menu_selector.draw_buttons()
        self.menu_handler.show_current_menu()

    def event_checking(self):
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
                    self.menu_handler.scroll_menu(scroll=drag_scroll, x=self.drag_x, y=self.drag_y)
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
        self.mouse_pos = pygame.mouse.get_pos()

        self.event_checking()
        self.screen_layering()

        self.game_window.blit(self.game_space, (0, 0))
        self.game_clock.tick(60)
        pygame.display.flip()
