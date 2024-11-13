import os #system()
import time #sleep()

todo_list = []

f = open("replits100DaysOfPython_day51_autoSaveAutoLoad/todo_list.txt", "r")
todo_list = eval(f.read())
f.close()

def view():
    if len(todo_list) == 0: 
        print("The list is empty!\n") 
        time.sleep(1)
    else: 
        print("Printing the current todo list...\n")
        time.sleep(1)

        for task in range(0, len(todo_list)): 
            print(f"{task + 1:>2}: {todo_list[task]}")
            time.sleep(.25)

        print("\nEnd of the list.\n")
        time.sleep(1)
        print("Returning to the main menu...\n")
        time.sleep(1)

def add(): 
    task = input("What task would you like to add?\n>> ").strip().lower().capitalize()
    print()

    if task not in todo_list: 
        todo_list.append(task)
        view()
    elif task in todo_list: 
        print("Duplicate task!\n")
        time.sleep(1)
        print("Returning to the main menu...\n")
        time.sleep(1)
    else: 
        print("ERROR! Unable to add task.")
        time.sleep(1)
        print("Returning to the main menu...\n")
        time.sleep(1)

def edit(): 
    view()
    original_task = input("Which task would you like to edit?\n>> ").strip().lower().capitalize()
    print()

    replacement_task = input("What task would you like instead?\n>> ").strip().lower().capitalize()
    print()

    if original_task in todo_list and replacement_task not in todo_list: 
        original_task_index = todo_list.index(original_task)
        todo_list[original_task_index] = replacement_task
        view()
    else: 
        print("ERROR! Unable to edit task.\n\nReturning to the main menu...\n")
        time.sleep(1)
        print("Returning to the main menu...\n")
        time.sleep(1)

def remove(): 
    view()
    task = input("What task would you like to remove?\n>> ").strip().lower().capitalize()
    print()

    if task in todo_list: 
        choice = input(f"Are you sure you want to remove '{task}'?\n>> ").strip().lower()
        print()
        if choice[0] == 'y': 
            todo_list.remove(task)
            view()
    elif task not in todo_list: 
        print("Missing task!\n")
        time.sleep(1)
        print("Returning to the main menu...\n")
        time.sleep(1)
    else: 
        print("ERROR! Unable to remove task.\n")
        time.sleep(1)
        print("Returning to the main menu...\n")
        time.sleep(1)

def remove_all(): 
    choice = input(f"Are you sure you want to clear the list?\n>> ").strip().lower()
    print()

    if choice[0] == 'y': 
        todo_list.clear()
        view()

def print_main_menu(): 
    print("ToDo List Manager\n")
    time.sleep(1)

    print("Do you want to view, add, remove, edit, or clear the todo list?")
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
    elif choice == "remove": 
        remove()
        continue
    elif choice == "clear": 
        remove_all()
        continue
    else: 
        print("Exiting the program...")
        f = open("replits100DaysOfPython_day51_autoSaveAutoLoad/todo_list.txt", "w")
        f.write(str(todo_list))
        f.close() 
        break

    
