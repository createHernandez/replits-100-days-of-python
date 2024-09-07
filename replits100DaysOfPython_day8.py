print("It's Generator Time!")
print()

name = input("Who are you? ")
print()
day = input("What day is it? ")
print()
choice = input("Do you want to be insulted 😈 or complimented 😊? ")
print()

if choice == "insulted":
  print("Custom Insult Generator")
  print()
  if name == "Dave" or name == "dave": 
    print("Alright Baldy? How's tricks?")
  elif day == "Monday" or day == "monday": 
    print("Not you again. Can you stop tapping your fingers on my keyboard please?")
  elif day == "Tuesday" or day == "tuesday":
    print("Dude, lose my phone number!")
  else: 
    print("You're not the brightest tool in the toolshed. Huh.")
  
elif choice == "complimented":
  print("Custom Affirmation Generator")

  if name == "Jessica" or name == "jessica": 
    print("You look nice today")
  if day == "Wednesday" or day == "wednesday":
    print("Today you're going to make an impact and change the world!")
  if day == "Thursday" or day == "thursday":
    print("Keep on keeping going!")
  else: 
    print("You're awesome!")

else: 
  print("Hmm... I don't know what you want to do.")