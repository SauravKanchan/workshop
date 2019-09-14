choice = -1
'''
1 is addition
2 is subtraction
3 is division
0
'''
while choice != 0:
    a=int(input("Enter your first number"))
    b=int(input("Enter your second number"))
    choice = int(input("Enter your choice"))
    if choice == 1:
        print(a+b)
    elif choice==2:
        print(a-b)
    elif choice == 3:
        print(a/b)
    elif choice == 0:
        break
    else:
        print("Invalid option")

