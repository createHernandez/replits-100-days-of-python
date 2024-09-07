print("Secure Login")
print("--")
print()

username = input("Username: ")
password = input("Password: ")
print() 

if username == "Mark" and password == "mark": 
  print("What's up Marky Mark!")
elif username == "Suzanne" and password == "suzanne": 
  print("Sup Suzanne!")
elif username == "Joe" and password == "joe": 
  print("Welcome Joe!")
else: 
  print("I dont know who you are! DENIED!")