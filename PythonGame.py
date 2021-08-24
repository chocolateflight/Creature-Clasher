# Hello World

from python_game_variables import creaturelist, potionslist
import python_game_functions

 
python_game_functions.print_logo()
print("Welcome to Creature Clash!")

while True:

    python_game_functions.print_pick_creature() # Prints List of creatures

    player = python_game_functions.creature_selection(creaturelist, python_game_functions.user_input) # Allows user to pick a creature for themselves

    python_game_functions.print_line()
    print("You choose " + str(player) + "! Now it's time to pick your opponent.")
    python_game_functions.print_pick_creature()

    opponent = python_game_functions.creature_selection(creaturelist, python_game_functions.user_input) # Allows user to pick an opponent creature
    print("\nYour opponent is " + str(opponent) + ". Good luck!")

    # python_game_functions.print_line
    # print("--- Ignore this part ---")
    # print(vars(player))
    # print(vars(opponent))
    # print("--- Ignore this part ---")
    # python_game_functions.print_line

    lostcode = 0
    wincode = 0
    while lostcode != 808 and wincode != 101: # While Loop for player's turn

        python_game_functions.print_line()
        print("It's your turn!\n")
        print(player.summary_player() + "\n")

        available_attacks = []

        while lostcode != 808 and wincode != 101: # While Loop for player's choices
            python_game_functions.print_round_choices()
            round_option = python_game_functions.user_input(python_game_functions.optionslist)
            python_game_functions.print_line()

            if round_option == 1:

                for attack in player.attacks:
                    if abs(attack.stamina_effect) <= player.stamina:
                        available_attacks.append(attack)
                
                if available_attacks != []:
                    print("Choose an option:\n\n")
                    i = 0
                    for attack in available_attacks:
                        print(str(i + 1) + " - " + str(attack))
                        i += 1
                    print("\n")
                
                    attack_number = python_game_functions.user_input(available_attacks)
                    python_game_functions.print_line()

                    if attack_number == 1:
                        output = python_game_functions.attack_move(player, opponent, available_attacks, attack_number)
                        player.stamina = output[0]
                        opponent.health = output[1]
                        opponent.armour = output[2]
                        break
                    elif attack_number == 2:
                        output = python_game_functions.attack_move(player, opponent, available_attacks, attack_number)
                        player.stamina = output[0]
                        opponent.health = output[1]
                        opponent.armour = output[2]
                        break
                    elif attack_number == 3:
                        output = python_game_functions.attack_move(player, opponent, available_attacks, attack_number)
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
                        print(str(i + 1) + " - " + str(potion))
                        i += 1
                    print("\n")

                    potion_number = python_game_functions.user_input(player.potions)
                    python_game_functions.print_line()

                    if potion_number == 1:
                        output = python_game_functions.potion_move(player, player.potions, potion_number)
                        player.health = output[0]
                        player.stamina = output[1]
                        break
                    if potion_number == 2:
                        output = python_game_functions.potion_move(player, player.potions, potion_number)
                        player.health = output[0]
                        player.stamina = output[1]
                        break
                    if potion_number == 3:
                        output = python_game_functions.potion_move(player, player.potions, potion_number)
                        player.health = output[0]
                        player.stamina = output[1]
                        break
            
            if round_option == 3:
                print("Are you sure that you want to skip your turn?\n\n1 - Yes\n2 - No\n")
                available_choices = ["Yes", "No"]
                choice = python_game_functions.user_input(available_choices)
                python_game_functions.print_line()

                if choice == 1:
                    break
                if choice == 2:
                    print("Pick again:")
                    continue
        break
    ## ADD CODE FOR OPPONENTS TURN ##
    break

print("####")
print(vars(player))
print(vars(opponent))
print("####")
