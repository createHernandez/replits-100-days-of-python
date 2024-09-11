import os       # system()
import time     # sleep()
import random   # randint()

def roll_dice(sides): 
  return random.randint(1, sides)

def get_name(): 
  name = input("Name your Legend: ")
  return name 

def get_type(): 
  type = input("Character Type (Human, Elf, Wizard, Orc): ")
  return type

def get_health(): 
  return (roll_dice(6) * roll_dice(12)) / 2 + 10

def get_strength():
  return (roll_dice(6) * roll_dice(12)) / 2 + 12

def generate_character(): 
  name = get_name()
  type = get_type()
  health = get_health()
  strength = get_strength()
  print()
  return name, type, health, strength

def print_character(name, type, health, strength):
  print(f"Name: {name}")
  time.sleep(.5)
  print(f"Type: {type}")
  time.sleep(.5)
  print(f"Health: {health}")
  time.sleep(.5)
  print(f"Strength: {strength}")
  time.sleep(.5)
  print()
  # print("May your name go down in Legend...\n")
  # time.sleep(.5)

def print_main_menu(): 
  os.system("clear")
  print("⚔️ CHARACTER BUILDER ⚔️\n")
  time.sleep(.5)

def print_battle_menu(): 
  os.system("clear")
  print("⚔️ CHARACTER BUILDER ⚔️\n")
  time.sleep(.5)

while True: 
  print_main_menu()

  char1_name, char1_type, char1_health, char1_strength = generate_character()
  print_character(char1_name, char1_type, char1_health, char1_strength)

  print("Who are they battling?\n")
  char2_name, char2_type, char2_health, char2_strength = generate_character()
  print_character(char2_name, char2_type, char2_health, char2_strength)

  # start = input("Press Enter to start the battle: ")

  round = 1
  winner = ""
  loser = ""

  while True: 
    print_battle_menu()

    if round == 1: 
      print("The battle begins!\n")
    else: 
      print("The battle continues!\n")
    time.sleep(1)

    char1_roll = roll_dice(6) 
    char2_roll = roll_dice(6) 

    damage = abs(char1_strength - char2_strength) + 1 

    if char1_roll == char2_roll: 
      print("Both legend's swords clashed and no damage was taken.")
    elif char1_roll > char2_roll: 
      if round == 1: 
        print(f"{char1_name} wins the first blow!")
      else: 
        print(f"{char1_name} wins round {round}!")
      time.sleep(1)
      char2_health -= damage
      print(f"{char2_name} takes a hit, with {damage} damage.\n")
      time.sleep(1)
    elif char2_roll > char1_roll: 
      if round == 1: 
        print(f"{char2_name} wins the first blow!")
      else: 
        print(f"{char2_name} wins round {round}!")
      time.sleep(1)
      char1_health -= damage
      print(f"{char1_name} takes a hit, with {damage} damage.\n")
      time.sleep(1)
    else: 
      print("ERROR! Unable to process round winner.\n")
      exit()

    print(f"{char1_name}\nHealth: {char1_health}\n")
    print(f"{char2_name}\nHealth: {char2_health}\n")
    time.sleep(1)

    if char1_health <= 0: 
      print(f"{char1_name} has died! ☠️\n")
      time.sleep(1)
      winner = char2_name
      loser = char1_name
      break
    elif char2_health <= 0: 
      print(f"{char2_name} has died! ☠️\n")
      time.sleep(1)
      winner = char1_name
      loser = char2_name
      break
    else: 
      print("They're both standing and ready for the next round!\n")
      time.sleep(1)
      # start = input("Press Enter to start the next round: ")
      round += 1 
      continue

  print(f"{winner} destroyed {loser} in {round} rounds!\n")

  choice = input("Battle two more characters?: ").strip().lower()

  if choice == "": 
    exit() 
  elif choice[0] == "y":
    continue
  else: 
    exit()