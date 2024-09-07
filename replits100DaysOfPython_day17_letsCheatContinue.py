from getpass import getpass as input 

print("2 Player 🪨 📄 ✂️\n")

condition = True
player1_score = 0
player2_score = 0

print("Select your move using R, P or S.\n")

while condition:   
  player1 = input("Player 1 > ")
  player2 = input("Player 2 > ")
  
  if player1[0].upper() == 'R': 
    if player2[0].upper() == 'R':
      print("It's a tie!\n")
    elif player2[0].upper() == 'P': 
      print("Player 2 wins the round!\n")
      player2_score += 1
    elif player2[0].upper() == 'S':
      print("Player 1 wins the round!\n")
      player1_score += 1
    else: 
      print("ERROR: Invalid input!")
  
  elif player1[0].upper() == 'P': 
    if player2[0].upper() == 'R':
      print("Player 1 wins the round!\n")
      player1_score += 1
    elif player2[0].upper() == 'P': 
      print("It's a tie!\n")
    elif player2[0].upper() == 'S':
      print("Player 2 wins the round!\n")
      player2_score += 1
    else: 
      print("ERROR: Invalid input!\n")
  
  elif player1[0].upper() == 'S': 
    if player2[0].upper() == 'R':
      print("Player 2 wins the round!\n")
      player2_score += 1
    elif player2[0].upper() == 'P': 
      print("Player 1 wins the round!\n")
      player1_score += 1
    elif player2[0].upper() == 'S':
      print("It's a tie!\n")
    else: 
      print("ERROR: Invalid input!\n")
  
  else: 
    print("ERROR: Invalid input!\n")

  if player1_score == 3:
    print("Player 1 won the game!\n")
    condition = False 
    break
  elif player2_score == 3: 
    print("Player 2 won the game!\n")
    condition = False
    break
  elif (player1_score < 3 and player1_score >= 0) or (player2_score < 3 and player2_score >= 0):
    continue
  else: 
    print("ERROR! Unable to process game winner.\n")
    condition = False
    exit()

print("Thanks for playing!")