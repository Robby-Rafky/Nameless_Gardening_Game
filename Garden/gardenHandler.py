from useful_functions import *
from Garden.Plants.plant1 import Plant1
from Garden.Plants.plant2 import Plant2
from Garden.Plants.plant3 import Plant3
from Garden.garden import GardenSpace


class GardenHandler:

    def __init__(self, game):
        self.garden = GardenSpace(game)
        self.additional_offset = None
        self.game = game
        self.garden_contents = []
        self.mouse_valid = False
        self.change_plot_size(1, 1)

    def change_plot_size(self, x_size, y_size):
        self.garden.plot_size_x, self.garden.plot_size_y = x_size, y_size
        self.additional_offset = [(100 * (18 - self.garden.plot_size_x)) / 2, (100 * (8 - self.garden.plot_size_x)) / 2]

        self.garden.offset_x = int(self.additional_offset[0]) + 60
        self.garden.offset_y = int(self.additional_offset[1]) + 150

        for x in range(len(self.garden_contents)):
            self.garden_contents[x].append(None)
        self.garden_contents.append([None for _ in range(self.garden.plot_size_y)])

    def mouse_within_garden_limits(self, mouse_coordinates):
        if (self.garden.offset_x <= mouse_coordinates[0] <= (self.garden.offset_x +
                                                             100 * self.garden.plot_size_x)) and (
                self.garden.offset_y <= mouse_coordinates[1] <= (self.garden.offset_y +
                                                                 100 * self.garden.plot_size_y)):

            self.garden.grid_x = clamp(int((mouse_coordinates[0] - self.garden.offset_x) / 100),
                                       self.garden.plot_size_x - 1, 0)
            self.garden.grid_y = clamp(int((mouse_coordinates[1] - self.garden.offset_y) / 100),
                                       self.garden.plot_size_y - 1, 0)
            self.mouse_valid = True
        else:
            self.mouse_valid = False

    def place_plant(self):
        if self.mouse_valid:
            if self.game.currently_placing == "plant1":
                if self.garden_contents[self.garden.grid_x][self.garden.grid_y] is None:
                    self.garden_contents[self.garden.grid_x][self.garden.grid_y] = Plant1()

            if self.game.currently_placing == "plant2":
                if self.garden_contents[self.garden.grid_x][self.garden.grid_y] is None:
                    self.garden_contents[self.garden.grid_x][self.garden.grid_y] = Plant2()

            if self.game.currently_placing == "plant3":
                if self.garden_contents[self.garden.grid_x][self.garden.grid_y] is None:
                    self.garden_contents[self.garden.grid_x][self.garden.grid_y] = Plant3()

    def kill_plant(self):
        self.garden_contents[self.garden.grid_x][self.garden.grid_y] = None

    def draw_plants(self):
        for x in range(len(self.garden_contents)):
            for y in range(len(self.garden_contents[0])):
                if self.garden_contents[x][y] is not None:
                    self.garden_contents[x][y].draw_plant(self.game.game_space, (self.garden.offset_x + x * 100),
                                                          (self.garden.offset_y + y * 100),
                                                          self.garden_contents[x][y].colour)

    def tick_garden(self):
        for x in range(len(self.garden_contents)):
            for y in range(len(self.garden_contents[0])):
                if self.garden_contents[x][y] is not None:
                    if self.garden_contents[x][y].tick_plant():
                        self.garden_contents[x][y] = None

    def draw_garden(self):
        self.garden.draw_base_garden()
        self.garden.draw_overlay_garden(self.mouse_valid)
        self.draw_plants()

