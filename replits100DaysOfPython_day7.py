favorite_band = input("What is your favorite NuMetal Band?: ")

if favorite_band == "System of a Down": 
  print("\nNice stable choice.\n")
  
  favorite_song = input("What's your favorite song?: ")
  if favorite_song == "Chop Suey":
    print("\nRight answer!\n")
  else: 
    print("\nNah, Chop Suey is the best.\n")
    
elif favorite_band == "Korn":
  print("\nMm dung da hoong dung da hoog a!\n")

  favorite_song = input("What's your favorite song?: ")
  if favorite_song == "Taken":
    print("\nRight answer\n")
  else: 
    print("\nMeh, Taken is better.\n")
    
elif favorite_band == "Linkin Park":
  print("\nRIP Chester Bennington!\n")

  favorite_song = input("What's your favorite song?: ")
  if favorite_song == "In the End\n":
    print("\nRight answer\n")
  else: 
    print("\nNah, In the End was their best.\n")
    
else: 
  print("Yeah, that's cool and all...\n")