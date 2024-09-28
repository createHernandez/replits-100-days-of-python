import os 

os.system("cls")

websiteInfo = {"Name": None, "URL": None, "Description": None, "Rating": None}

for name, value in websiteInfo.items(): 
    websiteInfo[name] = input(f"{name}: ")

print(f"\n{'-' * 50}\n")

print("Here's your website's info!\n")

for name, value in websiteInfo.items(): 
    print(f"{name}: {value}")
print()
