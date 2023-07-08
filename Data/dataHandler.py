import json


class DataHandler:
    def __init__(self):
        """
        Initialise the class attributes

        :param self.plant_types: dict
        :param self.plant_types_new: Bool
        :param self.passives: dict
        :param self.passives_new: Bool
        :param self.garden_globals: dict
        :param self.garden_globals_new: Bool

        :return: The object itself
        """
        self.plant_types = dict()
        self.plant_types_new = True
        self.passives = dict()
        self.passives_new = True
        self.garden_globals = dict()
        self.garden_globals_new = True
        self.load_all()
        self.save_all()

    def load_all(self):
        """
        initial loading of data
        """
        self.load_passives()
        self.load_plant_types()
        self.load_garden_globals()
        self.passives_new = False
        self.garden_globals_new = False
        self.plant_types_new = False

    def load_plant_types(self):
        """
        Setup of plant type data
        Reads data from
        """
        with open("Data/plantData.json") as f:
            data = json.load(f)
        for item in data:
            self.plant_types[item] = data[item]
        if self.plant_types_new:
            for item in data:
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

    def load_passives(self):
        """
        Setup of skill tree data
        """
        with open("Data/skillTreeData.json") as f:
            data = json.load(f)
        for item in data:
            self.passives[item] = data[item]
        if self.passives_new:
            for item in data:
                self.passives[item]["allocated"] = False
                self.passives[item]["available"] = False
            self.passives["starting_point"]["allocated"] = True
            self.passives["base_passive_1"]["available"] = True

    def load_garden_globals(self):
        """
        Setup of garden globals
        """
        with open("Data/gardenGlobals.json") as f:
            data = json.load(f)
        for item in data:
            self.garden_globals[item] = data[item]
        if self.garden_globals_new:
            for item in data:
                for value in data[item]:
                    self.garden_globals[item][value] = 1

    def save_all(self):
        """
        Runs all 3 data saving methods
        """
        self.save_plant_types()
        self.save_passives()
        self.save_garden_globals()

    def save_plant_types(self):
        """
        Saves plant data
        """
        with open("Data/plantDataTest.json", "w") as w:
            w.write(json.dumps(self.plant_types, indent=2))

    def save_passives(self):
        """
        Saves skill tree data
        """
        with open("Data/skillTreeDataTest.json", "w") as w:
            w.write(json.dumps(self.passives, indent=2))

    def save_garden_globals(self):
        """
        Saves garden data
        """
        with open("Data/gardenGlobalTest.json", "w") as w:
            w.write(json.dumps(self.garden_globals, indent=2))

