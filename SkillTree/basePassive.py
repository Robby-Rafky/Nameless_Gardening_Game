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
    """Represents a passive skill in a skill tree.

    Attributes:
        passive_type (str): The type of the passive skill (small, medium, or large).
        x (int): The x-coordinate of the passive skill's position in the skill tree.
        y (int): The y-coordinate of the passive skill's position in the skill tree.
        passive_id (str): The unique identifier of the passive skill.
        tier (int): The tier of the passive skill.
        group (str): The group to which the passive skill belongs (e.g., "res" for resistance group).
        rect_offset (int): The offset value for positioning the passive skill's rectangular area.
        size (int): The size of the passive skill's image.
        size_rect (int): The scaled size of the passive skill's image.
        ratio_offset (float): The ratio offset for positioning the passive skill's image within the rectangular area.
        y_scaled (int): The scaled y-coordinate of the passive skill's position.
        x_scaled (int): The scaled x-coordinate of the passive skill's position.
        rect_x (int): The x-coordinate of the rectangular area enclosing the passive skill's image.
        rect_y (int): The y-coordinate of the rectangular area enclosing the passive skill's image.
        image (pygame.Surface): The image of the passive skill.
        rect (pygame.Rect): The rectangular area enclosing the passive skill's image.
        colour (tuple): The colour of the passive skill based on its tier or group.

    Methods:
        __init__(passive_type, x, y, passive_id, tier, group):
            Initializes a new instance of the Passive class.
        construct_image(colour, scale):
            Constructs the image of the passive skill by blending frame and inner images.
        draw_passive(surface, x, y):
            Draws the passive skill on a given surface at the specified coordinates.
        change_colour(allocated, available, hovered, scale):
            Changes the colour of the passive skill based on its status (allocated, available, hovered).
        mouse_over(mouse_pos):
            Checks if the mouse is over the passive skill.
        passive_events(mouse_pos):
            Handles the events related to the passive skill.
    """

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
        """Constructs the image of the passive skill.

        The constructed image is a blend of the frame and inner images, with a specified colour and scale.

        Args:
            colour (tuple): The colour of the passive skill.
            scale (float): The scale factor applied to the passive skill's size.
        """
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
        """
        Draws the passive skill on a given surface at the specified coordinates.

        Args:
            surface (pygame.Surface): The surface to draw the passive skill on.
            x (int): The x-coordinate of the drawing position.
            y (int): The y-coordinate of the drawing position.
        """
        offset = self.ratio_offset * self.size
        self.rect.update(100 + x+self.scaled_x-self.size/2 + offset, 190 + y+self.scaled_y-self.size/2 + offset, self.size_rect, self.size_rect)
        surface.blit(self.image, (x+self.scaled_x-self.size/2, y+self.scaled_y-self.size/2))

    def change_colour(self, allocated, available, hovered, scale):
        """
        Changes the colour of the passive skill based on its status (allocated, available, hovered).

        Args:
            allocated (bool): Indicates if the passive skill is allocated.
            available (bool): Indicates if the passive skill is available for allocation.
            hovered (bool): Indicates if the passive skill is being hovered over.
            scale (float): The scale factor applied to the passive skill's size.
        """
        if allocated:
            self.construct_image(SKILL_ALLOCATED, scale)
        elif hovered:
            self.construct_image(SKILL_HOVER, scale)
        elif available:
            self.construct_image(SKILL_AVAILABLE, scale)
        else:
            self.construct_image(SKILL_UNAVAILABLE, scale)

    def mouse_over(self, mouse_pos):
        """
        Checks if the mouse is over the passive skill.

        Args:
            mouse_pos (tuple): The current position of the mouse.

        Returns:
            bool: True if the mouse is over the passive skill, False otherwise.
        """
        if self.rect.collidepoint(mouse_pos):
            if 100 <= mouse_pos[0] <= 1820 and 190 <= mouse_pos[1] <= 910:
                return True

    def passive_events(self, mouse_pos):
        """
        Handles the events related to the passive skill.

        Args:
            mouse_pos (tuple): The current position of the mouse.

        Returns:
            bool: True if the passive skill's event is triggered, False otherwise.
        """
        if self.rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                if 100 <= mouse_pos[0] <= 1720 and 190 <= mouse_pos[1] <= 870:
                    return True
