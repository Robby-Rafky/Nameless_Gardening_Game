from useful_functions import *
from Garden.Plants.basePlant import Plant
from Items.plantItem import PlantItem
from Garden.garden import GardenSpace


class GardenHandler:

    def __init__(self, game):
        self.garden = GardenSpace(game)
        self.additional_offset = None
        self.currently_placing = None
        self.game = game
        self.garden_contents = [[None]]
        self.mouse_valid = False
        self.update_plot_size()

        #test
        for _ in range(14):
            self.expand_horizontal()
        for _ in range(8):
            self.expand_vertical()

    def update_plot_size(self):
        self.garden.plot_size_x, self.garden.plot_size_y = len(self.garden_contents[0]), len(self.garden_contents)
        self.additional_offset = [(100 * (15 - self.garden.plot_size_x)) / 2,
                                  (100 * (9 - self.garden.plot_size_y)) / 2]

        self.garden.offset_x = int(self.additional_offset[0]) + 30
        self.garden.offset_y = int(self.additional_offset[1]) + 130

        print(" ")
        for row in self.garden_contents:
            print(row)

    def expand_horizontal(self):
        if self.garden.plot_size_x < 15:
            for row in range(len(self.garden_contents)):
                self.garden_contents[row].append(None)
            self.update_plot_size()

    def expand_vertical(self):
        if self.garden.plot_size_y < 9:
            self.garden_contents.append([None for _ in range(len(self.garden_contents[0]))])
            self.update_plot_size()

    def mouse_within_garden_limits(self):
        if (self.garden.offset_x <= self.game.mouse_position[0] <= (self.garden.offset_x +
                                                                    100 * self.garden.plot_size_x)) and (
                self.garden.offset_y <= self.game.mouse_position[1] <= (self.garden.offset_y +
                                                                        100 * self.garden.plot_size_y)):

            self.garden.grid_x = int((self.game.mouse_position[0] - self.garden.offset_x - 1) / 100)
            self.garden.grid_y = int((self.game.mouse_position[1] - self.garden.offset_y - 1) / 100)

            self.mouse_valid = True
        else:
            self.mouse_valid = False

    def place_on_garden_tile(self):
        if self.mouse_valid:
            if isinstance(self.currently_placing, PlantItem):
                if self.place_plant(self.currently_placing):
                    self.game.inventory_handler.remove_item(self.currently_placing)
                    self.currently_placing = None

    def place_plant(self, plant_item):
        if self.garden_contents[self.garden.grid_y][self.garden.grid_x] is None:
            self.garden_contents[self.garden.grid_y][self.garden.grid_x] = Plant(
                plant_item.stat_growth,
                plant_item.stat_mutation,
                plant_item.stat_yield,
                plant_item.stat_lifespan,
                plant_item.stat_value,
                plant_item.plant_type_1,
                plant_item.plant_type_2,
                plant_item.item_stats_description
            )
        return True

    def harvest_plant(self):
        if self.garden_contents[self.garden.grid_y][self.garden.grid_x] is not None:
            self.garden_contents[self.garden.grid_y][self.garden.grid_x] = None

    def draw_plants(self):
        for y in range(len(self.garden_contents)):
            for x in range(len(self.garden_contents[0])):
                if self.garden_contents[y][x] is not None:
                    self.garden_contents[y][x].draw_plant(self.game.game_space, (self.garden.offset_x + x * 100),
                                                          (self.garden.offset_y + y * 100))

    def tick_garden(self):
        for y in range(len(self.garden_contents)):
            for x in range(len(self.garden_contents[0])):
                if self.garden_contents[y][x] is not None:
                    if self.garden_contents[y][x].tick_plant():
                        if self.garden.currently_clicked == self.garden_contents[y][x]:
                            self.garden.currently_clicked = None
                        self.garden_contents[y][x] = None

    def draw_garden(self):
        self.draw_plants()
        self.garden.draw_base_garden()
        self.garden.draw_overlay_garden()
        self.garden.draw_side_garden_info()

