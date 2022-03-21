from Menus.baseMenu import Menu
from button import Button
from useful_functions import *


class InventoryMenu(Menu):

    def __init__(self, game):
        Menu.__init__(self, game, MENU_GREY)
        self.buttons.append(Button("Option1", (50, 50), (100, 100), (60, 150), True, 20, RED, "Option1"))
        self.buttons.append(Button("Option2", (200, 50), (100, 100), (60, 150), True, 20, BLUE, "Option2"))
        self.buttons.append(Button("Option3", (350, 50), (100, 100), (60, 150), True, 20, BROWN, "Option3"))
        self.buttons.append(Button("Option4", (550, 50), (100, 100), (60, 150), True, 20, GREEN, "Option4"))

    def inventory_menu_events(self):
        if self.buttons[0].button_event_check(self.game.mouse_position):
            print("inv menu option1")
            self.game.currently_placing = "plant1"
        if self.buttons[1].button_event_check(self.game.mouse_position):
            print("inv menu option2")
            self.game.currently_placing = "plant2"
        if self.buttons[2].button_event_check(self.game.mouse_position):
            print("inv menu option3")
            self.game.currently_placing = "plant3"
        if self.buttons[3].button_event_check(self.game.mouse_position):
            print("inv menu option4")
