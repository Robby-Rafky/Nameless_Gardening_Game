from useful_functions import *
from SkillTree.basePassive import BasePassive


class SmallPassive(BasePassive):
    def __init__(self, x, y, required, name, tier, description, connections=None):
        BasePassive.__init__(self, x, y, required, name, tier, description, connections)
        # split up to allow for various effects/stat allocations

    def draw_passive(self):
        pass
