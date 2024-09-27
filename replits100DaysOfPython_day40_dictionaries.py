contactCard = {}

contactCard["Name"] = input("What is your name?: ").strip().title()
contactCard["DOB"] = input("What is your date of birth?: ").strip()
contactCard["Phone"] = input("What's your phone number?: ").strip()
contactCard["Email"] = input("What is the best email for you?: ").strip()
contactCard["Address"] = input("Where can we send you mail?: ").strip()

print(f"\n{'-' * 50}\n")

print("Here's your contact card!\n")

for key in contactCard: 
    print(f"{key}: {contactCard[key]}")
print()
