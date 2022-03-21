from Menus.baseMenu import Menu
from button import Button
from useful_functions import *


class SkillTreeMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.buttons.append(Button("Option1", (50, 150), (100, 100), (60, 150), True, 20, RED, "Option1"))
        self.buttons.append(Button("Option2", (200, 150), (100, 100), (60, 150), True, 20, BLUE, "Option2"))
        self.buttons.append(Button("Option4", (350, 150), (100, 100), (60, 150), True, 20, GREEN, "Option4"))

    def skill_tree_menu_events(self):
        if self.buttons[0].button_event_check(self.game.mouse_position):
            print("skill tree menu option1")
        if self.buttons[1].button_event_check(self.game.mouse_position):
            print("skill tree menu option2")
        if self.buttons[2].button_event_check(self.game.mouse_position):
            print("skill tree menu option3")
