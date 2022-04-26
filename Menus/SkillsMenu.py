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
        for item in self.passive_data:
            a = self.passive_data[item]
            self.all_passives.append(Passive(a["type"], a["x"], a["y"], item, a["tier"]))

    def skill_tree_menu_events(self):
        pass

    def draw_skill_tree(self):
        self.skill_surface.fill(MENU_GREY)
        self.action_surface.fill(MENU_GREY)
        pygame.draw.rect(self.skill_surface, BLACK, (0, 0, 1720, 720), 2)
        pygame.draw.rect(self.action_surface, BLACK, (0, 0, 1720, 40), 2)
        self.surface.blit(self.action_surface, (40, 720))
        self.surface.blit(self.skill_surface, (40, 40))
