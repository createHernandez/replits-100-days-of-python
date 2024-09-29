import random #randint()
import os #system() 

# Create a 2D List for the bingo card 
# blank_bingoCard = []
blank_bingoCard = [[None,  None,   None], 
                   [None, "BINGO", None], 
                   [None,  None,   None]]

# test_blank_bingoCard = [[10,    22,   31], 
#                   [41, "BINGO", 73], 
#                   [84,    88,   89]]

# populate the card with random nums between 0 and 90 
def create_blank_bingoCard(): 
    ran_num_list = []
    ran_num_list_index = 0

    for index in range(8): 
        ran_num_list.append(random.randint(1, 90))

    ran_num_list.sort()

    for row_index in range(len(blank_bingoCard)): 
        for column_index in range(len(blank_bingoCard[row_index])): 
            if blank_bingoCard[row_index][column_index] == None: 
                blank_bingoCard[row_index][column_index] = ran_num_list[ran_num_list_index]
                ran_num_list_index += 1

def print_bingoCard(): 
    for row_index in range(len(blank_bingoCard)): 
        for column_index in range(len(blank_bingoCard[row_index])): 
            if column_index == (len(blank_bingoCard[row_index]) - 1): 
                print(f"{blank_bingoCard[row_index][column_index]:^4}")
            elif column_index == (len(blank_bingoCard[row_index]) // 2): 
                print(f"{blank_bingoCard[row_index][column_index]:^7}|", end="")
            else: 
                print(f"{blank_bingoCard[row_index][column_index]:^4}|", end="")
        if row_index != (len(blank_bingoCard) - 1): 
            print("-" * 20)
    print()

def print_main_menu(): 
    os.system("cls")

    print("David's Nan's Bingo Card Generator\n")

# MAIN PROGRAM 
print_main_menu()

play = input("Press Enter to Play >> ")
print()

if not play: 
    while True: 
        create_blank_bingoCard()

        print_bingoCard()

        choice = input("Would you like to generate another bingo card?: ").strip().lower()
        print()

        if choice[0] == "y": 
            blank_bingoCard = [[None,  None,   None], 
                               [None, "BINGO", None], 
                               [None,  None,   None]]
            print_main_menu()
            continue
        else: 
            print("Thanks for playing!\n\nExiting the program...\n")
            exit()
else: 
    print("Input Detected. Exiting the program...\n")
    exit()
