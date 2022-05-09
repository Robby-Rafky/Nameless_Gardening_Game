from useful_functions import *
from textBox import TextBox

stat_convert = {
    "adult_age": "time to fully grown",
    "adult_mult": "time to fully grown",
    "death_age": "time to death",
    "death_mult": "time to death",
    "yield_mult": "seed yield",
    "growth_mult": "growth rate",
    "value_base": "sell price",
    "value_mult": "sell price",
    "essence_base": "extractable essence",
    "resistance": "resistance",
    "resistance_cap": "maximum resistance",
    "mutation_chance": "mutation chance",
    "res_rate": "resistance reduction rate",
    "stat_magnitude": "seed stat magnitudes",
    "fert_effect": "fertiliser effect"
}


class PassiveInfo:
    def __init__(self):
        self.passive_title = TextBox("", (5, 5), (700, 30), True, True, 22)
        self.passive_tier_title = TextBox("", (710, 5), (105, 30), True, True, 22)
        self.passive_description = TextBox("", (5, 40), (810, 105), True, False, 20)

        self.surface = pygame.Surface((820, 150))

    def draw_passive_info(self, surface, pos):
        self.surface.fill(MENU_GREY)
        self.passive_title.draw_on_surface(self.surface)
        self.passive_tier_title.draw_on_surface(self.surface)
        self.passive_description.draw_on_surface(self.surface)
        pygame.draw.rect(self.surface, BLACK, (0, 0, 820, 150), 2)

        surface.blit(self.surface, (pos[0] - 100, pos[1] - 160))

    def update_keystone_info(self, passive):
        self.passive_title.update_textbox(passive["passive_name"], GREY)
        self.passive_description.update_textbox_multiline(passive["description"], GREY)
        self.passive_tier_title.update_textbox("Tier " + str(passive["tier"]), GREY)

    def update_info(self, passive):
        description = []
        # increase value for all plants by 20%
        for i in range(len(passive["stat"])):
            stat = passive["stat"][i]
            target = passive["target"][i]
            value = passive["value"][i]
            description.append("")
            if value > 0:
                description[i] = "Increase "
            else:
                description[i] = "Reduce "
            value = abs(value)
            description[i] = description[i] + stat_convert[stat]
            if target == "global":
                description[i] = description[i] + " for all plants by "
            else:
                description[i] = description[i] + " for all " + target + " plants by "
            if "mult" in stat or stat == "res_rate" or stat == "stat_magnitude" or stat == "fert_effect":
                description[i] = description[i] + str(value * 100) + "%"
            elif stat == "mutation_chance":
                description[i] = description[i] + str(value) + "%"
            else:
                description[i] = description[i] + str(value)

        self.passive_title.update_textbox(passive["passive_name"], GREY)
        self.passive_description.update_textbox_multiline(description, GREY)
        self.passive_tier_title.update_textbox("Tier " + str(passive["tier"]), GREY)
