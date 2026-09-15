"""
===============================================
Assignment 1 - Python Programming
Student Name: Cameron Seamone
Date: 9/11/2026

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

# =======================================================
# Question 1: Say Hello
# Write a program that asks the user for their name
# and prints: Hello, <name>!
# =======================================================

# --- Put your code here ---

### Get input
name = input("Your name: ")

### Print
print(f"Hello, {name}")

# =======================================================
# Question 2: Adding Numbers
# Ask the user to enter two numbers. Add them together
# and print the result.
# =======================================================

# --- Put your code here ---

### Get input
num1 = int(input("Input first number: "))
num2 = int(input("Input second number: "))

### Calculate
sum1 = num1 + num2

### Print
print(f"The sum is {sum1}")

# =======================================================
# Question 3: Average of Three Numbers
# Ask the user to enter three numbers. Calculate the
# average and print it.
# =======================================================

# --- Put your code here ---

### Get input
num3 = float(input("Input first number: "))
num4 = float(input("Input second number: "))
num5 = float(input("Input third number: "))

### Calculate
sum2 = num3 + num4 + num5
avg = sum2 / 3

### Print
print(f"The average is {avg}")

# =======================================================
# Question 4: Pizza Shop – Calculate Tax
# Ask the user to enter the total cost of their order.
# Calculate 13% tax and print the total amount including tax.
# ===============

# --- Put your code here ---

### Get input
price = float(input("Price in dollars: "))

### Calculate
taxDecimal = 0.13
taxAmount = taxDecimal * price
total = taxAmount + price

### Print
print(f"Price before tax: {price:.2f}")
print(f"Tax amount: {taxAmount:.2f}")
print(f"Total: {total:.2f}")

# =======================================================
# Question 5: Rectangle Area Calculator.
# Ask the user to enter the length and width of a rectangle.
# Calculate the area of the rectangle.
# Print the answer in a clear message.
# =======================================================

# --- Put your code here ---

### Get input
length = float(input("Enter the length of the rectangle (cm): "))
width = float(input("Enter the width of the rectangle (cm): "))

### Calculate
area = length * width

### Print
print(f"The area of the rectangle is {area}cm")

# =======================================================
# Question 6: Tip Calculator
# Ask the user to enter the total bill amount at a restaurant.
# Ask the user to enter a tip percentage (e.g., 15 for 15%).
# Calculate the tip amount and the total bill including tip.
# Print both values clearly.
# =======================================================

# --- Put your code here ---

### Get input
price1 = float(input("Enter bill amount: "))
tipPercent = float(input("Enter tip amount as a percent: "))

### Calculate
tipDecimal = tipPercent / 100
tipAmount = tipDecimal * price1
total1 = tipAmount + price1

### Print
print(f"Tip amount: {tipAmount:.2f}")
print(f"Total: {total1:.2f}")