userInput = input("Enter your code here: ")
word = ""

for letter in userInput:
    if letter.isalpha() == True:
        word += letter
        
print("Decoded result: ")
print(word)