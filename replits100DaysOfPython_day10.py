total_bill = float(input("How much is the bill?: "))
print()
tip_percent = float(input("What percent would you like to tip?: "))
print()
tip_percent = tip_percent / 100
tip_amount = total_bill * tip_percent
total_bill = total_bill + tip_amount
number_of_people = int(input("How many people are paying?: "))
split_amount = total_bill / number_of_people
print()
print("You all owe ", split_amount)