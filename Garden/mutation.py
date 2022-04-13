
def mutation_search(recipe, plants_present):
    recipe = sorted(recipe)
    plants_present = sorted(plants_present)
    it = iter(recipe)
    return all(c in it for c in plants_present)
