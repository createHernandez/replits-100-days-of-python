import os

def get_star_wars_name(): 
    first_name = input("What is your first name?: ").strip().lower()

    surname = input("What is your surname?: ").strip().lower()

    moms_maiden_name = input("What is your Mom's maiden name?: ").strip().lower()

    birth_city = input("What city were you born in?: ").strip().lower()
    print()

    star_wars_name = f"{first_name[0:3]}{surname[0:2]} {moms_maiden_name[0:2]}{birth_city[-3::1]}"

    return star_wars_name

os.system("cls")

print(f"Your Star Wars name is {get_star_wars_name().title()}.\n")