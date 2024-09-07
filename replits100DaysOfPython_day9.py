print("Generation Generator")
print()

birth_year = int(input("What year were you born? "))
print() 

if birth_year >= 1925 and birth_year <= 1946:
  print("You're a Traditionalist! 🧑‍🌾")
elif birth_year >= 1947 and birth_year <= 1964:
  print("You're a Baby Boomer! 🍼")
elif birth_year >= 1965 and birth_year <= 1981:
  print("You are Generation X! 🧠")
elif birth_year >= 1982 and birth_year <= 1995:
  print("You're a Millenial! 🥑")
elif birth_year >= 1996 and birth_year <= 2015:
  print("You're Generation Z! 🧑‍💻")
elif birth_year >= 2016 and birth_year <= 2024:
  print("You're Generation Alpha! 👽")
else: 
  print("I don't know what generation you are a part of.")