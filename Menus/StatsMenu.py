from Menus.baseMenu import Menu
from button import Button
from useful_functions import *


class StatsMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.buttons.append(Button("Option2", (200, 150), (100, 100), (60, 150), True, 20, BLUE, "Option2"))
        self.buttons.append(Button("Option3", (350, 250), (100, 100), (60, 150), True, 20, BROWN, "Option3"))
        self.buttons.append(Button("Option4", (1550, 350), (100, 100), (60, 150), True, 20, GREEN, "Option4"))

    def stats_menu_events(self):
        if self.buttons[0].button_event_check(self.game.mouse_position):
            print("stat menu option1")
        if self.buttons[1].button_event_check(self.game.mouse_position):
            print("stat menu option2")
        if self.buttons[2].button_event_check(self.game.mouse_position):
            print("stat menu option3")

