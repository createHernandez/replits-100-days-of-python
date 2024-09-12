def print_color(color):
  if color=="red":
    return ("\033[31m")
  elif color=="white":
    return ("\033[0m")
  elif color=="blue":
    return ("\033[34m")
  elif color=="yellow":
    return ("\033[33m")
  elif color == "green":
    return ("\033[32m")
  elif color == "purple":
    return ("\033[35m")


# Interface #1 

title = f"{print_color('red')}={print_color('white')}={print_color('blue')}= {print_color('yellow')}Music App {print_color('blue')}={print_color('white')}={print_color('red')}="

print(f"        {title:^35}\n")
print(f"🔥▶️    {print_color('white')}Radio Gaga")
print(f"    {print_color('yellow')}Queen")

prev = "prev"
next = "next"
pause = "pause"

print(f"{print_color('white')}{prev:<35}")
print(f"{print_color('green')}{next:^35}")
print(f"{print_color('purple')}{pause:>35}")

# Space Between Interfaces 
print()
print()

# Interface #2

text = "WELCOME TO"
print(f"{print_color('white')}{text:^35}")
text = "--  ARMBOOK  --"
print(f"{print_color('blue')}{text:^35}\n")
text = "Definitely not a rip off"
print(f"{print_color('yellow')}{text:>35}")
text = "a certain other social"
print(f"{print_color('yellow')}{text:>35}")
text = "networking site"
print(f"{print_color('yellow')}{text:>35}")
text = "Honest."
print(f"\n{print_color('red')}{text:^35}\n")
text = "Username: "
username = input(f"{print_color('white')}{text:^35}")
text = "Password: "
username = input(f"{print_color('white')}{text:^35}")
print()