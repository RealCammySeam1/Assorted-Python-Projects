# ==============================================================================
# PYTHON PRACTICE PROBLEMS
# ==============================================================================



"""
QUESTION 1: Personalized Welcome Banner

Task:
Prompt the user for their name and favorite color using input().
Then, print a three-line banner where:
  - Line 1 is: ***
  - Line 2 says: "Hello [Name], your favorite color is [Color]!"
  - Line 3 is: ***

Concepts tested:
Basic input(), variable assignment, string concatenation or f-strings, print().
"""

# Write your code for Question 1 below:

name = input("Enter your name: ")
colour = input("Enter your favourite colour: ")

print("***")
print(f"Hello {name}, your favourite colour is {colour}!")

"""
QUESTION 2: Simple Age Calculator

Task:
Ask the user to enter their age as an integer. Convert it and print:
  1. How old they will be in 5 years.
  2. Their age in months (age multiplied by 12).

Concepts tested:
Type casting (int()), basic arithmetic (+, *), printing combined text and numbers.
"""

# Write your code for Question 2 below:

age = int(input("Enter your age in years: "))
ageInFiveYears = age + 5
ageInMonths = age * 12

print(f"You will be {ageInFiveYears} old in five years.")
print(f"You are {ageInMonths} months old. (feel old?)")

"""
QUESTION 3: Receipt Total Generator

Task:
Prompt the user to enter:
  - The price of an item (e.g., 19.99)
  - The quantity purchased (e.g., 3)

Calculate the subtotal, calculate a 13% tax on the subtotal, and print 
the final total.

Concepts tested:
Type casting (float(), int()), multi-step arithmetic, floating-point variables.
"""

# Write your code for Question 3 below:

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity purchased: "))

totalBeforeTax = price * quantity
totalAfterTax = totalBeforeTax * 1.13

print(f"Total before tax: ${totalBeforeTax:.2f}")
print(f"Total after tax: ${totalAfterTax:.2f}")

"""
QUESTION 4: Swap Without Extra Code

Task:
Ask the user for two words (word1 and word2).
  1. Print them out in the order entered.
  2. Swap their values using Python's variable assignment trick.
  3. Print them out again to prove they swapped.

Concepts tested:
String variables, multiple variable assignment/swapping (a, b = b, a), 
variable re-assignment.
"""

# Write your code for Question 4 below:

word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")

print(word1, word2)
word1, word2 = word2, word1
print(word1, word2)

# ------------------------------------------------------------------------------
# HARD QUESTIONS
# ------------------------------------------------------------------------------

"""
QUESTION 5: Mad Libs Character Stat Sheet

Task:
Create a mini character sheet generator. Prompt the user for:
  - A character name (string)
  - Base health points (integer)
  - A defense multiplier (float)
  - Is the character a hero? (Ask user to type True/False, convert to boolean)

Calculate the character's Effective Health by multiplying base health by 
the defense multiplier. Print a formatted summary showing every variable 
alongside its data type using the type() function.

Concepts tested:
Multiple data types (str, int, float, bool), type casting (bool()), 
type checking (type()), output formatting.
"""

# Write your code for Question 5 below:

charName = str(input("Enter a character name: "))
baseHealth = int(input("Enter health points: "))
defenceMulti = float(input("Enter the defence multiplier: "))
heroTF = str(input("Is the charactor a hero? (true/false): "))

effectiveHealth = baseHealth * defenceMulti

if heroTF.lower() == "true":
    heroTF = True
elif heroTF.lower() == "false":
    heroTF = False

print()
print(f"Character name:     | {charName}         \n{type(charName)}\n")
print(f"Base health:        | {baseHealth}       \n{type(baseHealth)}\n")
print(f"Defence multiplier: | {defenceMulti}     \n{type(defenceMulti)}\n")
print(f"Effective health:   | {effectiveHealth}  \n{type(effectiveHealth)}\n")
print(f"Hero (true/false):  | {heroTF}           \n{type(heroTF)}\n")



"""
QUESTION 6: Time Converter (Seconds to Hours, Minutes, Seconds)

Task:
Ask the user to input a single large integer representing a total number 
of seconds (e.g., 3665). 

Without using loops or conditional 'if' statements, use integer division (//) 
and modulo (%) to calculate how many hours, minutes, and remaining seconds 
that represents. Print the final formatted result.
(e.g., "1 hour(s), 1 minute(s), and 5 second(s)")

Concepts tested:
Integer division (//), modulo operator (%), multi-step mathematical logic.
"""

# Write your code for Question 6 below:

seconds = int(input("Enter the total number of seconds: "))

secondsRemainder = seconds % 60
minutes = seconds / 60 % 60
hours = seconds / 3600 % 24
days = seconds / 86400

print(f"{days:.0f} days")
print(f"{hours:.0f} hours")
print(f"{minutes:.0f} minutes")
print(f"{secondsRemainder} seconds")