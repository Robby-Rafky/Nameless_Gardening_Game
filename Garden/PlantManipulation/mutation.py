from useful_functions import *
from Garden.Plants.basePlant import Plant

mutator_image = pygame.image.load("Garden/PlantManipulation/asset_mutator.png")

mutator_tiers = {
    1: [tier_colours[0], 200],
    2: [tier_colours[2], 300],
    3: [tier_colours[3], 400],
    4: [tier_colours[4], 500],
    5: [tier_colours[5], 600],
    6: [tier_colours[6], 700],
    7: [tier_colours[7], None]
}


class Mutator:
    """
    A class representing a mutator in the garden.

    Attributes:
        game (Game): The game instance.
        types (dict): The dictionary of plant types from the game's data handler.
        tier (int): The tier of the mutator.
        x (int): The x-coordinate position of the mutator.
        y (int): The y-coordinate position of the mutator.
        plants_present (list): The list of plants present near the mutator.
        can_mutate (list): The list of plants that can mutate.
        image (pygame.Surface): The image representation of the mutator.

    Methods:
        __init__(self, x, y, game, tier, actual): Initialize the Mutator instance.
        create_image(self): Create the image of the mutator.
        create_translucent(self): Create a translucent representation of the mutator.
        draw_mutator(self, surface, pos_x, pos_y): Draw the mutator on a surface.
        search_for_plants(self): Search for plants near the mutator and populate the plants_present and can_mutate lists.
        mutation_search(self, recipe, plants_present): Check if a mutation recipe is satisfied by the plants present.
        trigger_mutation_rolls(self): Trigger mutation rolls for the plants that can mutate.
        get_price(self): Get the price of the mutator.
    """

    def __init__(self, x, y, game, tier, actual):
        """Initialize the Mutator instance.

            Args:
                x (int): The x-coordinate position of the mutator.
                y (int): The y-coordinate position of the mutator.
                game (Game): The game instance.
                tier (int): The tier of the mutator.
                actual (bool): Indicates whether the mutator is an actual mutator or a translucent representation.
        """
        self.game = game
        self.types = self.game.data_handler.plant_types
        self.tier = tier
        self.x = x
        self.y = y
        self.plants_present = []
        self.can_mutate = []
        if actual:
            self.image = self.create_image()
        else:
            self.image = self.create_translucent()

    def create_image(self):
        """Create the image of the mutator.

        Returns:
            pygame.Surface: The final image of the mutator.
        """
        mutator_image_final = mutator_image.copy()
        mutator_coloured = pygame.Surface(mutator_image.get_size())
        mutator_coloured.fill(mutator_tiers[self.tier][0])
        mutator_image_final.blit(mutator_coloured, (0, 0), special_flags=pygame.BLEND_MULT)

        return mutator_image_final

    def create_translucent(self):
        """Create a translucent representation of the mutator.

        Returns:
            pygame.Surface: The translucent image of the mutator.
        """
        image = self.create_image()
        translucent_image = image.convert_alpha()
        translucent_image.set_alpha(130)

        return translucent_image

    def draw_mutator(self, surface, pos_x, pos_y):
        """Draw the mutator on a surface.

        Args:
            surface (pygame.Surface): The surface to draw the mutator on.
            pos_x (int): The x-coordinate position to draw the mutator.
            pos_y (int): The y-coordinate position to draw the mutator.
        """
        surface.blit(self.image, (pos_x, pos_y))

    def search_for_plants(self):
        """Search for plants near the mutator and populate the plants_present and can_mutate lists."""
        self.plants_present.clear()
        self.can_mutate.clear()
        for plant_pos in self.game.garden_handler.targeter.target_area(1, self.y, self.x):
            plant = self.game.garden_handler.garden_contents[plant_pos[0]][plant_pos[1]]
            if isinstance(plant, Plant):
                if plant.is_pure and plant.is_adult:
                    if plant.is_max:
                        self.plants_present.append(plant.type1["type_name"] + " [Max]")
                        self.plants_present.append(plant.type1["type_name"])
                    else:
                        self.plants_present.append(plant.type1["type_name"])
        for plant_type, plant in self.types.items():
            if self.mutation_search(plant["mutation_recipe"], self.plants_present) and plant["tier"] <= self.tier:
                self.can_mutate.append(plant_type)

    def mutation_search(self, recipe, plants_present):
        """Check if a mutation recipe is satisfied by the plants present.

        Args:
            recipe (list): The mutation recipe to check.
            plants_present (list): The list of plants present.

        Returns:
            bool: True if the mutation recipe is satisfied, False otherwise.
        """
        recipe = sorted(recipe)
        plants_present = sorted(plants_present)
        it = iter(plants_present)
        return all(c in it for c in recipe)

    def trigger_mutation_rolls(self):
        """Trigger mutation rolls for the plants that can mutate."""
        for item in self.can_mutate:
            if small_chance_to_occur(self.types[item]["mutation_chance"][0]):
                self.game.garden_handler.garden_contents[self.y][self.x] = Plant(
                    0, 0, 0, 0, self.x, self.y, item, item, self.game)
                self.game.garden_handler.garden.clicked_plot = None

    def get_price(self):
        """Get the price of the mutator.

        Returns:
            int: The price of the mutator.
        """
        return mutator_tiers[self.tier][1]

