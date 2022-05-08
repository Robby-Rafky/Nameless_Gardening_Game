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
# Search connections for stuff to be required before allocation (using OR)
# Requirements are optional, and dont have to be connected (using AND)


class SkillTreeMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.passive_data = self.game.data_handler.passives
        self.all_passives = []
        self.skill_surface = pygame.Surface((1720, 680))
        self.action_surface = pygame.Surface((1720, 40))
        self.zoom_scale = 0.2
        self.scroll_x = 9000
        self.scroll_y = 400
        for item in self.passive_data:
            a = self.passive_data[item]
            self.all_passives.append(Passive(a["type"], a["x"], a["y"], item, a["tier"], a["group"]))

    def skill_tree_menu_events(self):
        for item in self.all_passives:
            if item.passive_events(self.game.mouse_pos):
                allocatable = False
                for connection in self.passive_data[item.passive_id]["connections"]:
                    if self.passive_data[connection]["allocated"]:
                        allocatable = True
                if not self.passive_data[item.passive_id]["required"]:
                    requirements_met = False
                else:
                    requirements_met = True
                for requirement in self.passive_data[item.passive_id]["required"]:
                    if not self.passive_data[requirement]["allocated"]:
                        requirements_met = False
                if allocatable or requirements_met:
                    self.passive_data[item.passive_id]["allocated"] = True

    def draw_skill_tree(self):
        self.skill_surface.fill(MENU_GREY)
        self.action_surface.fill(MENU_GREY)
        looking_at = [860 - self.scroll_x, 340 - self.scroll_y]

        for item in self.passive_data:
            for connection in self.passive_data[item]["connections"]:
                pos_x = (self.scroll_x - self.passive_data[connection]["x"]) * self.zoom_scale + self.scroll_x
                pos_y = (self.scroll_y - self.passive_data[connection]["y"]) * self.zoom_scale + self.scroll_y
                pos_x2 = (self.scroll_x - self.passive_data[item]["x"]) * self.zoom_scale + self.scroll_x
                pos_y2 = (self.scroll_y - self.passive_data[item]["y"]) * self.zoom_scale + self.scroll_y
                if self.passive_data[connection]["allocated"] and self.passive_data[item]["allocated"]:
                    colour = GREEN
                else:
                    colour = GREY
                pygame.draw.line(self.skill_surface, colour, (pos_x + looking_at[0],
                                                              pos_y + looking_at[1]),
                                 (pos_x2 + looking_at[0],
                                  pos_y2 + looking_at[1]),
                                 int(20 * self.zoom_scale))

        for item in self.all_passives:
            item.change_colour(self.passive_data[item.passive_id]["allocated"],
                               item.mouse_over(self.game.mouse_pos), self.zoom_scale)

            item.scaled_x = (self.scroll_x - item.x) * self.zoom_scale + self.scroll_x
            item.scaled_y = (self.scroll_y - item.y) * self.zoom_scale + self.scroll_y

            item.draw_passive(self.skill_surface, looking_at[0], looking_at[1])

        pygame.draw.rect(self.skill_surface, BLACK, (0, 0, 1720, 680), 2)
        pygame.draw.rect(self.action_surface, BLACK, (0, 0, 1720, 40), 2)
        self.surface.blit(self.action_surface, (40, 720))
        self.surface.blit(self.skill_surface, (40, 40))
