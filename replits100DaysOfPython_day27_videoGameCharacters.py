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
  print("May your name go down in Legend...\n")
  time.sleep(.5)

def print_menu(): 
  os.system("clear")
  
  print("⚔️ CHARACTER BUILDER ⚔️\n")

  time.sleep(.5)

while True: 
  print_menu()

  name, type, health, strength = generate_character()

  print_character(name, type, health, strength)

  choice = input("Again?: ")

  if choice[0].strip().lower() == "y":
    continue
  else: 
    exit()