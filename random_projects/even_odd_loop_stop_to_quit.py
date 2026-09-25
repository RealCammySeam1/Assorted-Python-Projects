#GOAL: Make a program that lets the user keep typing numbers, check if they are even/odd!

import sys

userInput = str(input("Enter a number (type 'stop' to quit): ")).strip().lower()
total = 0

#Make a while loop to keep program going until user says stop
while userInput != "stop":

    if userInput == "stop":
        print(f"The running total is {total}")
        sys.exit()

    elif int(userInput) % 2 == 0:
        print("Even") #Print if the input is even or odd
        total += int(userInput) #Add to running total
        userInput = str(input("Enter a number (type 'stop' to quit): ")) #Keep getting input
        print(f"The running total is {total}") #Display total

    elif int(userInput) % 2 != 0:
        print("Odd") #Print if the input is even or odd
        total += int(userInput) #Add to running total
        userInput = str(input("Enter a number (type 'stop' to quit): ")) #Keep getting input
        print(f"The running total is {total}") #Display total