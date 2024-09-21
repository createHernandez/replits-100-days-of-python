import os #system()
import time #sleep()

# email_list = []
#test list 
email_list = ["john@test.com", "sian@coolhairsian.com", "bobthebuilder@gmail.com", "billyjoel@aol.com", "samanthatabatha@me.com", "billyandmandy@cn.com", "another@email.com", "andanother@gmail.com", "oooyeah@gmail.com", "something@gmail.com", "thingsandstuff@gmail.com"]

# def print_email_list():
#     print("Printing the current email list...\n")
#     time.sleep(1)

#     # total_characters = pipe + space + 2 + space + pipe + space + email_length + space + pipe
#     total_characters = 9

#     for email in range(0, len(email_list)): 
#         print(f"{email + 1:>2}: {email_list[email]}")
#         time.sleep(.25)

#     print("\nEnd of the list.")
#     time.sleep(5)

def print_email_list():
    # Look: 
    # ===============================================
    # |  1 | someemail@gmail.com                    |
    # |  2 | anotheremailthatisreallylong@gmail.com |
    # |  3 | bobthebuilder@build.com                |

    # 123456789
    # |    | email | 
 
    longest_email_length = -1

    for email in range(0, len(email_list)): 
        if longest_email_length < len(email_list[email]): 
            longest_email_length = email 
    
    print(longest_email_length)
    line = '-'

    print(line * longest_email_length + line * 9)
        
    print("Printing the current email list...\n")
    time.sleep(1)

    line = '-'
    space = ' '

    print(line * 9 + line * longest_email_length)
    for email in range(0, len(email_list)): 
        space = space * (longest_email_length - len(email_list[email]))
        print(f"| {email + 1:>2} | {email_list[email]} |")
        time.sleep(.25)
    print(line * 9 + line * longest_email_length)
    print("\nEnd of the list.")
    time.sleep(5)

def add_email(): 
    email = input("Email to add: ")
    print()

    if email in email_list: 
        print("Email is already in the list.\n\nReturning to main menu...")
        time.sleep(1)
    elif email not in email_list: 
        email_list.append(email)
        print_email_list()
        print("Returning to the main menu...\n")
        time.sleep(1)
    else: 
        print("ERROR! Unable to add email to the list.\n\nReturning to main menu...")
        time.sleep(1)

def remove_email(): 
    print_email_list()
    print()
    email = input("Email to remove: ")
    print()
    if email in email_list: 
        email_list.remove(email)
        print_email_list()
        print("Returning to the main menu...\n")
        time.sleep(1)
    else: 
        print("ERROR! Unable to find that email.")
        time.sleep(1)

def show_emails(): 
    print_email_list()
    print("Returning to the main menu...\n")
    time.sleep(1)

def get_spamming(): 
    for email in range(0, 11): 
        os.system("cls")

        print(f"Email {email + 1}\n")
        time.sleep(1)

        print(f"Dear {email_list[email]}")
        print("It has come to our attention that your're missing out on \nthe amazing Replit 100 days of code. We insist you do it \nright away. If you don't we will pass on your email\naddress to every spammer we've ever encountered and also\nsign you up to the My Little Pony newsletter, because\nthat's neat. We might just do that anyway.\n")
        time.sleep(1)

        print("Love and hugs,\n")
        time.sleep(1)
        
        print("Ian Spammington III\n")
        time.sleep(2)
    print("Returning to the main menu...\n")
    time.sleep(1)

def print_main_menu(): 
    print("SPAMMER Inc.\n")
    time.sleep(1)

    print("1: Add email")
    time.sleep(1)
    print("2: Remove email")
    time.sleep(1)
    print("3: Show emails")
    time.sleep(1)
    print("4: Get SPAMMING")
    time.sleep(1)
    print()


while True: 
    os.system("cls")

    print_main_menu()

    choice = int(input(">> "))
    print()

    if choice == 1: 
        add_email()
        continue
    elif choice == 2: 
        remove_email()
        continue
    elif choice == 3: 
        show_emails()
        continue
    elif choice == 4: 
        get_spamming()
    else: 
        print("Exiting the program...")
        time.sleep(1)
        exit()