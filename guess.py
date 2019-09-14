number = "5"
choice = ""
while number != choice:
    choice = input("Enter your number")
    if choice == number:
        print("Number matched")
    else:
        print("Not matched")