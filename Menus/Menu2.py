from baseMenu import Menu
from button import Button
from useful_functions import *


class ShopMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.buttons.append(Button("Option1", (50, 250), (100, 100), (60, 150), True, 20, RED, "Option1"))
        self.buttons.append(Button("Option3", (250, 250), (100, 100), (60, 150), True, 20, BROWN, "Option3"))
        self.buttons.append(Button("Option4", (350, 250), (100, 100), (60, 150), True, 20, GREEN, "Option4"))

    def shop_menu_events(self):
        if self.buttons[0].button_event_check(self.game.mouse_position):
            print("shop menu option1")
        if self.buttons[1].button_event_check(self.game.mouse_position):
            print("shop menu option2")
        if self.buttons[2].button_event_check(self.game.mouse_position):
            print("shop menu option3")

