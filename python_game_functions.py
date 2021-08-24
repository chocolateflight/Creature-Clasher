import random
from python_game_variables import Attacks, Potions

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

# Pick Creature Selection

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

###########################################################################

# Choices for each round

def print_round_choices():
    print("""
    Choose an option:

    1 - Attacks
    2 - Potions
    3 - Skip Round
    
    """)
optionslist = ["Attacks", "Potions", "Skip Round"]

###########################################################################

# Checks if user input is valid

def user_input(lst):
    while True:

        try:
            user_input = int(input("Enter number: "))
        except:
            print("\nPlease enter a valid number.\n")
            continue

        if (user_input < 1) or (user_input > (len(lst) + 1)):
            print("\nPlease enter a valid number.\n")
            continue
        else:
            break

    return user_input

###########################################################################

# Creature Selection

def creature_selection(lst, user_input):
    character = user_input(lst)

    if character == (len(lst) + 1):
        character = lst[random.randint(0, (len(lst) - 1))]
    else:
        character = lst[character - 1]
    
    return character

###########################################################################

# Select a move after the round choice

def attack_move(player, opponent, round_option, attack_number):

    attack = round_option[attack_number - 1]
    print(str(player) + " (player) uses " + str(attack) + " against " + str(opponent) + ".")
    health_effect_attack = abs(attack.health_effect)
    stamina_effect_attack = abs(attack.stamina_effect)
    
    if opponent.armour > 0:
        if opponent.armour - health_effect_attack < 0:
            opponent.health -= abs(opponent.armour - health_effect_attack)
            opponent.armour = 0
        elif opponent.armour - health_effect_attack >= 0:
            opponent.armour -= health_effect_attack
    elif opponent.armour <= 0:
        opponent.health -= health_effect_attack
    
    player.stamina -= stamina_effect_attack

    return player.stamina, opponent.health, opponent.armour