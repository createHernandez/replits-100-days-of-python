import random #randint()
import os #system() 
import time #sleep()

bingoCard = [[None,  None,   None], 
             [None, "BINGO", None], 
             [None,  None,   None]]

def reset_bingoCard(): 
    for rowIndex in range(len(bingoCard)): 
        for colIndex in range(len(bingoCard[rowIndex])): 
            if bingoCard[rowIndex][colIndex] != "BINGO": 
                bingoCard[rowIndex][colIndex] = None

def generate_numbers(): 
    numbers = []

    while True: 
        random_number = random.randint(1, 90)

        if random_number not in numbers: 
            numbers.append(random_number)
        
        if len(numbers) == 8:
            break
        else: 
            continue
    
    numbers.sort() 

    return numbers

def generate_bingoCard(): 
    reset_bingoCard() 

    numbers = generate_numbers()
    numIndex = 0
    
    for rowIndex in range(len(bingoCard)): 
        for colIndex in range(len(bingoCard[rowIndex])): 
            if bingoCard[rowIndex][colIndex] == None: 
                bingoCard[rowIndex][colIndex] = numbers[numIndex]
                numIndex += 1 

def daub_number(number): 
    daub = 'X'

    for rowIndex in range(len(bingoCard)): 
        for colIndex in range(len(bingoCard[rowIndex])): 
            if bingoCard[rowIndex][colIndex] == number: 
                bingoCard[rowIndex][colIndex] = daub 

def check_bingo():
    count_x = 0 

    #traverse the 2d list looking for x's 
    for rowIndex in range(len(bingoCard)): 
        for colIndex in range(len(bingoCard[rowIndex])): 
            #if there is an x add to the counter 
            if bingoCard[rowIndex][colIndex] == 'X': 
                count_x += 1 

    #check how many x's and return the winner condition 
    if count_x == 8: 
        return True 
    else: 
        return False
    
def print_bingoCard(): 
    for rowIndex in range(len(bingoCard)): 
        for column_index in range(len(bingoCard[rowIndex])): 
            if column_index == (len(bingoCard[rowIndex]) - 1): 
                #print last row with no pipe 
                print(f"{bingoCard[rowIndex][column_index]:^4}")
            elif column_index == (len(bingoCard[rowIndex]) // 2): 
                #print the middle column with enough space for "BINGO" 
                print(f"{bingoCard[rowIndex][column_index]:^7}|", end="")
            else: 
                #print normal 
                print(f"{bingoCard[rowIndex][column_index]:^4}|", end="")
        #print the break line 
        if rowIndex != (len(bingoCard) - 1): 
            print("-" * 20)
    print()

def print_main_menu(): 
    os.system("cls")
    print("David's Nan's Bingo Card Generator\n")


# MAIN PROGRAM 
while True: 
    print_main_menu() 

    generate_bingoCard() 

    while True: 
        print_bingoCard()

        # ask player for what number was called 
        number = int(input("What number was called?: ").strip())
        print()

        daub_number(number)

        if check_bingo() == True: 
            #player has won 
            print("BINGO!\n")
            break
        else: 
            #player has not won yet 
            continue

    again = input("Would you like to play again?: ")
    print() 

    if again[0] == 'y': 
        continue
    else: 
        print("Thanks for playing!\n\nNow Exiting the Program...\n")
        exit()
