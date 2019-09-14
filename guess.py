from random import randrange
number = randrange(1,10)
# print(number)
choice = ""
while number != choice:
    choice = int(input("Enter your number"))
    if choice == number:
        print("Number matched")
    else:
        if choice> number:
            print("Please enter a lower value")
        else:
            print("Enter a higher value")