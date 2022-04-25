import json


class DataHandler:
    def __init__(self):
        self.plant_types = dict()
        self.plant_types_new = True
        self.passives = dict()
        self.passives_new = True
        self.garden_globals = dict()
        self.garden_globals_new = True
        self.load_all()
        self.save_all()

    def load_all(self):
        self.load_passives()
        self.load_plant_types()
        self.load_garden_globals()
        self.passives_new = False
        self.garden_globals_new = False
        self.plant_types_new = False

    def load_plant_types(self):
        with open("Data/plantData.json") as f:
            data = json.load(f)
        if self.plant_types_new:
            for item in data:
                self.plant_types[item] = data[item]
                self.plant_types[item]["adult_age"][0:2] = data[item]["adult_age"][2:4]
                self.plant_types[item]["adult_mult"][0:2] = data[item]["adult_mult"][2:4]
                self.plant_types[item]["death_age"][0:2] = data[item]["death_age"][2:4]
                self.plant_types[item]["death_mult"][0:2] = data[item]["death_mult"][2:4]
                self.plant_types[item]["yield_mult"][0:2] = data[item]["yield_mult"][2:4]
                self.plant_types[item]["growth_mult"][0:2] = data[item]["growth_mult"][2:4]
                self.plant_types[item]["value_base"][0:2] = data[item]["value_base"][2:4]
                self.plant_types[item]["value_mult"][0:2] = data[item]["value_mult"][2:4]
                self.plant_types[item]["essence_base"][0:2] = data[item]["essence_base"][2:4]
                self.plant_types[item]["mutation_chance"][0:1] = data[item]["mutation_chance"][1:2]

        else:
            for item in data["plantSpecies"]:
                type_name = item["type_name"]
                self.plant_types[type_name] = item

    def load_passives(self):
        pass

    def load_garden_globals(self):
        pass

    def save_all(self):
        self.save_plant_types()
        self.save_passives()
        self.save_garden_globals()

    def save_plant_types(self):
        with open("Data/plantDataTest.json", "w") as w:
            w.write(json.dumps(self.plant_types, indent=2))

    def save_passives(self):
        pass

    def save_garden_globals(self):
        pass

