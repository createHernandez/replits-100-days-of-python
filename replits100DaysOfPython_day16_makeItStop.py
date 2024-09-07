print("Fill-in the Blank Lyrics!\n")
print("(Type in the blank lyrics and see if you are as cool as me.)\n\n")

attempts = 1 

while True: 
  lyric = input("Never going to ______ you up.\n")

  print() 
  
  if lyric == "give":
    break
  else: 
    print("Nope, try again.\n")
    attempts += 1

print("Well done! It only took you", attempts, "attempts.")