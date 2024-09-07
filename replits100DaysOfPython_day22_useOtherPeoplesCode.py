import random 

print("One-Million-To-One\n")

print("Choose a number between 1 and 1,000,000.\n")

answer = random.randint(1, 1000000)
attempts = 1

while True: 
  guess = int(input("What is your guess?: "))

  if guess == answer:
    print("Correct!\n")
    break
  elif guess < answer:
    print("Too low\n")
    attempts += 1
    continue
  elif guess > answer: 
    print("Too high\n")
    attempts += 1
    continue
  else: 
    print(f"You guessed {guess}\n")

if attempts == 1: 
  print(f"It took you {attempts} guess to get it right!")
else: 
  print(f"It took you {attempts} guesses to get it right!")