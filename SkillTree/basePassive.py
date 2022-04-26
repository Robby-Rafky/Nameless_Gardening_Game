from useful_functions import *

passive_frame = pygame.image.load("SkillTree/Assets/smallPassiveFrame.png")
passive_inner_frame = pygame.image.load("SkillTree/Assets/smallPassiveInnerFrame.png")


class Passive:
    def __init__(self, passive_type, x, y, passive_id, tier):
        self.passive_type = passive_type
        self.passive_id = passive_id
        self.y = y
        self.x = x
        self.tier = tier
        self.size_x = 100
        self.size_y = 100

        self.rect = pygame.Rect(x, y, self.size_x, self.size_y)

    def passive_events(self, mouse_pos):
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_pos):
                return 1
        elif self.rect.collidepoint(mouse_pos):
            return 2

    def draw_passive(self, surface):
        pass

    def move_passive_pos(self, x, y):
        self.rect = pygame.Rect(x, y, self.size_x, self.size_y)

    def zoom_passive(self, zoom):
        self.rect = pygame.Rect(x, y, self.size_x * zoom, self.size_y * zoom)

