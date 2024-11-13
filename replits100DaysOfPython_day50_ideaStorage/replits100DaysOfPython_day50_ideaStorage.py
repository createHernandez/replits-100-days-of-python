import os     # system()
import random # choice() 

def print_main_menu(): 
    os.system("cls")

    print("IDEAS\n")

    print("1: Add an idea")
    print("2: Load up a random idea")
    print() 

def add_idea(): 
    f = open("replits100DaysOfPython_day50_ideaStorage/my.ideas", "a+")

    idea = input("Idea > ")

    f.write(f"{idea}\n") 

    f.close() 

def random_idea(): 
    f = open("replits100DaysOfPython_day50_ideaStorage/my.ideas", "r")

    idea_list = f.read().split("\n")

    idea_list.remove(idea_list[(len(idea_list) - 1)])

    random_idea = random.choice(idea_list)

    print(f"Random idea: {random_idea}")

while True: 
    print_main_menu()

    user_choice = input("> ")
    print()

    if int(user_choice) == 1: 
        add_idea() 
        continue
    elif int(user_choice) == 2: 
        random_idea() 
        continue
    else: 
        print("Exiting the program...\n")
        exit() 
