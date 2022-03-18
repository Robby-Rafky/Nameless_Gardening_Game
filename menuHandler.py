from useful_functions import *
from baseMenu import Menu


class MenuHandler:

    def __init__(self):
        self.current_menu = None
        self.test_menu = Menu(self, MENU_GREY)

    def draw_current_menu(self):
        if self.current_menu == "test":
            self.test_menu.show_menu_background()

    def current_menu_event_check(self, event):
        # event checking in each specific menu
        if event.type == pygame.K_ESCAPE:
            self.current_menu = None
        if self.current_menu == "test":
            pass
