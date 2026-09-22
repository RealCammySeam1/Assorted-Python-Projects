"""
===============================================
Assignment [2]
Student Name: [Cameron]
Date: [17/09/2026]

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""


# =========================================================
# TASK 1: Vending Machine Program
# ---------------------------------------------------------
# Requirements:
# - Simulate a vending machine with 3 items:
#     1. Chips – $2.00
#     2. Chocolate – $2.50
#     3. Soda – $3.00
# - Ask user to choose an item (1–3)
# - Ask user to insert money
# - If money < cost then print "Not enough money. Transaction cancelled."
# - If money == cost then print "Enjoy your item!"
# - If money > cost then print "Enjoy your item! Your change is $X."
#
# Pseudocode:
# (Write your pseudocode here as comments)
#
# Display prices for each item
# Ask the user which item (as a number)
# Ask the user for amount of money ($)
# Calculate the amount of money minus the price of the item
# If the result of the calculation is greater than zero, display, "Enjoy your item! Your change is ${result of calculation rounded to two decimal points}."
# If the result of the calculation is zero, then display, "Enjoy your item!"
# If the result of the calculation is less than zero, display, "Not enough money. Transaction cancelled."
#
# Flowchart:
# (Attach separately as a PDF document)
#
# Python Code:
# =========================================================
# (Write your Python code here)

"""
import sys

print(
    "Pricing: \n"
    "1: Chips - $2.00\n"
    "2: Chocolate - $2.50\n"
    "3: Soda - $3.00\n"
)

# Set prices as variables
chipsPrice = 2.00
chocolatePrice = 2.50
sodaPrice = 3.00
# totalPrice was an attempt to allow selection of multiple items
totalPrice = 0

# Get and process inputs
foodChoice = float(input("Enter your choice (1, 2, 3): "))

if foodChoice == 1:
    price = chipsPrice
    totalPrice += chipsPrice

elif foodChoice == 2:
    price = chocolatePrice
    totalPrice += chocolatePrice

elif foodChoice == 3:
    price = sodaPrice
    totalPrice += sodaPrice

else:
    print("Invalid choice.")
    sys.exit()

moneyIn = float(input("Enter money : $"))
check = moneyIn - totalPrice

if check < 0:
    print("Not enough money. Transaction canceled.")

if check == 0:
    print("Enjoy your item!")

if check > 0:
    print(f"Enjoy your item! Your change is ${check:.2}")
"""

# =========================================================
# TASK 2: Movie Ticket Price Calculator
# ---------------------------------------------------------
# Requirements:
# - Ask user for age
# - Ask if user is a student (Yes/No)
# - Ticket prices:
#     Under 12 then $8
#     12–17 then $10
#     18–64 then $12
#     65+ then $6
# - If student AND over 12 then $2 discount
# - Output final ticket price
#
# Pseudocode:
# (Write your pseudocode here as comments)
#
# Ask the user for their age
# Ask the user if they're a student
# Choose price based on age
# Subtract $2
# Display the total price
#
# Flowchart:
# (Attach separately as a PDF document)
#
# Python Code:
# =========================================================
# (Write your Python code here)

"""
### Get inputs
age = float(input("Enter your age: "))
student = input("Are you a student? (y/n) ")

### Convert to all lowercase
studentLower = student.lower()

### Create price variable to be modified
price = 0

### Set the price from input
if age < 12:
    price += 8.00
elif age >= 12 and age <= 17:
    price += 10.00
elif age >= 18 and age <= 64:
    price += 12
elif age >= 65:
    price += 6

### Student discount
if studentLower == "y":
    price -= 2

