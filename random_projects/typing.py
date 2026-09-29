import time
import random

score = 0

print("Type the word that comes up on screen. Press enter to complete. Type 'quit' to exit.")

def chooseWord():
    words = ["green", "yellow", "curtain"]
    return random.choice(words)

word = chooseWord()

def checker():
    global typingInput
    typingInput = input(f"Type: {word}\n\n")

    if typingInput.lower() == "quit":
        print("Program aborted")

    if typingInput.lower() == word:
        print("Success")
        chooseWord()
        checker()

    else:
        print("Incorrect")

checker()