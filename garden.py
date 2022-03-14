import pygame


class GardenSpace:

    def __init__(self, game_space, plot_size_x, plot_size_y):
        self.game_space = game_space
        self.plot_size_x = plot_size_x
        self.plot_size_y = plot_size_y

    def draw_base_garden(self):
        for x in range(self.plot_size_x):
            for y in range(self.plot_size_y):
                pygame.draw.rect(self.game_space, (255, 0, 0), (x * 50, y * 50, 50, 50), 2)
