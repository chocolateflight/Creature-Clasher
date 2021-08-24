
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
    
    def summary_player(self):
        return "You have " + str(self.armour) + " Armour points. Your Health is " + str(self.health) + " and you have " + str(self.stamina) + " Stamina."
    
    def summary_opponent(self):
        return "Your opponent has " + str(self.armour) + " Armour points, " + str(self.health) + " Health and " + str(self.stamina) + " Stamina."


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