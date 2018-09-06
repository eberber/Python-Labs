from builtins import print
import random
import string

print("welcome to hangman by Edgar Berber!")
word = random.choice(open("capitals.txt").readlines()) #read txt file and pick rand line
word = word.rstrip() #remove trailing newline

match = "_" * len(word)
print(match)
print('length is: ', len(match))
i = 0

while match != word:
    name = input("Guess a letter:  ").upper()
    type(name)
    print("letter is: ", name)
    word = list(word)

    while i < len(word): #loop through entire string
        if name == word[i]: #on match set that element in match to element in name
            print('match found at element: ', i)
            match = list(match)
            match[i] = name
            match = "".join(match)
        if word[i] == ",": #skip comma
            match = list(match)
            match[i] = word[i]
            match = "".join(match)
        if word[i] == " ": #skip white space
            match = list(match)
            match[i] = word[i]
            match = "".join(match)

        i = i + 1
    i = 0
    word = "".join(word)
    print(match, '\n')
print('Congrats you won!')


