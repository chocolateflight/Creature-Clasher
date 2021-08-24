import random

###########################################################################

# Logo Design #

def decor(func):
    def wrap():
        print(67 * "=")
        func()
        print(67 * "=")
    return wrap

@decor
def print_logo():
    print("""
 _____                _                    _____ _           _     
/  __ \              | |                  /  __ \ |         | |    
| /  \/_ __ ___  __ _| |_ _   _ _ __ ___  | /  \/ | __ _ ___| |__  
| |   | '__/ _ \/ _` | __| | | | '__/ _ \ | |   | |/ _` / __| '_ \ 
| \__/\ | |  __/ (_| | |_| |_| | | |  __/ | \__/\ | (_| \__ \ | | |
 \____/_|  \___|\__,_|\__|\__,_|_|  \___|  \____/_|\__,_|___/_| |_|
                                                                   
""")

def print_line():
    print(67 * "=")

###########################################################################

# Game #

def print_pick_creature():
    print("""
Please pick a creature!

1 - Frostboy
2 - Vampthing
3 - Cryptbeast
4 - Glowtree
5 - Slagtooth
6 - Random

""")

def creature_selection(lst):
    while True:

        try:
            character = int(input("Enter number: "))
        except: 
            print("\nPlease enter a valid number\n")
            continue

        if (character < 1) or ((len(lst) + 1) < character):
            print("\nPlease enter a valid number\n")
            continue
        else:
            break

    if character == (len(lst) + 1):
        character = lst[random.randint(0, (len(lst) - 1))]
    else:
        character = lst[character - 1]
    
    return character

def print_round_choices():
    print("""
    Choose an option:

    1 - Attacks
    2 - Potions
    3 - Skip Round
    
    """)
optionslist = ["Attacks", "Potions", "Skip Round"]

def round_selection(lst, player):
    while True:

        try:
            round_option = int(input("Enter number: "))
        except:
            print("\nPlease enter a valid number\n")
            continue

        if (round_option < 1) or (round_option > (len(lst) + 1)):
            print("\nPlease enter a valid number\n")
            continue
        elif round_option == 2:
            if player.potions == []:
                print("\nNo more potions left. Pick another option.\n")
                continue
            else:
                break
        else:
            break

    return round_option

def move_selection(round_option, character):
    if round_option == 1:
        print("Choose an option:\n\n1 - " + str(character.attacks[0]) + "\n2 - " + str(character.attacks[1]) + "\n3 - " + str(character.attacks[2]))

    elif round_option == 2:
        print("Choose an option:\n\n")
        i = 0
        for potion in character.potions:
            print(str(i + 1) + " - " + str(potion))
            i += 1
    
    elif round_option == 3:
        return round_option