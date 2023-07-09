import json


class DataHandler:
    """A class for handling data related to plant types, passives, and garden globals.

    The DataHandler class provides methods for loading, saving, and manipulating data related to plant types, passives,
    and garden globals. It loads the data from JSON files, stores them in dictionaries, and allows access to the data.

    Attributes:
        plant_types (dict): A dictionary containing the plant types data.
        plant_types_new (bool): A flag indicating if the plant types data is new.
        passives (dict): A dictionary containing the passives data.
        passives_new (bool): A flag indicating if the passives data is new.
        garden_globals (dict): A dictionary containing the garden globals data.
        garden_globals_new (bool): A flag indicating if the garden globals data is new.

    Methods:
        __init__(): Initialize a new instance of the DataHandler class.
        load_all(): Load all the data related to plant types, passives, and garden globals.
        load_plant_types(): Load the plant types data from a JSON file.
        load_passives(): Load the passives data from a JSON file.
        load_garden_globals(): Load the garden globals data from a JSON file.
        save_all(): Save all the data to external files.
        save_plant_types(): Save the plant types data to a JSON file.
        save_passives(): Save the passives data to a JSON file.
        save_garden_globals(): Save the garden globals data to a JSON file.
    """

    def __init__(self):
        """A class for handling data related to plant types, passives, and garden globals."""
        self.plant_types = dict()
        self.plant_types_new = True
        self.passives = dict()
        self.passives_new = True
        self.garden_globals = dict()
        self.garden_globals_new = True
        self.load_all()
        self.save_all()

    def load_all(self):
        """Initialize the DataHandler instance."""
        self.load_passives()
        self.load_plant_types()
        self.load_garden_globals()
        self.passives_new = False
        self.garden_globals_new = False
        self.plant_types_new = False

    def load_plant_types(self):
        """Load the plant types data from a JSON file."""
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
        """Load the passives data from a JSON file."""
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
        """Load the garden globals data from a JSON file."""
        with open("Data/gardenGlobals.json") as f:
            data = json.load(f)
        for item in data:
            self.garden_globals[item] = data[item]
        if self.garden_globals_new:
            for item in data:
                for value in data[item]:
                    self.garden_globals[item][value] = 1

    def save_all(self):
        """Save all the data to external files."""
        self.save_plant_types()
        self.save_passives()
        self.save_garden_globals()

    def save_plant_types(self):
        """Save the plant types data to a JSON file."""
        with open("Data/plantDataTest.json", "w") as w:
            w.write(json.dumps(self.plant_types, indent=2))

    def save_passives(self):
        """Save the passives data to a JSON file."""
        with open("Data/skillTreeDataTest.json", "w") as w:
            w.write(json.dumps(self.passives, indent=2))

    def save_garden_globals(self):
        """Save the garden globals data to a JSON file."""
        with open("Data/gardenGlobalTest.json", "w") as w:
            w.write(json.dumps(self.garden_globals, indent=2))

