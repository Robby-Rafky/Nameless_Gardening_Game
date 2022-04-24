from useful_functions import *
from SkillTree.smallPassive import SmallPassive

skill_tree_data = {
    "stuff": SmallPassive(
        x=1000,
        y=2000,
        required="im",
        name="stuff",
        tier=4,
        description="ye",
        connections=["ye"]
    ),
    "im": SmallPassive(
        x=2000,
        y=1000,
        required="im",
        name="stuff",
        tier=0,
        description="ye2"
    )
}
