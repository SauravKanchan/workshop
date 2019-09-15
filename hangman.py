word = "secrate"
for i in range(10):
    guess = input("Type your guess")
    if word == guess:
        print("Matched")
        break
    else:
        print("Not matched",i,"tries remaining")