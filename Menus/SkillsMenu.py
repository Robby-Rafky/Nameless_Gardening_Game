from Menus.baseMenu import Menu
from SkillTree.basePassive import Passive
from useful_functions import *
from SkillTree.passiveInfo import PassiveInfo


# passive data:
# stat: exact name of stat (for specific species) or general name
# target: name of specific species or global
# value: value to be added/subtracted from the target stat
# Order of lists matter, and apply stats to targets in the order they're displayed
# Small passives: Stats + name, No description
# Large passives: stats + name + desc
# The item string is the ID for the passive, but the passive also has its own name
# Search connections for stuff to be required before allocation (using OR)
# Requirements are optional, and dont have to be connected (using AND)


class SkillTreeMenu(Menu):
    """
    A class representing the skill tree menu.

    The SkillTreeMenu class extends the base Menu class and provides functionality for displaying and handling events in
    the skill tree menu. It allows the player to allocate passive skills, view skill connections, and see skill details.

    Attributes:
        game (Game): The game instance.
        passive_info (PassiveInfo): The instance of the PassiveInfo class for displaying passive skill information.
        passive_data (dict): The data for all passive skills in the skill tree.
        all_passives (list): A list of all passive skill instances in the skill tree.
        skill_surface (Surface): The surface for rendering the skill tree.
        action_surface (Surface): The surface for rendering the action bar.
        zoom_scale (float): The current zoom scale of the skill tree.
        scroll_x (float): The current horizontal scroll position of the skill tree.
        scroll_y (float): The current vertical scroll position of the skill tree.

    Methods:
        __init__(self, game): Initialize the SkillTreeMenu instance.
        skill_tree_menu_events(self): Handle the events in the skill tree menu.
        draw_skill_tree(self): Draw the skill tree on the skill tree menu surface.
    """

    def __init__(self, game):
        """
        Initialize the SkillTreeMenu instance.

        Args:
            game (Game): The game instance.
        """
        Menu.__init__(self, game, MENU_GREY)
        self.passive_info = PassiveInfo()
        self.passive_data = self.game.data_handler.passives
        self.all_passives = []
        self.skill_surface = pygame.Surface((1720, 680))
        self.action_surface = pygame.Surface((1720, 40))
        self.zoom_scale = 0.2
        self.scroll_x = 9000
        self.scroll_y = 400
        for item in self.passive_data:
            a = self.passive_data[item]
            self.all_passives.append(Passive(a["type"], a["x"], a["y"], item, a["tier"], a["group"]))

    def skill_tree_menu_events(self):
        """Handle the events in the skill tree menu."""
        for item in self.all_passives:
            if item.passive_events(self.game.mouse_pos):
                if self.passive_data[item.passive_id]["available"]:
                    self.passive_data[item.passive_id]["allocated"] = True
                    self.passive_data[item.passive_id]["available"] = False
                    for connection in self.passive_data[item.passive_id]["connections"]:
                        self.passive_data[connection]["available"] = True
                    for passive in self.passive_data:
                        if self.passive_data[passive]["required"]:
                            reqs_met = True
                            for requirement in self.passive_data[passive]["required"]:
                                if not self.passive_data[requirement]["allocated"]:
                                    reqs_met = False
                            if reqs_met:
                                self.passive_data[passive]["available"] = True

    def draw_skill_tree(self):
        """Draw the skill tree on the skill tree menu surface."""
        self.skill_surface.fill(D_GREY)
        self.action_surface.fill(MENU_GREY)
        looking_at = [860 - self.scroll_x, 340 - self.scroll_y]

        for item in self.passive_data:
            for connection in self.passive_data[item]["connections"]:
                pos_x = (self.scroll_x - self.passive_data[connection]["x"]) * self.zoom_scale + self.scroll_x
                pos_y = (self.scroll_y - self.passive_data[connection]["y"]) * self.zoom_scale + self.scroll_y
                pos_x2 = (self.scroll_x - self.passive_data[item]["x"]) * self.zoom_scale + self.scroll_x
                pos_y2 = (self.scroll_y - self.passive_data[item]["y"]) * self.zoom_scale + self.scroll_y
                if self.passive_data[connection]["allocated"] and self.passive_data[item]["allocated"]:
                    colour = SKILL_ALLOCATED
                elif self.passive_data[connection]["allocated"] and self.passive_data[item]["available"]:
                    colour = SKILL_AVAILABLE
                elif self.passive_data[connection]["available"] and self.passive_data[item]["allocated"]:
                    colour = SKILL_AVAILABLE
                else:
                    colour = SKILL_UNAVAILABLE
                pygame.draw.line(self.skill_surface, colour, (pos_x + looking_at[0],
                                                              pos_y + looking_at[1]),
                                 (pos_x2 + looking_at[0],
                                  pos_y2 + looking_at[1]),
                                 int(20 * self.zoom_scale))

        passive_hovered = None
        for item in self.all_passives:
            item.change_colour(self.passive_data[item.passive_id]["allocated"],
                               self.passive_data[item.passive_id]["available"],
                               item.mouse_over(self.game.mouse_pos), self.zoom_scale)
            if item.mouse_over(self.game.mouse_pos):
                passive_hovered = item
            item.scaled_x = (self.scroll_x - item.x) * self.zoom_scale + self.scroll_x
            item.scaled_y = (self.scroll_y - item.y) * self.zoom_scale + self.scroll_y

            item.draw_passive(self.skill_surface, looking_at[0], looking_at[1])

        if passive_hovered is not None:
            self.passive_info.update_info(self.passive_data[passive_hovered.passive_id])
            #self.passive_info.update_keystone_info(self.passive_data[passive_hovered.passive_id])
            self.passive_info.draw_passive_info(self.skill_surface, self.game.mouse_pos)

        pygame.draw.rect(self.skill_surface, BLACK, (0, 0, 1720, 680), 2)
        pygame.draw.rect(self.action_surface, BLACK, (0, 0, 1720, 40), 2)
        self.surface.blit(self.action_surface, (40, 720))
        self.surface.blit(self.skill_surface, (40, 40))
