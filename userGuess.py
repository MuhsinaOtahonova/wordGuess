import random
from uzwords import words

def get_word():
    index = random.randint(0, len(words)-1)
    # word = random.choice(words)
    # return word
    return words[index]

def display(letters, word):
    for letter in word:
        if letter in letters:
            print(letter, end=" ")
        else:
            print("_", end=" ")

def checkLetter(guessLetters, word):
    for letter in word:
        if letter not in guessLetters:
            return False
    return True

def userGuess():
    count = 0
    word = get_word()
    print(word)
    letters = []
    print(f"I have a {len(word)}-letter word. Can you guess it?")
    while 1:
        if checkLetter(letters,word) == True:
            print(f"You found it in {count-1} attempts.")
            break
        else:
            count += 1
            letter = input("Enter a letter.")
            if letter not in letters:
                letters.append(letter)
            else:
                letter = input("You have already entered this letter, please enter another one.")
            print(f"Entered letter(s): {letters}")
            display(letters,word)

