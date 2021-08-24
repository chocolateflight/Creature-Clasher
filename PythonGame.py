# Hello World

from python_game_variables import creaturelist
import python_game_functions

 
python_game_functions.print_logo()
print("Welcome to Creature Clash!")

while True:

    python_game_functions.print_pick_creature()

    player = python_game_functions.creature_selection(creaturelist)

    python_game_functions.print_line()
    print("\nYou choose " + str(player) + "! Now it's time to pick your opponent.\n")
    python_game_functions.print_pick_creature()

    opponent = python_game_functions.creature_selection(creaturelist)
    print("\nYour opponent is " + str(opponent) + ". Good luck!\n")

    while True:

        python_game_functions.print_line()
        print("\nLet's go! It's your turn!\n")
        print(player.summary_player() + "\n")
        python_game_functions.print_round_choices()
        round_selection = python_game_functions.round_selection(python_game_functions.optionslist, player)
        move_selection = python_game_functions.move_selection(round_selection, player)
        break
    break

python_game_functions.print_line()
print(player)
print(round_selection)