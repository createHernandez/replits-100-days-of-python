import random #random.choice()

words_list = ["british", "suave", "bald", "integrity", "evil", "genius", "sixteen", "chapel", "sunrise", "buggy"]
guess_list = []

word = random.choice(words_list)

print(f"\n{word}\n")

lives = 6 

while True: 
    guess = input("Choose a letter: ").strip().lower()

    if guess in guess_list: 
        print("You've already tried that letter! Try again.\n")
        continue

    guess_list.append(guess) 

    if guess in word: 
        print("You found a letter!")
    else: 
        print("Nope, try again.")
        lives -= 1

    win_condition = True

    for letter in word: 
        if letter in guess_list: 
            print(letter, end="")
        else: 
            print("_", end="")
            win_condition = False
    print()

    if win_condition: 
        print(f"\nYou won! With {lives} lives left.\n")
        break

    if lives <= 0: 
        print("\nYou've run out of lives!\n")
        break
    else: 
        print(f"Only {lives} lives left.\n")
        continue