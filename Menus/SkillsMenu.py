import pygame

from Menus.baseMenu import Menu
from SkillTree.basePassive import Passive
from useful_functions import *


# passive data:
# stat: exact name of stat (for specific species) or general name
# target: name of specific species or global
# value: value to be added/subtracted from the target stat
# Order of lists matter, and apply stats to targets in the order they're displayed
# Small passives: Stats + name, No description
# Large passives: stats + name + desc
# The item string is the ID for the passive, but the passive also has its own name


class SkillTreeMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.passive_data = self.game.data_handler.passives
        self.all_passives = []
        self.skill_surface = pygame.Surface((1720, 680))
        self.action_surface = pygame.Surface((1720, 40))
        self.zoom_scale = 0.2
        self.scroll_x = 0
        self.scroll_y = 0
        for item in self.passive_data:
            a = self.passive_data[item]
            self.all_passives.append(Passive(a["type"], a["x"], a["y"], item, a["tier"]))

    def skill_tree_menu_events(self):
        for item in self.all_passives:
            if item.passive_events(self.game.mouse_pos):
                self.passive_data[item.passive_id]["allocated"] = True

    def draw_skill_tree(self):
        self.skill_surface.fill(MENU_GREY)
        self.action_surface.fill(MENU_GREY)

        for item in self.passive_data:
            for connection in self.passive_data[item]["connections"]:
                pos_x = self.passive_data[connection]["x"] * self.zoom_scale + 860
                pos_y = self.passive_data[connection]["y"] * self.zoom_scale + 340
                pos_x2 = self.passive_data[item]["x"] * self.zoom_scale + 860
                pos_y2 = self.passive_data[item]["y"] * self.zoom_scale + 340
                if self.passive_data[connection]["allocated"] and self.passive_data[item]["allocated"]:
                    colour = GREEN
                else:
                    colour = GREY
                pygame.draw.line(self.skill_surface, colour, (pos_x + self.scroll_x * self.zoom_scale,
                                                             pos_y + self.scroll_y * self.zoom_scale),
                                 (pos_x2 + self.scroll_x * self.zoom_scale,
                                  pos_y2 + self.scroll_y * self.zoom_scale),
                                 int(20 * self.zoom_scale))

        for item in self.all_passives:
            item.change_colour(self.passive_data[item.passive_id]["allocated"],
                               item.mouse_over(self.game.mouse_pos), self.zoom_scale * 100)
            item.scaled_x = item.x * self.zoom_scale + 860
            item.scaled_y = item.y * self.zoom_scale + 340
            item.draw_passive(self.skill_surface, self.scroll_x * self.zoom_scale, self.scroll_y * self.zoom_scale)

        pygame.draw.rect(self.skill_surface, BLACK, (0, 0, 1720, 680), 2)
        pygame.draw.rect(self.action_surface, BLACK, (0, 0, 1720, 40), 2)
        self.surface.blit(self.action_surface, (40, 720))
        self.surface.blit(self.skill_surface, (40, 40))
