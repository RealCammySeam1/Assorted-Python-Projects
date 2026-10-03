userInput = int(input("Enter an even number: "))
number = 0
total = 0

if userInput %2 == 0:
    while number != userInput:
        number += 2
        total += number
        print(number)
        if number == userInput:
            print(f"The sum of all numbers is: {total}")

if userInput %2 != 0:
    print("Please enter an even number.")