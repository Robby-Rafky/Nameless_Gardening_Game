from useful_functions import *
from Garden.Plants.basePlant import Plant
from Garden.Plants.plantSpecies import plant_species

mutator_image = pygame.image.load("Garden/PlantManipulation/asset_mutator.png")

mutator_tiers = {
    1: [(160, 159, 161), 200],
    2: [(35, 68, 219), 300],
    3: [(80, 28, 201), 400],
    4: [(217, 168, 9), 500],
    5: [(220, 129, 247), 600],
    6: [(14, 215, 237), 700],
    7: [(184, 0, 0), None]
}


class Mutator:
    def __init__(self, x, y, game, tier):
        self.game = game
        self.tier = tier
        self.x = x
        self.y = y
        self.plants_present = []
        self.can_mutate = []
        self.image = self.create_image()

    def create_image(self):
        mutator_image_final = mutator_image.copy()
        mutator_coloured = pygame.Surface(mutator_image.get_size())
        mutator_coloured.fill(mutator_tiers[self.tier][0])
        mutator_image_final.blit(mutator_coloured, (0, 0), special_flags=pygame.BLEND_MULT)

        return mutator_image_final

    def draw_mutator(self, surface, pos_x, pos_y):
        surface.blit(self.image, (pos_x, pos_y))

    def search_for_plants(self):
        self.plants_present.clear()
        self.can_mutate.clear()
        for plant_pos in self.game.garden_handler.targeter.target_area(1, self.y, self.x):
            plant = self.game.garden_handler.garden_contents[plant_pos[0]][plant_pos[1]]
            if isinstance(plant, Plant):
                if plant.is_pure and plant.is_adult:
                    if plant.is_max:
                        self.plants_present.append(plant.type1 + " [Max]")
                        self.plants_present.append(plant.type1)
                    else:
                        self.plants_present.append(plant.type1)
        for plant_type, plant in plant_species.items():
            if self.mutation_search(plant.recipe, self.plants_present) and plant.tier <= self.tier:
                self.can_mutate.append(plant_type)

    def mutation_search(self, recipe, plants_present):
        recipe = sorted(recipe)
        plants_present = sorted(plants_present)
        it = iter(plants_present)
        return all(c in it for c in recipe)

    def trigger_mutation_rolls(self):
        for item in self.can_mutate:
            if small_chance_to_occur(plant_species[item].mutation_chance):
                self.game.garden_handler.garden_contents[self.y][self.x] = Plant(
                    0, 0, 0, 0, self.x, self.y, item, item, self.game)
                self.game.garden_handler.garden.clicked_plot = None

    def get_price(self):
        return mutator_tiers[self.tier][1]

