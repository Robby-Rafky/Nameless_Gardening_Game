from useful_functions import *

garden_global = {
    "stat_magnitude": 1,

    "flat_fertiliser": 0,
    "mult_fertiliser": 0,
    "total_fertiliser": 0,

    "total_adult": 1,
    "total_death": 1,
    "total_rate": 1,
    "total_mutation": 1,
    "total_yield": 1,
    "total_value": 1,
    "total_ability": 1,

    "skill_tree_adult": 1,
    "skill_tree_death": 1,
    "skill_tree_rate": 1,
    "skill_tree_mutation": 1,
    "skill_tree_yield": 1,
    "skill_tree_value": 1,
    "skill_tree_ability": 1,

    "garden_global_adult": 1,
    "garden_global_death": 1,
    "garden_global_rate": 1,
    "garden_global_mutation": 1,
    "garden_global_yield": 1,
    "garden_global_value": 1,
    "garden_global_ability": 1
}


def add_stat(stat, value):
    garden_global[stat] += value
    update_totals(stat.rsplit("_", 1)[1])


def subtract_stat(stat, value):
    garden_global[stat] -= value
    update_totals(stat.rsplit("_", 1)[1])


def multiply_stat(stat, value):
    garden_global[stat] = garden_global[stat] * value
    update_totals(stat.rsplit("_", 1)[1])


def divide_stat(stat, value):
    garden_global[stat] = garden_global[stat] / value
    update_totals(stat.rsplit("_", 1)[1])


def update_totals(stat):
    if stat != "fertiliser":
        garden_global["total_"+stat] = garden_global["skill_tree_"+stat] * garden_global["garden_global_"+stat]
    else:
        garden_global["total_" + stat] = garden_global["flat_" + stat] * garden_global["mult_" + stat]
