import os 

def print_color(color):
  if color=="r":
    print("\033[31m", end="")
  elif color==" ":
    print("\033[0m", end="")
  elif color=="b":
    print("\033[0;34m", end="")
  elif color=="y":
    print("\033[33m", end="")
  elif color == "g":
    print("\033[32m", end="")
  elif color == "p":
    print("\033[35m", end="")

os.system("cls")

sentence = input("What sentence do you want rainbow-ising?\n>> ")
# sentence = "Become one with the rainbow my young rainbowan"
print()

for letter in sentence: 
    print_color(letter.lower())
    print(letter, end="")
print("\033[0m\n")
