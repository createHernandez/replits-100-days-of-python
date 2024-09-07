print("Math Game!\n")

score = 0 
multiplicand = 1
multiplier = int(input("Name your multiples: "))
print()

for multiplicand in range(1, 11): 
  answer = int(input(f"{multiplicand} x {multiplier} = "))

  product = multiplicand * multiplier

  if answer == product:
    score += 1
    print("\033[0;32mGreat work!\033[0m 🥳\n")
  else: 
    print(f"\033[0;31mNope!\033[0m 😭 The answer was {product}.\n")

print("---\n")

print(f"You scored {score} out of 10!")