print("===Story Simulator===")
print()
print("""You're gonna be asked a bunch of questions
then make you up an amazing story
with YOU as the star! 🤩""")
print()
name = input("What is your name?: ")
state = input("What US state would you like to visit?: ")
festival = input("What festival would you like to attend?: ")
first_band_name = input("What is your favorite band?: ")
second_band_name = input("What is your second favorite band?: ")
print()
print("Congradulations", name, "! You have", "\033[32m", "won" ,"\033[0m", "a trip to", state, " where you will get to join", "\033[35m", first_band_name, "\033[0m", "backstage at", festival, ", to watch", "\033[31m", second_band_name, "\033[0m", "play live. Hopefully, you have a great time!")