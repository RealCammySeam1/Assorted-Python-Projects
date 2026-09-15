"""

num_1 = input("Enter your first number: ")
num_2 = input("Enter your Second number ")

answer = num_1 + num_2
print(answer)

"""
### The error in the above code is that the inputs are strings, not integers or floats.
### Fixed code is below.

num_1 = float(input("Enter your first number: "))
num_2 = float(input("Enter your Second number "))

answer = num_1 + num_2
print(answer)