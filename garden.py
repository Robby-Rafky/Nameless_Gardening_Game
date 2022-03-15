import pygame
from useful_functions import *


class GardenSpace:

    def __init__(self, game_space, plot_size, garden_offset, tile_size):
        self.game_space = game_space
        self.plot_size_x = plot_size[0]
        self.plot_size_y = plot_size[1]
        self.offset_x = garden_offset[0]
        self.offset_y = garden_offset[1]
        self.tile_size = tile_size

    def draw_base_garden(self):
        for x in range(self.plot_size_x):
            for y in range(self.plot_size_y):
                pygame.draw.rect(self.game_space, BLACK, (self.offset_x + x * self.tile_size,
                                                          self.offset_y + y * self.tile_size,
                                                          self.tile_size, self.tile_size), 2)

    def draw_overlay_garden(self, mouse_coordinates):
        if (self.offset_x <= mouse_coordinates[0] <= (self.offset_x + self.tile_size * self.plot_size_x)) and (
                self.offset_y <= mouse_coordinates[1] <= (self.offset_y + self.tile_size * self.plot_size_y)):

            grid_x = clamp(int((mouse_coordinates[0] - self.offset_x) / 100), self.plot_size_x - 1, 0)
            grid_y = clamp(int((mouse_coordinates[1] - self.offset_y) / 100), self.plot_size_y - 1, 0)

            if pygame.mouse.get_pressed()[0]:
                pygame.draw.rect(self.game_space, WHITE, (self.offset_x + grid_x * self.tile_size,
                                                       self.offset_y + grid_y * self.tile_size,
                                                       self.tile_size, self.tile_size), 4)
                return grid_x, grid_y
            else:
                pygame.draw.rect(self.game_space, GREY, (self.offset_x + grid_x * self.tile_size,
                                                          self.offset_y + grid_y * self.tile_size,
                                                          self.tile_size, self.tile_size), 2)

    # garden plot control via array
    def test_overlay(self, grid_data):
        test_ycoord = -1
        for y in grid_data:
            test_ycoord += 1
            test_xcoord = -1
            for x in y:
                test_xcoord += 1
                x = clamp(x * 5, 100, 0)
                pygame.draw.rect(self.game_space, BROWN, (self.offset_x + test_xcoord * self.tile_size + 50 - x/2,
                                                         self.offset_y + test_ycoord * self.tile_size + 50 - x/2,
                                                         x, x))

