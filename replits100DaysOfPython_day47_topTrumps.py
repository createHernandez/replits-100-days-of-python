import os     # system()
import random # choice()

trump_list = {"Mr Spock": {"Intelligence": 46, "Speed": 81, "Guile": 48, "Baldness Level": 0}, 
             "David": {"Intelligence": 45, "Speed": 64, "Guile": 64, "Baldness Level": 99}, 
             "Monica from Friends": {"Intelligence": 54, "Speed": 78, "Guile": 98, "Baldness Level": 87}, 
             "Professor X": {"Intelligence": 76, "Speed": 26, "Guile": 78, "Baldness Level": 105}}

def print_characters(): 
    for key in trump_list: 
        print(f"{key}")

def pick_random_character(): 
    random_character = random.choice(list(trump_list))

    return random_character

# MAIN PROGRAM 
while True: 
    os.system("cls")

    print("TOP TRUMPS")
    print("----------\n")

    print("Characters\n")

    print_characters()
    print() 

    character_choice = input("Pick your character\n> ").strip().lower().title()
    print()

    computer_choice = pick_random_character()

    print(f"Computer has picked {computer_choice}\n")

    stat_choice = input("Choose your stat: Intelligence, Speed, Guile & Baldness Level\n\n> ").strip().lower().title()
    print()

    print(f"{character_choice}: {trump_list[character_choice][stat_choice]}")
    print(f"{computer_choice}: {trump_list[computer_choice][stat_choice]}")
    print()

    if trump_list[character_choice][stat_choice] > trump_list[computer_choice][stat_choice]: 
        print(f"{character_choice} wins!")
    elif trump_list[computer_choice][stat_choice] > trump_list[character_choice][stat_choice]: 
        print(f"{computer_choice} wins!")
    elif trump_list[character_choice][stat_choice] == trump_list[computer_choice][stat_choice]: 
        print("It's a draw.")
    else: 
        print("Unable to determine a winner.")
    print()

    choice = input("Again?: ").strip().lower()
    print()

    if choice[0] == 'y': 
        continue
    else: 
        print("Exiting...\n")
        exit()