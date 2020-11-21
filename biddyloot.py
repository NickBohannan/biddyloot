import config

def loot_init(level, char_class, item_class):
    # this is where we will handle the level scaling and character/item conditionals
    print("you have chosen a level " + level + " " + char_class)
    print("you have chosen to generate a " + item_class)