#GOAL: Make a program that lets the user keep typing numbers, check if they are even/odd!

import sys

userInput = int(input("Enter a number (type '-1' to quit): "))
total = 0
stop = False

#Make a while loop to keep program going until user says stop
while stop == False:

    if userInput == -1:
        stop == True

    elif userInput % 2 == 0:
        print("Even") #Print if the input is even or odd
        total += int(userInput) #Add to running total
        userInput = input("Enter a number (type '-1' to quit): ") #Keep getting input

    elif userInput % 2 != 0:
        print("Odd") #Print if the input is even or odd
        total += int(userInput) #Add to running total
        userInput = input("Enter a number (type '-1' to quit): ") #Keep getting input


print(f"The running total is {total}")