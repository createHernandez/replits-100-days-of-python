import csv # DictReader() 

print("Calculating...\n")

total = 0.0 

with open("replits100DaysOfPython_day54_commaSeparatedWhat/Day54Totals.csv") as file: 
    reader = csv.DictReader(file) 
    
    for row in reader: 
        total += float(row["Cost"]) * int(row["Quantity"])

print(f"Total: ${total:,.2f}\n")