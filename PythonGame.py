# Hello World

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

###########################################################################

# Classes #

class Creature:
    def __init__(self, name, armour, health, stamina, attacks, potions):
        self.name = name
        self.armour = armour
        self.health = health
        self.stamina = stamina
        self.attacks = attacks
        self.potions = potions
    
    def __repr__(self):
        return self.name

class Attacks:
    def __init__(self, name, health_effect, stamina_effect):
        self.name = name
        self.health_effect = health_effect
        self.stamina_effect = stamina_effect
    
    def __repr__(self):
        return self.name

class Potions(Attacks):
    pass


###########################################################################

# Attacks #

frostbite = Attacks("Frostbyte", -30, -10)
winterstorm = Attacks("Winterstorm", -50, -30)
snowball = Attacks("Snowball", -10, -10)

vampire_bite = Attacks("Vampire Bite", -40, -20)
moonshock = Attacks("Moonshock", -30, -10)
invisible_attack = Attacks("Invisible Attack", -10, -10)

electric_shock = Attacks("Electric Shock", -30, -20)
hashfryer = Attacks("Hash Fryer", -35, -15)
market_crash = Attacks("Market Crash", -10, -10)

firethrow = Attacks("Fire Throw", -55, -35)
chainsaw = Attacks("Chainsaw", -20, -30)
falling_apple = Attacks("Falling Apple", -10, -10)

strongbite = Attacks("Strongbite", -40, -30)
monstercrush = Attacks("Monstercrush", -30, -20)
fingerflip = Attacks("Fingerflip", -15, -15)

# Potions #

staminapotion = Potions("Stamina Potion", 0, +30)
healthpotion = Potions("Health Potion", +20, 0)

# Creatures #

frostboy = Creature("Frostboy", 80, 100, 45, [frostbite, winterstorm, snowball], [staminapotion, staminapotion])
vampthing = Creature("Vampthing", 10, 150, 50, [vampire_bite, moonshock, invisible_attack], [healthpotion, staminapotion, staminapotion])
cryptbeast = Creature("Cryptbeast", 50, 80, 80, [electric_shock, hashfryer, market_crash], [healthpotion, healthpotion, staminapotion])
glowtree = Creature("Glowtree", 120, 10, 90, [firethrow, chainsaw, falling_apple], [healthpotion, healthpotion, staminapotion])
slagtooth = Creature("Slagtooth", 90, 90, 40, [strongbite, monstercrush, fingerflip], [staminapotion, staminapotion])

creaturelist = [frostboy, vampthing, cryptbeast, glowtree, slagtooth]

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

print_logo()
print("Welcome to Creature Clash!")

while True:

    print_pick_creature()

    player = creature_selection(creaturelist)

    print("\nYou choose " + str(player) + " ! Now it's time to pick your opponent.\n")
    print_pick_creature()

    opponent = creature_selection(creaturelist)
    print("\nYour opponent is " + str(opponent) + ". Good luck!")

