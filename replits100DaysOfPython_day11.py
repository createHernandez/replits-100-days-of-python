print("How many seconds are in a year?")
print()

print("Let's find out!")
leap_year = input("Is it a leap year? ")
print()

seconds = 60 
minutes = 60
hours = 24
days = 365
months = 12

sec_in_year = seconds * minutes * hours * days 

if leap_year == "Yes" or leap_year == "yes" or leap_year == 'Y' or leap_year == 'y': 
  sec_in_leap_year = sec_in_year + (seconds * minutes * hours)
  print(f"There are {sec_in_leap_year:,} seconds in this leap year.")
else: 
  print(f"There are {sec_in_year:,} seconds in the year.")