# def reverse(value): 
#     if value <= 0: 
#         print("Done!\n")
#         return
#     else: 
#         for i in range(value): 
#             print("⚽", end="")
#         print()
#         reverse(value - 2)

# reverse(21)

def factorial(value): 
    if value == 1: 
        return 1
    else: 
        return value + factorial(value - 1) 

# MAIN PROGRAM 
print(f"Calculating Factorials\n")

value = input("What is the value?: ")
print()

print(f"{value}! = {factorial(int(value))}\n")
