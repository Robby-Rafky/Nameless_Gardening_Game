import pygame

from useful_functions import *

small_frame = pygame.image.load("SkillTree/Assets/smallPassiveFrame.png")
small_inner_frame = pygame.image.load("SkillTree/Assets/smallPassiveInnerFrame.png")
medium_frame = pygame.image.load("SkillTree/Assets/mediumPassiveFrame.png")
medium_inner_frame = pygame.image.load("SkillTree/Assets/mediumPassiveInnerFrame.png")
large_frame = pygame.image.load("SkillTree/Assets/largePassiveFrame.png")
large_inner_frame = pygame.image.load("SkillTree/Assets/largePassiveInnerFrame.png")

size_data = {
    "small": [small_frame, small_inner_frame, 100, 10, 0.8],
    "medium": [medium_frame, medium_inner_frame, 150, 10, 0.87],
    "large": [large_frame, large_inner_frame, 200, 10, 0.9]
}


class Passive:
    def __init__(self, passive_type, x, y, passive_id, tier, group):
        self.passive_type = passive_type
        self.passive_id = passive_id
        self.rect_offset = size_data[self.passive_type][3]
        self.size = size_data[self.passive_type][2]
        self.size_rect = self.size * size_data[self.passive_type][4]
        self.ratio_offset = size_data[self.passive_type][3]/size_data[self.passive_type][2]
        self.y = y
        self.scaled_y = y
        self.x = x
        self.scaled_x = x
        self.rect_x = self.x + self.rect_offset-self.size/2
        self.rect_y = self.y + self.rect_offset-self.size/2
        self.tier = tier
        self.image = None
        self.rect = pygame.Rect(self.rect_x + 100, self.rect_y + 190, self.size_rect, self.size_rect)
        self.group = group
        self.colour = tier_colours[self.tier]
        if self.group == "res":
            self.colour = RES_COLOUR
        self.construct_image(GREY, 1)

    def construct_image(self, colour, scale):
        frame_image = size_data[self.passive_type][0].copy()
        inner_image = size_data[self.passive_type][1].copy()
        frame_image_coloured = pygame.Surface(frame_image.get_size())
        inner_image_coloured = pygame.Surface(inner_image.get_size())
        frame_image_coloured.fill(colour)
        inner_image_coloured.fill(self.colour)
        frame_image.blit(frame_image_coloured, (0, 0), special_flags=pygame.BLEND_MULT)
        inner_image.blit(inner_image_coloured, (0, 0), special_flags=pygame.BLEND_MULT)
        inner_image.blit(frame_image, (0, 0))
        modified_scale = scale * size_data[self.passive_type][2]
        inner_image = pygame.transform.scale(inner_image, (modified_scale, modified_scale))
        self.image = inner_image
        self.size = self.image.get_size()[0]
        self.size_rect = self.size * size_data[self.passive_type][4]

    def draw_passive(self, surface, x, y):
        offset = self.ratio_offset * self.size
        self.rect.update(100 + x+self.scaled_x-self.size/2 + offset, 190 + y+self.scaled_y-self.size/2 + offset, self.size_rect, self.size_rect)
        surface.blit(self.image, (x+self.scaled_x-self.size/2, y+self.scaled_y-self.size/2))

    def change_colour(self, allocated, hovered, scale):
        if allocated:
            self.construct_image(GREEN, scale)
        elif hovered:
            self.construct_image(L_ORANGE, scale)
        else:
            self.construct_image(GREY, scale)

    def mouse_over(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if 100 <= mouse_pos[0] <= 1820 and 190 <= mouse_pos[1] <= 910:
                return True

    def passive_events(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if 100 <= mouse_pos[0] <= 1720 and 190 <= mouse_pos[1] <= 870:
                    return True
