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

# Select an option from the round choices

def round_selection(options_lst, player, user_input, potionslist):
    available_attacks = []

    while True:
        round_option = user_input(options_lst)

        if round_option == 1:

            for attack in player.attacks:
                if abs(attack.stamina_effect) <= player.stamina:
                    available_attacks.append(attack)

            if available_attacks != []:
                return available_attacks
            elif (available_attacks == []) and (potionslist[0] in player.potions):
                print("You need to drink a stamina potion if you want to attack your opponent.")
                continue

            elif (available_attacks == []) and not (potionslist[0] in player.potions):
                return 12 # No attack can be used, no potion is available. Player looses. 

        if round_option == 2:
            if player.potions == []:
                print("\nNo more potions left. Pick another option.\n")
                continue
            else:
                return player.potions
        
        if round_option == 3:
            return 11 # Skip Round

###########################################################################

# Select a move after the round choice

def attack_move(player, opponent, attack):
    print(str(player) + " uses " + str(player.attacks[attack]) + " against " + str(opponent) + "!" )
    chosen_attack = player.attacks[attack - 1]
    attack_health_effect = chosen_attack.health_effect
    attack_stamina_effect = chosen_attack.stamina_effect
    opponent.health -= attack_health_effect
    player.stamina -= attack_stamina_effect
    

def move_selection(round_option, player, opponent, user_input, attack_move):

    if type(round_option) is list:

        if isinstance(round_option[0], Attacks):

            print("Choose an option:\n\n")
            i = 0
            for attack in round_option:
                print(str(i + 1) + " - " + str(attack))
                i += 1
            print("\n")

            attack = user_input(round_option)

            if attack == 1:
                pass # Add code for attack 1
            elif attack == 2:
                pass # Add Code for attack 2
            elif attack == 3:
                pass # Add Code for attack 3
            
            return "Move Selection function, if round option == 1" # Change output

        elif isinstance(round_option[0, Potions]):
            print("Choose an option:\n\n")

            i = 0
            for potion in player.potions:
                print(str(i + 1) + " - " + str(potion))
                i += 1
            
            potion = user_input(player.potions)

            if potion == 1:
                pass # Add code for potion 1
            elif potion == 2:
                pass # Add code for potion 2
            elif potion == 3:
                pass # Add code for potion 3

            return "Move Selection function, if round option == 2" # Change output
        
    elif round_option == 11:
        return "Move Selection function, if round option == 3" # Change Output
