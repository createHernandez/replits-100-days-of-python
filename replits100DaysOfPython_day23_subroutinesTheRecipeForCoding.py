def login(): 
  print("Replit Login System\n")
  
  while True: 
    username = input("What is your username?: ")
    password = input("What is your password?: ")
    print()
    if username.strip() == "david" and password.strip() == "baldies4life":
      print("Welcome to Replit!\n")
      break
    else:
      print("Whoops! I don't recognize that username or password. Try again!\n")
      continue

login() 