### Display the total
print(f"The total price is: ${price}")
"""

# =========================================================
# TASK 3: Amusement Park Ride Eligibility Checker
# ---------------------------------------------------------
# Requirements:
# - Ask user for height (in cm)
# - Ask user for age
# - Ask if user is accompanied by an adult (Yes/No)
# - Safety Rules:
#     1. Height must be AT LEAST 120 cm to ride.
#     2. If height is 140 cm or taller AND age is 12 or older then
#        "Approved: You can ride alone! Ticket price: $15"
#     3. If height is between 120 cm and 139 cm OR age is under 12 then
#        Must check adult accompaniment:
#        - If accompanied by an adult then
#          "Approved: You can ride with an adult! Ticket price: $10"
#        - Otherwise then
#          "Denied: You need an adult with you to ride."
#     4. If height is under 120 cm then
#        "Denied: You do not meet the height requirement."
#
# Pseudocode:
# (Write your pseudocode here as comments)
# 
# Ask user to input their height
# Ask user to input their age
# Ask if user is accompanied by an adult
# If height is less than 120cm, display, "Denied: You do not meet the height requirement."
# If height is greater than or equal to 140cm AND age is greater than or equal to 12, display, "Approved: You can ride alone! Ticket price: $15"
# If height is greater than or equal to 120 cm AND less than or equal to 139cm OR age is less than 12, then check adult accompaniment
#      If accompanied, then display, "Approved: You can ride with an adult! Ticket price: $10"
#      Else, display, "Denied: You need an adult with you to ride."
#
# Flowchart:
# (Attach separately as a PDF document)
#
# Python Code:
# =========================================================
# (Write your Python code here)

"""
### Get input
height = float(input("Input your height (cm): "))
age = int(input("Input your age: "))
accompanied = str(input("Are you accompanied by an adult (y/n)?"))

### Display approval/denial and price based on age and height
if height < 120:
    print("Denied. You do not meet the height requirement.")
elif height >= 140 and age > 12:
    print("Approved: You can ride alone! Ticket price: $15")
elif height >= 120 and height <= 139:
    if accompanied.lower() == y:
        print("Approved: You can ride with an adult! Ticket price: $10")
    else:
        print("Denied: You need an adult with you to ride.")
"""

# =========================================================
# TASK 4: Bank Loan & Interest Rate Screener NO PSEUDO CODE OR FLOW CHART NEEDED!
# ---------------------------------------------------------
# Requirements:
# - Ask user for:
#     1. Annual income ($)
#     2. Credit score (300–850)
#     3. Existing debt amount ($)
#     4. Preferred loan term in years (15 or 30)
#
# - Initial Loan Qualification (Check FIRST using AND/OR):
#     - To qualify, user must have:
#       (Income >= $45,000 OR Debt == $0) AND Credit Score >= 620
#     - If they do NOT meet this threshold then Print "Loan Denied: High risk applicant."
#
# - Interest Rate Determination (If Qualified, evaluate using NESTED logic):
#     - High Tier: Credit score >= 750 AND Debt < $10,000:
#         - If 15-year term then Base Rate = 4.5%
#         - If 30-year term then Base Rate = 5.0%
#         - Invalid term choice then Print "Error: Invalid term duration."
#     - Standard Tier: Credit score < 750 OR Debt >= $10,000:
#         - If 15-year term then Base Rate = 6.0%
#         - If 30-year term then Base Rate = 6.5%
#         - Invalid term choice then Print "Error: Invalid term duration."
#
# - Discount Check (Apply to Base Rate if valid term was chosen):
#     - If Income > $100,000 AND Debt < $5,000 then Apply a 0.5% discount to Base Rate.
#
# - Output:
#     - Print final approval status and calculated interest rate (e.g., "Loan Approved! Your interest rate is 4.0%").
#
#
# Python Code:
# =========================================================
# (Write your Python code here)

import sys

anIncome = float(input("Enter your annual income ($): "))
creditScore = float(input("Enter your credit score: "))
existingDebt = float(input("Enter your debt amount ($): "))
loanTerm = float(input("Enter your preferred loan term (y): "))

if anIncome >= 45000:
    

if anIncome < 45000:
    sys.exit