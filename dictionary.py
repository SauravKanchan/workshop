meaning = {
    "asdf": "It's a string",
    "asf":"asfd"
}

meaning["1"] = "It is a number"
meaning["True"] = "It is a boolean"
try:
    print(meaning[input("Enter your word")])
except KeyError:
    print("Word not in dictionary")
'''
Task is to make a program 
which takes word/key as input from user
and print its meaning/value 
using dictionary
'''