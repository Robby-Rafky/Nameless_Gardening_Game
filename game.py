import pygame

from useful_functions import *
from garden import GardenSpace
from menuHandler import MenuHandler
from upperUI import MenuSwitcher


class Game:

    def __init__(self):
        pygame.init()
        self.running = True
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = 1920, 1080
        self.game_space = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.game_window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        # move to garden manager-------------
        self.garden_offset = (60, 150)
        self.garden_size = (18, 8)
        self.garden_tile_size = 100
        self.garden_contents = [[0 for _ in range(self.garden_size[0])] for _ in range(self.garden_size[1])]
        # ----------------------------------
        self.game_clock = pygame.time.Clock()
        self.base_background_colour = GREEN
        self.mouse_position = (0, 0)
        # all menu references go here.
        self.current_menu = None
        self.plot_clicked = (0, 0)

        self.base_garden = GardenSpace(self.game_space, self.garden_size, self.garden_offset, self.garden_tile_size)
        self.menu_selector = MenuSwitcher(self)
        self.menu_handler = MenuHandler(self)

        self.testing_stuff()

    def testing_stuff(self):
        pass

    def screen_layering(self):
        self.game_space.fill(GREEN)

        self.base_garden.draw_base_garden()
        self.base_garden.test_overlay(self.garden_contents)

        self.plot_clicked = self.base_garden.draw_overlay_garden(self.mouse_position)

        self.menu_selector.draw_buttons()
        self.menu_handler.show_current_menu()

    def event_checking(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONUP:
                if self.plot_clicked is not None and self.menu_handler.current_menu is None:
                    self.garden_contents[self.plot_clicked[1]][self.plot_clicked[0]] += 1

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.menu_handler.current_menu = self.menu_selector.menu_switching()
                self.menu_handler.current_menu_event_check()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.menu_handler.close_current_menu()

    def game_loop(self):
        self.mouse_position = pygame.mouse.get_pos()

        self.event_checking()
        self.screen_layering()

        self.game_window.blit(self.game_space, (0, 0))
        self.game_clock.tick(60)
        pygame.display.flip()
