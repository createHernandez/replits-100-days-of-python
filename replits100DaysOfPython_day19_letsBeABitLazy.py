print("Loan Calculator\n")

principal = 1000
years = 10
apr = 0.05 
loan_amount = principal
total_interest = 0

print(f"The following is a breakdown of a ${principal:,.2f} loan over {years} years at a {apr:.0%} APR.\n")

for year in range(years): 
  interest = loan_amount * apr
  total_interest += interest
  loan_amount += interest

  print(f"Year {year + 1:<2} is ${round(loan_amount, 2):,.2f}.")

print(f"\nYou paid ${total_interest:,.2f} in interest!")