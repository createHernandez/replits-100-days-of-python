print("What does the ... say?\n")

condition = True

while (condition): 
  animal = input("What animal do you want?: ")

  if animal.lower() == "cow": 
    print("A cow goes moo.\n")
  elif animal.lower() == "lesser spotted lemur": 
    print("Ummm...the Lesser Spotter Lemur goes awooga.\n")
  elif animal.lower() == "dog": 
    print("A dog goes woof.\n")
  elif animal.lower() == "cat": 
    print("A cat goes meow.\n")
  elif animal.lower() == "sheep": 
    print("A sheep goes baa.\n")
  elif animal.lower() == "fox": 
    print("Ring-ding-ding-ding-dingeringeding!\n")
  else: 
    print("I don't know that animal.\n")

  answer = input("Do you want to exit?: ")
  print()

  if answer[0].upper() == 'Y': 
    condition = False 
  else: 
    condition = True 