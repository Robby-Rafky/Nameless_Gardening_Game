import pygame
from useful_functions import *


class GardenSpace:

    def __init__(self, game_space, plot_size_x, plot_size_y, garden_offset, tile_size):
        self.game_space = game_space
        self.plot_size_x = plot_size_x
        self.plot_size_y = plot_size_y
        self.offset_x = garden_offset[0]
        self.offset_y = garden_offset[1]
        self.tile_size = tile_size

    def draw_base_garden(self):
        for x in range(self.plot_size_x):
            for y in range(self.plot_size_y):
                pygame.draw.rect(self.game_space, (0, 0, 0), (self.offset_x + x * self.tile_size,
                                                              self.offset_y + y * self.tile_size,
                                                              self.tile_size, self.tile_size), 2)

    def draw_overlay_garden(self, mouse_coordinates):
        grid_x = clamp(int((mouse_coordinates[0]-self.offset_x) / 100), self.plot_size_x - 1, 0)
        grid_y = clamp(int((mouse_coordinates[1]-self.offset_y) / 100), self.plot_size_y - 1, 0)
        pygame.draw.rect(self.game_space, (255, 255, 255), (self.offset_x + grid_x * self.tile_size,
                                                            self.offset_y + grid_y * self.tile_size,
                                                            self.tile_size, self.tile_size), 2)
