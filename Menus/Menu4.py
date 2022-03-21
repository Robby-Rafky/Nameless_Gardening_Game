from Menus.baseMenu import Menu
from button import Button
from useful_functions import *


class Menu4(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.buttons.append(Button("Option1", (50, 50), (100, 100), (60, 150), True, 20, RED, "Option1"))
        self.buttons.append(Button("Option2", (200, 50), (100, 100), (60, 150), True, 20, BLUE, "Option2"))
        self.buttons.append(Button("Option3", (350, 50), (100, 100), (60, 150), True, 20, BROWN, "Option3"))
        self.buttons.append(Button("Option4", (950, 50), (100, 100), (60, 150), True, 20, GREEN, "Option4"))

    def menu4_menu_events(self):
        if self.buttons[0].button_event_check(self.game.mouse_position):
            print("menu4 menu option1")
        if self.buttons[1].button_event_check(self.game.mouse_position):
            print("menu4 menu option2")
        if self.buttons[2].button_event_check(self.game.mouse_position):
            print("menu4 menu option3")
        if self.buttons[3].button_event_check(self.game.mouse_position):
            print("menu4 menu option4")
