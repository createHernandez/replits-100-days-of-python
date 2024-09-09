import random #randint()

print("Example:\n")

print("Infinity Dice 🎲\n")

def sides(): 
  sides = int(input("How many sides?: "))
  return sides

def rollDice(sides):
  print(f"You rolled {random.randint(1, sides)} \n")

sides = sides()

while True: 
  rollDice(sides)

  again = input("Roll again? ")

  if again[0].strip().lower() == "y":
    continue
  else: 
    break