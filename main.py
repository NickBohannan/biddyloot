import builtins
import biddyloot
import config

def main():
    class_exists = False
    item_exists = False
    
    # display all character classes
    print("")
    print("options\n------")
    for x in config.class_tuple:
        print(x) 
    print("")

    # enter the character class
    char_class = input("please enter your character class: ")

    for x in config.class_tuple:
        if x == char_class:
            class_exists = True
    
    if class_exists == False:
        print("GET A BRAIN MORAN")
        return 0

    # enter the desired level
    level = input("please enter your character level: ")

    # display all item classes
    print("")
    print("options\n------")
    for x in config.item_tuple:
        print(x)
    print("")

    # enter the item class
    item_class = input("what type of item do you want generated?: ")

    for x in config.item_tuple:
        if x == item_class:
            item_exists = True
    
    if item_exists == False:
        print("GET A BRAIN MORAN")
        return 0
    
    # Initialize loot logic
    biddyloot.loot_init(level, char_class, item_class)

if __name__ == "__main__":
    main()
    