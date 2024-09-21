import os, time 

names_list = []

def print_names_list():
    if len(names_list) == 0: 
        print("The list is empty!\n") 
        time.sleep(1)
    else: 
        print("Printing the current names list...\n")
        time.sleep(1)

        for name in range(0, len(names_list)): 
            print(f"{name + 1:>2}: {names_list[name]}")
            time.sleep(.25)

        print("\nEnd of the list.\n")
        time.sleep(1)

def get_full_name(): 
    first_name = input("What is your first name?: ").strip().lower().capitalize()

    surname = input("What is your surname?: ").strip().lower().capitalize()
    print()

    full_name = f"{first_name} {surname}"

    if full_name not in names_list: 
        names_list.append(full_name)
        print_names_list()
    else: 
        print("ERROR! Unable to add name.\n")

os.system("cls")

while True: 
    get_full_name()

    choice = input("Add another name?: ").strip().lower()
    print()

    if choice[0] == "y": 
        continue
    else: 
        print("Exiting the program...")
        exit()