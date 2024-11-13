# # NOTES 
# # f = open(file name, Mode)
# # Opens the file you want to write to. 
# f = open("replits100DaysOfPython_day48_savingToFiles/savedFile.txt", "w")

# # f.write(Data to be put in the file)
# # Writes the data you want to save. 
# f.write("Hello World!")

# # f.close()
# # Saves the changes to the file back to the file system. 
# f.close()

print("HIGH SCORE TABLE\n")


while True: 
    f = open("replits100DaysOfPython_day48_savingToFiles/high.score", "a+")

    initials = input("INITIALS > ").strip().upper()

    while (len(initials) < 0 and len(initials) > 3): 
        initials = input("INITIALS > ").strip().upper()

    score = int(input("SCORE > ").strip())
    print()

    f.write(f"{initials} {score}\n")

    print("ADDED\n")

    choice = input("Again?: ").strip().lower()
    print()

    if choice[0] == 'y': 
        continue
    else: 
        print("Exiting...\n")
        f.close()
        break 