# Hello World

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

class Attacks:
    def __init__(self, name, health_effect, stamina_effect):
        self.name = name
        self.health_effect = health_effect
        self.stamina_effect = stamina_effect

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

frostboy = Creature("Frostboy", 80, 100, 43, [frostbite, winterstorm, snowball], [])
vampthing = Creature("Vampthing", 10, 150, 50, [vampire_bite, moonshock, invisible_attack], [])
cryptbeast = Creature("Cryptbeast", 50, 80, 80, [electric_shock, hashfryer, market_crash], [])
glowtree = Creature("Glowtree", 120, 10, 90, [firethrow, chainsaw, falling_apple], [])
slagtooth = Creature("Slagtooth", 90, 90, 40, [strongbite, monstercrush, fingerflip], [])