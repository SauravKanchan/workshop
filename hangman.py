word = "asdf"
count = 10
guesses = []
def output(guess_array,word="secrate"):
    fail = False
    for w in word:
        if w in guess_array:
            print(w, end=" ")
        else:
            fail = True
            print("_", end=" ")
    print()
    return fail

for i in range(count):
    guess = input("Type your guess")
    guesses.append(guess)
    result = output(guesses, word)
    if result:
        print("Not matched", count - i - 1, "tries remaining")
    else:
        print("You have won")
        break