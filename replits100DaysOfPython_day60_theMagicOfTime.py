# import datetime # date() 

# myDate = datetime.date(year=2022, month=12, day=7) 
# print(myDate)

# today = datetime.date.today() 
# print(today)

# day = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))
# date = datetime.date(year, month, day)
# print(date)

# difference = datetime.timedelta(days=14)
# newDate = today + difference
# print(newDate)

# today = datetime.date.today() 
# holiday = datetime.date(year=2022, month=10, day=30)
# if holiday > today: 
#     print("Coming soon")
# elif holiday < today: 
#     print("Hope you enjoyed it!")
# else: 
#     print("HOLIDAY TIME!")

import datetime # date(), date.today() 

print("EVENT COUNTDOWN\n")

today = datetime.date.today() 

event_name = input("What's the event?: ")
day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

event = datetime.date(year, month, day)

if event > today: 
    print("😃😃😃 It's gonna happen soon!")
elif event < today: 
    print(f"😭😭😭 You missed {event_name} by {(today - event).days} days...")
else: 
    print("🥳🥳🥳 It's today!")
print()