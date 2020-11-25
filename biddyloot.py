import config
import math
import random

# array name: inventory = {0}


def godFormula(config_item, ilvl):
    range_modifier = 3
    # return abs(int(random.uniform((math.log(ilvl)) - range_modifier, (math.log10(ilvl)*100) + range_modifier)))
    return int(random.uniform(ilvl + math.sqrt(config_item["stats"]["proficiency"]) - range_modifier, ilvl + math.sqrt(config_item["stats"]["proficiency"]) + range_modifier))
def loot_init(config_item):
    ilvl=config_item["item_level"]
    # range_modifier = 3
    # god_formula = abs(int(random.uniform((math.log(ilvl)) - range_modifier, (math.log10#(ilvl)*100) + range_modifier)))
    config_item["stats"]["strength"]=godFormula(config_item, ilvl)
    config_item["stats"]["intelligence"]=godFormula(config_item, ilvl)
    config_item["stats"]["dexterity"]=godFormula(config_item, ilvl)
    config_item["stats"]["vitality"]=godFormula(config_item, ilvl)

    return print(config_item)


# def get_item(looted_item):
  #
