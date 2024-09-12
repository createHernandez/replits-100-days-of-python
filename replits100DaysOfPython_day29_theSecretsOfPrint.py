# Their version
def print_color(color, word):
  if color=="pink":
    print("\033[95m", word, sep="", end="")
  elif color=="red":
    print("\033[31m", word, sep="", end="")
  elif color=="cyan":
    print("\033[36m", word, sep="", end="")
  else:
    print("\033[0m", word, sep="", end="")

print("Super Subroutine", end="\n\n")

print("With my ", end="")
print_color("pink", "new program")
print_color("reset", " I can just call red('and') ")
print_color("red", "and ")
print_color("reset", "that word will appear in the color I set it to.\n\nWith no ")
print_color("cyan", "weird gaps")
print_color("reset", ".")
print("\n")
print("Epic.\n")

#My version 
# print("Super Subroutine\n")

# def change_color(color, text): 
#     if color == "pink": 
#          text = f"\033[1;95m{text}\033[1;0m"
#     elif color == "red": 
#         text = f"\033[1;31m{text}\033[1;0m"
#     elif color == "cyan": 
#         text = f"\033[1;36m{text}\033[1;0m"
#     else: 
#         text = f"\033[1;0m{text}"
#     return text 

# print(f"""With my {change_color("pink", "new program")} I can just call red("and") {change_color("red", "and")} that word will appear in the color I set it to.\n""")

# print(f"With no {change_color("cyan", "weird gaps")}.\n")

# print("Epic.\n")