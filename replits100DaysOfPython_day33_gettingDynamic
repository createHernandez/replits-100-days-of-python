import os #system()
import time #sleep()

todo_list = []

def view(): 
    print()
    for item in range(0, len(todo_list)): 
        print(f"{todo_list[item]}")
        time.sleep(1)
    print()

def add(): 
    print("What do you want to add?")
    item = input(">> ")
    todo_list.append(item)
    view()

def edit(): 
    view()
    print("What do you want to remove?")
    item = input(">> ")
    todo_list.remove(item)

def print_main_menu(): 
    print("ToDo List Manager\n")
    time.sleep(1)

    print("Do you want to view, add or edit the todo list?")
    time.sleep(1)

while True: 
    os.system("cls")

    print_main_menu()

    choice = input(">> ").strip().lower()
    print()

    if choice == "view": 
        view()
        continue
    elif choice == "add": 
        add()
        continue
    elif choice == "edit": 
        edit()
        continue
    else: 
        print("Exiting the program...")
        exit()