from getpass import getpass as input 

print("2 Player 🪨 📄 ✂️\n")

print("Select your move using R, P or S.\n")

player1 = input("Player 1 > ")
print()
player2 = input("Player 2 > ")
print()

if player1[0].upper() == 'R': 
  if player2[0].upper() == 'R':
    print("It's a tie!")
  elif player2[0].upper() == 'P': 
    print("Player 2 wins!")
  elif player2[0].upper() == 'S':
    print("Player 1 wins!")
  else: 
    print("ERROR: Invalid input!")
    
elif player1[0].upper() == 'P': 
  if player2[0].upper() == 'R':
    print("Player 1 wins!")
  elif player2[0].upper() == 'P': 
    print("It's a tie!")
  elif player2[0].upper() == 'S':
    print("Player 2 wins!")
  else: 
    print("ERROR: Invalid input!")
    
elif player1[0].upper() == 'S': 
  if player2[0].upper() == 'R':
    print("Player 2 wins!")
  elif player2[0].upper() == 'P': 
    print("Player 1 wins!")
  elif player2[0].upper() == 'S':
    print("It's a tie!")
  else: 
    print("ERROR: Invalid input!")

else: 
  print("ERROR: Invalid input!")