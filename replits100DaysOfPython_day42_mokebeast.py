import os #system()

mokeBeast = {"Beast Name": None, 
             "Type": None, 
             "Special Move": None, 
             "HP": None, 
             "MP": None }

def get_mokebeast(): 
  for key in mokeBeast: 
    mokeBeast[key] = input(f"{key}: ").strip()
  print()

def print_main_menu(): 
  os.system("cls")
  print("MokéBeast\n")

def print_type_color(type):
  if type == "earth": 
    return "\033[32m"
  elif type == "fire": 
    return "\033[31m"
  elif type == "wind":
    return "\033[0m"
  elif type == "water":
    return "\033[34m" 
  elif type == "lightning":
    return "\033[33m" 
  elif type == "ghost":
    return "\033[35m" 
  else: 
    return "\033[0m" 

def print_mokeBeast(): 
  print("Here's your MokéBeast's info!\n")

  print(f"{'-' * 50}")

  print(f"{print_type_color(mokeBeast['Type'])} ")

  for key, value in mokeBeast.items(): 
    print(f"{key}: {value}") 
  
  print(f"{print_type_color('default')} ")

# MAIN PROGRAM 
print_main_menu()

get_mokebeast()

print_mokeBeast()