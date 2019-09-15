word = "asdf"
count = 10
guesses = []
def output(guess_array,word="secrate"):
    for w in word:
        if w in guess_array:
            print(w, end=" ")
        else:
            print("_", end=" ")
    print()

for i in range(count):
    guess = input("Type your guess")
    guesses.append(guess)
    output(guesses, word)
    # if word == guess:
    #     print("Matched")
    #     break
    # else:
    #     print("Not matched",count-i-1,"tries remaining")