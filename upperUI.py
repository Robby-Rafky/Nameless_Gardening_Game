from useful_functions import *
from menuHandler import MenuHandler
from button import Button


class MenuSwitcher:
    def __init__(self):
        self.menu_handler = MenuHandler()
        self.button_1 = Button("1", (0, 0), (300, 70), 20, GREY, "open")
        self.button_2 = Button("2", (375, 0), (300, 70), 20, GREY, "open")
        self.button_3 = Button("3", (750, 0), (300, 70), 20, GREY, "open")
        self.button_4 = Button("4", (1125, 0), (300, 70), 20, GREY, "open")
        self.button_5 = Button("5", (1500, 0), (300, 70), 20, GREY, "open")
        self.surface = pygame.Surface((1800, 70))
        self.surface.fill(GREEN)
        self.button_1.pack_button(self.surface)
        self.button_2.pack_button(self.surface)
        self.button_3.pack_button(self.surface)
        self.button_4.pack_button(self.surface)
        self.button_5.pack_button(self.surface)
