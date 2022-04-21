from useful_functions import *
from Garden.Plants.basePlant import Plant
from Items.plantItem import PlantItem
from Garden.garden import GardenSpace
from Garden.Targeting import Targeter
from Garden.PlantManipulation.mutation import Mutator


class GardenHandler:

    def __init__(self, game):
        self.garden = GardenSpace(game)
        self.targeter = Targeter(game)
        self.additional_offset = None
        self.planting = None
        self.game = game
        self.garden_contents = [[None]]
        self.mouse_valid = False
        self.update_plot_size()

        for _ in range(4):
            self.expand_vertical()
            self.expand_horizontal()

    def update_plot_size(self):
        self.garden.size_x, self.garden.size_y = len(self.garden_contents[0]), len(self.garden_contents)
        self.additional_offset = [(100 * (15 - self.garden.size_x)) / 2,
                                  (100 * (9 - self.garden.size_y)) / 2]

        self.garden.offset_x = int(self.additional_offset[0]) + 30
        self.garden.offset_y = int(self.additional_offset[1]) + 130

    def expand_horizontal(self):
        if self.garden.size_x < 15:
            for row in range(len(self.garden_contents)):
                self.garden_contents[row].append(None)
            self.update_plot_size()
            self.targeter.limit_x = self.garden.size_x - 1

    def expand_vertical(self):
        if self.garden.size_y < 9:
            self.garden_contents.append([None for _ in range(len(self.garden_contents[0]))])
            self.update_plot_size()
            self.targeter.limit_y = self.garden.size_y - 1

    def mouse_within_garden_limits(self):
        if (self.garden.offset_x <= self.game.mouse_pos[0] <= (self.garden.offset_x +
                                                               100 * self.garden.size_x)) and (
                self.garden.offset_y <= self.game.mouse_pos[1] <= (self.garden.offset_y +
                                                                   100 * self.garden.size_y)):

            self.garden.grid_x = int((self.game.mouse_pos[0] - self.garden.offset_x - 1) / 100)
            self.garden.grid_y = int((self.game.mouse_pos[1] - self.garden.offset_y - 1) / 100)

            self.mouse_valid = True
        else:
            self.mouse_valid = False

    def place_on_garden_tile(self):
        if self.mouse_valid:
            if isinstance(self.planting, PlantItem):
                if self.place_plant(self.planting):
                    self.game.inventory_handler.remove_item(self.planting)
                    self.planting = None
            if isinstance(self.planting, Mutator):
                if self.garden_contents[self.garden.grid_y][self.garden.grid_x] is None:
                    self.game.user.purchase_check(self.game.menu_handler.shop_menu.buy_mutator.price)
                    self.planting.x = self.garden.grid_x
                    self.planting.y = self.garden.grid_y
                    self.garden_contents[self.garden.grid_y][self.garden.grid_x] = self.planting
                    self.planting = None

    def place_plant(self, plant_item):
        if self.garden_contents[self.garden.grid_y][self.garden.grid_x] is None:
            self.garden_contents[self.garden.grid_y][self.garden.grid_x] = Plant(
                plant_item.stat_growth,
                plant_item.stat_yield,
                plant_item.stat_lifespan,
                plant_item.stat_value,
                self.garden.grid_x,
                self.garden.grid_y,
                plant_item.type1,
                plant_item.type2,
                self.game,
            )
            return True
        else:
            return False

    # some plants might give extra stuff when harvested (crystalline -> valuable crystals to sell)
    def harvest_plant(self, plant, garden_index):
        seed_count = self.garden_contents[garden_index[1]][garden_index[0]].final_yield
        final_seed_count = int(seed_count / 100)
        if chance_to_occur(seed_count % 100):
            final_seed_count += 1
        for _ in range(final_seed_count):
            self.game.inventory_handler.add_item(PlantItem(
                plant.stat_growth,
                plant.stat_yield,
                plant.stat_lifespan,
                plant.stat_value,
                plant.type1,
                plant.type2,
            ))
        pygame.event.post(pygame.event.Event(self.game.plant_state_changed, message=[[garden_index[1],
                                                                                      garden_index[0]]]))
        self.garden_contents[garden_index[1]][garden_index[0]] = None

    def draw_plants(self):
        for x in range(len(self.garden_contents)):
            for y in range(len(self.garden_contents[0])):
                if isinstance(self.garden_contents[y][x], Plant):
                    self.garden_contents[y][x].draw_plant(self.game.game_space, (self.garden.offset_x + x * 100),
                                                          (self.garden.offset_y + y * 100))
                if isinstance(self.garden_contents[y][x], Mutator):
                    self.garden_contents[y][x].draw_mutator(self.game.game_space, (self.garden.offset_x + x * 100),
                                                            (self.garden.offset_y + y * 100))

    def tick_garden(self):
        garden_update = []
        for x in range(len(self.garden_contents)):
            for y in range(len(self.garden_contents[0])):
                if isinstance(self.garden_contents[x][y], Plant):
                    action = self.garden_contents[x][y].tick_plant()
                    if action == 0:
                        garden_update.append((x, y))
                    elif action == 1:
                        if self.garden.clicked_plot == self.garden_contents[x][y]:
                            self.garden.clicked_plot = None
                        self.garden_contents[x][y] = None
                        garden_update.append((x, y))
                if isinstance(self.garden_contents[x][y], Mutator):
                    self.garden_contents[x][y].trigger_mutation_rolls()
        if len(garden_update) != 0:
            pygame.event.post(pygame.event.Event(self.game.plant_state_changed, message=garden_update))

    def update_plant_stats(self):
        for y in range(len(self.garden_contents)):
            for x in range(len(self.garden_contents[0])):
                if self.garden_contents[y][x] is not None:
                    self.garden_contents[y][x].update_final_values()

    def update_non_plants(self, x, y):
        for tile in self.targeter.target_area(1, x, y):
            if isinstance(self.garden_contents[tile[0]][tile[1]], Mutator):
                self.garden_contents[tile[0]][tile[1]].search_for_plants()


    def draw_garden(self):
        self.draw_plants()
        self.garden.draw_base_garden()
        self.garden.draw_overlay_garden()
        self.garden.draw_side_garden_info()
