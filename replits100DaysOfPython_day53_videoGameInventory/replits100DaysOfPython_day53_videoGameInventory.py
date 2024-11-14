# https://docs.python.org/3/library/exceptions.html
import os # system() 
import time # sleep() 

inventory = []

try: 
    f = open("replits100DaysOfPython_day53_videoGameInventory/inventory.txt", "r")
    try: 
        inventory = eval(f.read())
    except Exception as err: 
        print("ERROR: Unable to load data.\n")
        time.sleep(1)
    else: 
        print("Data loaded successfully.")
        time.sleep(1)
    finally: 
        f.close() 
except: 
    print("ERROR: Unable to open the file.")
    time.sleep(1)

def print_main_menu(): 
    print("INVENTORY")
    print("=========\n")

    print("1: Add")
    print("2: View")
    print("3: Remove")
    print() 

def add_item(): 
    new_item = input("Item to add > ").strip().lower().capitalize()

    try: 
        inventory.append(new_item)
    except: 
        print("ERROR: Unable to add item.\n")
    else: 
        if new_item in inventory: 
            print("Added\n")

def remove_item(): 
    item = input("Item to remove > ").strip().lower().capitalize()

    try: 
        inventory.remove(item)
    except: 
        print("ERROR: Unable to add item.\n")
    else: 
        if item in inventory: 
            print("Removed\n")

def view_inventory():
    already_printed = []

    if inventory == []: 
        print("You have no items!\n")
    else: 
        for item in inventory: 
            if item not in already_printed: 
                already_printed.append(item)
                quantity = inventory.count(item)
                print(f"{item} {quantity}")
        
        print() 
        time.sleep(2)

while True: 
    os.system("cls")            

    print_main_menu() 

    choice = input("> ")
    print() 

    if choice == "1": 
        add_item()
        continue
    elif choice == "2": 
        view_inventory() 
        continue
    elif choice == "3": 
        remove_item()
        continue
    else: 
        print("Leaving inventory...\n")
        f = open("replits100DaysOfPython_day53_videoGameInventory/inventory.txt", "w")
        f.write(str(inventory))
        f.close() 
        exit() 
