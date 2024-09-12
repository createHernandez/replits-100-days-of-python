print("30 Days Down - What did you think?\n")

for i in range(1, 31): 
    thoughts = input(f"Day {i}: \n")

    summary = f"You thought Day {i} was"

    print(f"\n{summary:^35}")
    print(f"{thoughts:^35}\n")