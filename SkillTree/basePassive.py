from useful_functions import *


class BasePassive:
    def __init__(self, x, y, required, name, tier, description, connections):
        if connections is None:
            connections = []
        self.y = y
        self.x = x
        self.required = required
        self.name = name
        self.description = description

        self.is_allocated = False

        self.rect = pygame.Rect(x, y, 100, 100)

    def passive_events(self, mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_coordinates):
                return True
                pass
            return False

    def move_passive_pos(self, x, y):
        self.rect = pygame.Rect(x, y)
        pass

    def zoom_passive(self, zoom):
        pass

