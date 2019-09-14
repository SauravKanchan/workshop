choice = -1
'''
1 is addition
2 is subtraction
3 is division
0
'''
'''
Task:
Ensure that b is not 0
if user enters b as 0
then tell him that it is not possible.

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
        try:
            print(a/b)
        except ZeroDivisionError:
            print("b cannot be 0")
    elif choice == 0:
        break
    else:
        print("Invalid option")

