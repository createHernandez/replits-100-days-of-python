# | Name | Date | Priority 

import os, time, random

todo_list = [] 

todo_list = [["Read book.", "01/15/2025", "High"], 
             ["Sleep", "10/04/2024", "High"], 
             ["Something", "12/15/2024", "Low"], 
             ["Build a building", "05/45/2024", "High"]]

def display_main_menu(): 
    os.system("cls")

    print("Welcome to Your ToDo List Management System!\n")

    print("What would you like to do?\n")

    print("Enter 1 - to view the current to do list.")
    print("Enter 2 - to add a task.")
    print("Enter 3 - to remove a task.") 
    print("Enter 4 - to edit a task.") 
    print("Enter 5 - to get a random task to accomplish.") 
    print("Enter nothing to exit.")

def view_all(): 
    task_name = "Task Name"
    due_date = "Due Date"
    priority = "Priority"
    break_line_character = f'-'
    break_line_length = 90

    print(break_line_character * break_line_length)
    print(f"{task_name:^30} | {due_date:^30} | {priority:^10}")
    print(break_line_character * break_line_length)
    for rowIndex in range(len(todo_list)): 
        for colIndex in range(len(todo_list[rowIndex])): 
            if colIndex == (len(todo_list[rowIndex]) - 1): 
                print(f"{todo_list[rowIndex][colIndex]:^10}")
            else: 
                print(f"{todo_list[rowIndex][colIndex]:^30} |", end=" ")
        time.sleep(.5)
        print(break_line_character * break_line_length)
    time.sleep(2)
    print()

def view_priority(priority_level): 
    task_name = "Task Name"
    due_date = "Due Date"
    priority = "Priority"
    break_line_character = f'-'
    break_line_length = 90

    print(break_line_character * break_line_length)
    print(f"{task_name:^30} | {due_date:^30} | {priority:^10}")
    print(break_line_character * break_line_length)
    for rowIndex in range(len(todo_list)): 
        if todo_list[rowIndex][2] == priority_level:
            for colIndex in range(len(todo_list[rowIndex])):     
                if colIndex == (len(todo_list[rowIndex]) - 1): 
                    print(f"{todo_list[rowIndex][colIndex]:^10}")
                else: 
                    print(f"{todo_list[rowIndex][colIndex]:^30} |", end=" ")
            time.sleep(.5)
            print(break_line_character * break_line_length)
    time.sleep(1)
    print()

def view(): 
    os.system("cls")

    print("View\n")
    
    print("1: View All")
    print("2: View Priority")

    choice = int(input(">> ").strip())
    print()

    if choice == 1: 
        view_all() 
    elif choice == 2: 
        priority_level = input("What priority tasks would you like to see?: ").strip().lower().capitalize()
        view_priority(priority_level)
    else: 
        print("ERROR! Invalid Input.\n\nReturing to the main menu...\n")
        time.sleep(1)   

def add_new_task(): 
    task = input("What task would you like to add?\n>> ").strip().lower().capitalize()
    print()
    due_date = input("When is it due?: ").strip().lower().capitalize()
    print()
    priority = input("How important is it?: ").strip().lower().capitalize()
    print()

    for row in todo_list: 
        if task in row: 
            print("That task is already in your todo list.")
            print("Returning to the main menu...\n")
            time.sleep(1)

    todo_list.append([task, due_date, priority])

    for row in todo_list: 
        if task in row: 
            view_all() 

def remove_task(): 
    view_all() 

    task = input("Which task would you like to remove?: ").strip().lower().capitalize()

    for row in todo_list: 
        if task in row: 
            todo_list.remove(row)
            was_removed = True

    if was_removed == True: 
        print("Task was successfully removed.\n")
        view_all() 
    else: 
        print("Unable to remove task. Not on the list.")
        print("Returning to the main menu...\n")
        time.sleep(1)

def edit_task(): 
    view_all() 

    task = input("Which task would you like to edit?: ").strip().lower().capitalize()

    column = input("What part would you like to change? (Task, Due Date, or Priority): ").strip().lower()

    if column == "task": 
        new_task = input("What is the new task name?: ").strip().lower().capitalize()

        for row in todo_list: 
            if task in row: 
                row_index = todo_list.index(row)
                todo_list[row_index][0] = new_task
                was_edited = True

    elif column == "due date": 
        new_due_date = input("What is the new due date?: ").strip().lower() 

        for row in todo_list: 
            if task in row: 
                row_index = todo_list.index(row)
                todo_list[row_index][1] = new_due_date
                was_edited = True

    elif column == "priority": 
        new_priority = input("What is the new priority?: ").strip().lower().capitalize()

        for row in todo_list: 
            if task in row: 
                row_index = todo_list.index(row)
                todo_list[row_index][2] = new_priority
                was_edited = True

    if was_edited == True: 
        print("Successfully edited.\n")
        view_all() 
    else: 
        print("Unable to edit.")
        print("Returning to the main menu...\n")
        time.sleep(1)

# MAIN PROGRAM 
while True: 
    display_main_menu() 

    choice = input(">> ").strip()
    print()

    if not choice: 
        print("Thanks for using the ToDo List Management System!")
        print("Exiting...\n")
        exit()
    elif int(choice) == 1: 
        view()
    elif int(choice) == 2: 
        add_new_task() 
    elif int(choice) == 3: 
        remove_task() 
    elif int(choice) == 4: 
        edit_task() 
    else: 
        print("Thanks for using the ToDo List Management System!")
        print("Exiting...\n")
        exit()