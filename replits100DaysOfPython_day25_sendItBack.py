import random #randint()

def roll_dice(sides): 
  return random.randint(1, sides)

def get_health(): 
  return roll_dice(6) * roll_dice(8)

print("⚔️ Character Stats Generator ⚔️\n")

while True: 
  name = input("Name your warrior: ")
  print(f"Their health is: {get_health()}hp\n")
  
  again = input("Roll for another character? ")
  print()

  if again[0].strip().lower() == "y":
    continue
  else: 
    break