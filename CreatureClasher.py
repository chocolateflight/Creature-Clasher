# Hello World

from creatureclasher_variables import creaturelist, potionslist
import creatureclasher_functions
import random

 
creatureclasher_functions.print_logo()
print("Welcome to Creature Clasher!")

while True:

    creatureclasher_functions.print_pick_creature() # Prints List of creatures

    player = creatureclasher_functions.creature_selection(creaturelist, creatureclasher_functions.user_input) # Allows user to pick a creature for themselves

    creatureclasher_functions.print_line()
    print("You choose " + str(player) + "! Now it's time to pick your opponent.")
    creatureclasher_functions.print_pick_creature()

    opponent = creatureclasher_functions.creature_selection(creaturelist, creatureclasher_functions.user_input) # Allows user to pick an opponent creature
    print("\nYour opponent is " + str(opponent) + ". Good luck!")

    lostcode = 0
    wincode = 0
    while lostcode != 808 and wincode != 101: # While Loop for game round
        
        if player.health <= 0:
            lostcode = 808
            break

        creatureclasher_functions.print_line()
        print("It's your turn!\n")
        print(player.summary_player())
        print(opponent.summary_opponent() + "\n")

        available_attacks = []

        while lostcode != 808 and wincode != 101: # While Loop for player's choices
            creatureclasher_functions.print_round_choices()
            round_option = creatureclasher_functions.user_input(creatureclasher_functions.optionslist)
            creatureclasher_functions.print_line()

            if round_option == 1:

                for attack in player.attacks:
                    if abs(attack.stamina_effect) <= player.stamina:
                        available_attacks.append(attack)
                
                if available_attacks != []:
                    print("Choose an option:\n\n")
                    i = 0
                    for attack in available_attacks:
                        print(str(i + 1) + " - " + str(attack) + " (Effect on opponent: " + str(attack.health_effect) + " health, Effect on you: " + str(attack.stamina_effect) + " stamina.)")
                        i += 1
                    print("\n")
                
                    attack_number = creatureclasher_functions.user_input(available_attacks)
                    creatureclasher_functions.print_line()

                    output = creatureclasher_functions.attack_move(player, opponent, available_attacks, attack_number)
                    player.stamina = output[0]
                    opponent.health = output[1]
                    opponent.armour = output[2]
                    break

                elif (available_attacks == []) and (potionslist[0] in player.potions):
                    print("You need to drink a stamina potion if you want to attack your opponent.")
                    continue

                elif (available_attacks == []) and not (potionslist[0] in player.potions):
                    lostcode = 808
                    break
            
            if round_option == 2:
                if player.potions == []:
                    print("\nNo more potions left. Pick another option.\n")
                    continue
                else:
                    print("Choose an option:\n\n")

                    i = 0
                    for potion in player.potions:
                        print(str(i + 1) + " - " + str(potion) + " (Effect: + " + str(abs(potion.health_effect)) + " health, +" + str(abs(potion.stamina_effect)) + " stamina.)")
                        i += 1
                    print("\n")

                    potion_number = creatureclasher_functions.user_input(player.potions)
                    creatureclasher_functions.print_line()

                    output = creatureclasher_functions.potion_move(player, player.potions, potion_number)
                    player.health = output[0]
                    player.stamina = output[1]
                    player.potions.remove(output[2])
                    break
            
            if round_option == 3:
                print("Are you sure that you want to skip your turn?\n\n1 - Yes\n2 - No\n")
                available_choices = ["Yes", "No"]
                choice = creatureclasher_functions.user_input(available_choices)
                creatureclasher_functions.print_line()

                if choice == 1:
                    break
                if choice == 2:
                    print("Pick again:")
                    continue
        
        if lostcode == 808:
            break

        if opponent.health <= 0:
            wincode = 101
            break

        print("\n")
        print(opponent.summary_opponent())
        creatureclasher_functions.print_line()    

        # Opponent Turn
        print("It is now your opponents turn!\n")
        if opponent.health <= 40: # Opponent drinks health potion if health is low
            if potionslist[1] in opponent.potions:
                opponent.health += potionslist[1].health_effect
                opponent.potions.remove(potionslist[1])
                print("Your opponent drank a healthpotion.")
                continue
            else:
                pass

        available_attacks_opo = []
        for attack in opponent.attacks:
            if abs(attack.stamina_effect) <= opponent.stamina:
                available_attacks_opo.append(attack)

        if available_attacks_opo != []:

            opponent_attack_number = int(random.randint(0, (len(available_attacks_opo) - 1)))

            output = creatureclasher_functions.attack_move(opponent, player, available_attacks_opo, opponent_attack_number)
            opponent.stamina = output[0]
            player.health = output[1]
            player.armour = output[2]
            continue
                
        elif (available_attacks_opo == []) and potionslist[0] in opponent.potions:
            opponent.stamina += potionslist[0].stamina_effect
            opponent.potions.remove(potionslist[0])
            print("Your opponent drank a stamina potion.")
            continue # Opponent drinks Stamina potion when necessary

        elif (available_attacks_opo == []) and not (potionslist[0] in opponent.potions):
            wincode = 101
            break # Opponent looses
    
    if lostcode == 808:
        creatureclasher_functions.print_line()
        print("You lost! Your opponent " + str(opponent) + " won this battle. Would you like to play another round?")
        print("\n1 - Yes\n2 - No\n")
        available_choices = ["Yes", "No"]
        choice = creatureclasher_functions.user_input(available_choices)
        creatureclasher_functions.print_line

        if choice == 1:
            continue

        if choice == 2:
            break
    
    elif wincode == 101:
        creatureclasher_functions.print_line()
        print("Congratulations! You won. Your opponent was destroyed. Would you like to play another round?")
        print("\n1 - Yes\n2 - No\n")
        available_choices = ["Yes", "No"]
        choice = creatureclasher_functions.user_input(available_choices)
        creatureclasher_functions.print_line

        if choice == 1:
            continue

        if choice == 2:
            break       
    break

while True:
    creatureclasher_functions.print_line()
    print("Thank you for playing Creature Clasher!\n")
    creatureclasher_functions.print_logo()
    print("\nA training project by Marc Hostettler")
    creatureclasher_functions.print_line()
    print("Enter \"1\" to end programm")
    available_choices = []
    choice = creatureclasher_functions.user_input(available_choices)
    break