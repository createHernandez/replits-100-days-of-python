# https://docs.python.org/3/library/exceptions.html
import os # system() 
import time # sleep() 

pizza_orders = []

try: 
    f = open("replits100DaysOfPython_day52_braceForImpact/pizza.txt", "r")
    try: 
        pizza_orders = eval(f.read())
    except Exception as err: 
        print("ERROR: Unable to load data.\n")
        time.sleep(1)
    else: 
        print("Data loaded successfully.")
        time.sleep(1)
    finally: 
        f.close() 
except: 
    print("ERROR: Unable to open the 'pizza.txt' file.")
    time.sleep(1)

def print_main_menu(): 
    print("Rominos Pizza\n")

    print("1: Add Pizza")
    print("2: View Pizzas")
    print() 

def get_name(): 
    name = input("What is the name for the order?: ").strip().lower().title()
    return name 

def get_toppings(): 
    toppings = input("What toppings would you like?: ").strip().lower().title() 
    return toppings

def get_size(): 
    size = input("What size?: ").strip().lower()
    size = size[0]
    return size

def get_quantity(): 
    while True: 
        try: 
            quantity = int(input("How many pizzas?: ").strip())
        except ValueError: 
            print("ERROR: Not a valid quantity. Please try again...\n")
            time.sleep(1)
        else: 
            print("quantity variable initialized successfully.")
            time.sleep(1)
        break

    return quantity

def calculate_cost(size, quantity): 
    small_pizza_price = 5.99 
    medium_pizza_price = 9.99 
    large_pizza_price = 14.99 

    if size == 's': 
        cost = small_pizza_price * quantity 
    elif size == 'm': 
        cost = medium_pizza_price * quantity 
    elif size == 'l': 
        cost = large_pizza_price * quantity 

    return cost 

def new_order(): 
    name = get_name() 
    toppings = get_toppings() 
    size = get_size() 
    quantity = get_quantity() 
    cost = calculate_cost(size, quantity) 

    pizza_orders.append([name, toppings, size, quantity, cost])

def print_orders():
    name = "Name"
    topping = "Topping(s)"
    s_title = "Size"
    q_title = "Quantity"
    total = "Total"
    br_char = '-'
    br_len = 90

    if pizza_orders == []: 
        print("There are currently no orders.\n")
    else: 
        print(f"{name:^20} | {topping:^15} | {s_title:^15} | {q_title:^15} | {total:^15} ")
        print(br_char * br_len)

        for row in range(len(pizza_orders)): 
            for col in range(len(pizza_orders[row])): 
                if col == (len(pizza_orders[row]) - 1): 
                    print(f"{pizza_orders[row][col]:^15} ")
                elif col == 0: 
                    print(f"{pizza_orders[row][col]:^20} |", end=" ")
                else: 
                    print(f"{pizza_orders[row][col]:^15} |", end=" ")
        print() 
        time.sleep(2)

while True: 
    os.system("cls")            

    print_main_menu() 

    choice = input("> ")
    print() 

    if choice == "1": 
        new_order()
        continue
    elif choice == "2": 
        print_orders() 
        continue
    else: 
        print("Thank you for ordering with Romino's Pizza.")
        print("Goodbye...\n")
        f = open("replits100DaysOfPython_day52_braceForImpact/pizza.txt", "w")
        f.write(str(pizza_orders))
        f.close() 
        exit() 
