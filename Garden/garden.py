from useful_functions import *
from textBox import TextBox
from button import Button


class GardenSpace:

    def __init__(self, game):
        self.plot_size_x, self.plot_size_y = 1, 1
        self.offset_x, self.offset_y = None, None
        self.grid_x, self.grid_y = None, None
        self.currently_clicked = None
        self.currently_clicked_index = None
        self.action_box = TextBox(" ", (10, 10), (320, 40), (1560, 120), True, True, 26, MENU_GREY)
        self.timers_box = TextBox(" ", (10, 300), (320, 50), (1560, 120), True, True, 20, MENU_GREY)
        self.types_box = TextBox(" ", (10, 360), (320, 70), (1560, 120), True, False, 24, MENU_GREY)
        self.stats_box = TextBox(" ", (10, 440), (320, 140), (1560, 120), True, False, 24, MENU_GREY)
        self.harvest_button = Button("Harvest", (10, 600), (170, 40), (1560, 120), True, True, 26, GREY)
        self.game = game
        self.side_surface = pygame.Surface((340, 920))

    def draw_base_garden(self):
        for x in range(self.plot_size_x):
            for y in range(self.plot_size_y):
                pygame.draw.rect(self.game.game_space, BLACK, (self.offset_x + x * 100,
                                                               self.offset_y + y * 100,
                                                               100, 100), 1)
        pygame.draw.rect(self.game.game_space, BLACK, (20, 120, 1520, 920), 2)

    def draw_overlay_garden(self):
        if self.game.garden_handler.mouse_valid:
            if pygame.mouse.get_pressed()[0] and self.game.menu_handler.current_menu is None:
                if self.game.garden_handler.currently_placing is None:
                    self.currently_clicked = self.game.garden_handler.garden_contents[self.grid_y][self.grid_x]
                    self.currently_clicked_index = [self.grid_x, self.grid_y]
            else:
                pygame.draw.rect(self.game.game_space, GREY, (self.offset_x + self.grid_x * 100,
                                                              self.offset_y + self.grid_y * 100,
                                                              100, 100), 2)
        if self.currently_clicked_index is not None:
            pygame.draw.rect(self.game.game_space, WHITE, (self.offset_x + self.currently_clicked_index[0] * 100,
                                                           self.offset_y + self.currently_clicked_index[1] * 100,
                                                           100, 100), 3)

    def garden_button_events(self):
        if self.harvest_button.button_event_check(self.game.mouse_position):
            if self.currently_clicked is not None:
                if self.currently_clicked.is_adult():
                    self.game.garden_handler.harvest_plant(self.currently_clicked, self.currently_clicked_index)
                    self.currently_clicked = None

    def draw_side_garden_info(self):
        self.side_surface.fill(GREEN)
        if self.game.garden_handler.currently_placing is not None:
            item = self.game.garden_handler.currently_placing
            item.draw_item(170, 170, self.side_surface, 1)
            pygame.draw.rect(self.side_surface, BLACK, (0, 0, 340, 920), 2)
            self.action_box.update_textbox("Currently Placing", MENU_GREY)
            self.stats_box.update_textbox_multiline(item.item_stats_description, MENU_GREY)
            self.types_box.update_textbox_multiline([item.plant_type_1, item.plant_type_2], MENU_GREY)

            self.types_box.draw_on_surface(self.side_surface)
            self.stats_box.draw_on_surface(self.side_surface)
            self.action_box.draw_on_surface(self.side_surface)
        elif self.currently_clicked is not None:
            self.currently_clicked.draw_plant(self.side_surface, 120, 120)
            pygame.draw.rect(self.side_surface, BLACK, (0, 0, 340, 920), 2)
            self.action_box.update_textbox("Plant Info", MENU_GREY)
            if self.currently_clicked.is_adult():
                self.timers_box.update_textbox("Dies in:  " + self.currently_clicked.get_time_to_death(), MENU_GREY)
            else:
                self.timers_box.update_textbox("Grown in: " + self.currently_clicked.get_time_to_adult(), MENU_GREY)
            self.stats_box.update_textbox_multiline(self.currently_clicked.plant_description, MENU_GREY)
            self.types_box.update_textbox_multiline([self.currently_clicked.plant_type_1,
                                                     self.currently_clicked.plant_type_2], MENU_GREY)

            self.harvest_button.draw_on_surface(self.side_surface)
            self.types_box.draw_on_surface(self.side_surface)
            self.stats_box.draw_on_surface(self.side_surface)
            self.timers_box.draw_on_surface(self.side_surface)
            self.action_box.draw_on_surface(self.side_surface)

        self.game.game_space.blit(self.side_surface, (1560, 120))




