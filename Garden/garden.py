from useful_functions import *


class GardenSpace:

    def __init__(self, game):
        self.plot_size_x, self.plot_size_y = None, None
        self.offset_x, self.offset_y = None, None
        self.grid_x, self.grid_y = None, None
        self.game = game

    def draw_base_garden(self):
        for x in range(self.plot_size_x):
            for y in range(self.plot_size_y):
                pygame.draw.rect(self.game.game_space, BLACK, (self.offset_x + x * 100,
                                                               self.offset_y + y * 100,
                                                               100, 100), 2)

    def draw_overlay_garden(self):
        if self.game.garden_handler.mouse_valid:
            if pygame.mouse.get_pressed()[0] and self.game.menu_handler.current_menu is None:
                pygame.draw.rect(self.game.game_space, WHITE, (self.offset_x + self.grid_x * 100,
                                                               self.offset_y + self.grid_y * 100,
                                                               100, 100), 4)
            elif pygame.mouse.get_pressed()[2] and self.game.menu_handler.current_menu is None:
                pygame.draw.rect(self.game.game_space, RED, (self.offset_x + self.grid_x * 100,
                                                             self.offset_y + self.grid_y * 100,
                                                             100, 100), 4)
            else:
                pygame.draw.rect(self.game.game_space, GREY, (self.offset_x + self.grid_x * 100,
                                                              self.offset_y + self.grid_y * 100,
                                                              100, 100), 2)





