word = "secrate"
count = 10
for i in range(count):
    guess = input("Type your guess")
    if word == guess:
        print("Matched")
        break
    else:
        print("Not matched",count-i-1,"tries remaining")