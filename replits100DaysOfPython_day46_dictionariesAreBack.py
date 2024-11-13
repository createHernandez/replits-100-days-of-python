import os    # system()
import time  # sleep()

# mokeBeast = { }

mokeBeast = {"Pain Toad": {"Type": "Water", "HP": 9999, "MP": -3},
             "Jigglyzard": {"Type": "Fire", "HP": 43, "MP": 4322}}

def display_main_menu(): 
    os.system("cls")

    print("Welcome to Your MokéBeasts Full-on MokéDex!\n")

    print("What would you like to do?\n")

    print("Enter 1 - to view your MokéDex.")
    print("Enter 2 - to add a MokéBeast.")
    print("Enter nothing to exit.")

def print_type_color(type):
    if type == "Earth":
        return "\033[32m"
    elif type == "Fire":
        return "\033[31m"
    elif type == "Wind":
        return "\033[0m"
    elif type == "Water":
        return "\033[34m"
    elif type == "Lightning":
        return "\033[33m"
    elif type == "Ghost":
        return "\033[35m"
    else:
        return "\033[0m"
    
def print_mokedex():
    beast_name = "Beast Name"
    type = "Type" 
    hp = "HP"
    mp = "MP"
    break_line_char = '-'
    break_line_len = 80

    print("Here's your MokéBeast's info!\n")

    print(break_line_char * break_line_len)
    print(f"{beast_name:^30} | {type:^20} | {hp:^10} | {mp:^10} ")
    print(break_line_char * break_line_len)
    for key, value in mokeBeast.items(): 
        print(f"{key:^30} |", end=" ")

        for subkey, subvalue in value.items(): 
            if subkey == "Type": 
                print(f"{print_type_color(subvalue)}{subvalue:^20}{print_type_color("Default")} |", end=" ")
            elif subkey == "HP": 
                print(f"{subvalue:>10} |", end=" ")
            else: 
                print(f"{subvalue:>10} ")
    time.sleep(2)
    print()

def get_mokebeast():
    print("Add Your Beast!\n")

    while True:
        beast_name = input("What is the beast's name?: ").strip().lower().capitalize()
        type = input("What type is it?: ").strip().lower().capitalize()
        hp = int(input("How much HP does it have?: ").strip())
        mp = int(input("How much MP does it have?: ").strip())
        print()

        mokeBeast[beast_name] = {"Type": type, "HP": hp, "MP": mp}

        choice = input("Would you like to add another beast?: ").strip().lower() 

        if choice[0] == 'y': 
            continue
        else: 
            break

    print()

def print_exit_message(): 
    print("Thanks for using Your MokéBeasts Full-on MokéDex!")
    print("Exiting...\n")

# MAIN PROGRAM 
while True: 
    display_main_menu() 

    choice = input(">> ").strip()
    print()

    if not choice: 
        print_exit_message()
        exit()
    elif int(choice) == 1: 
        print_mokedex()
    elif int(choice) == 2: 
        get_mokebeast() 
    else: 
        print_exit_message()
        exit()