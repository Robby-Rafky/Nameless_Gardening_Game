from Menus.baseMenu import Menu
from button import Button
from useful_functions import *
from SkillTree.skillTreeData import skill_tree_data


class SkillTreeMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.all_passives = []
        for item in skill_tree_data:
            self.all_passives.append(Button)

    def skill_tree_menu_events(self):
        pass
