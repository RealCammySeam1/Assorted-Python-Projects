#Get number from user
userInput = int(input("Input a number: "))
print()

#Create variables for total odd and even
odd = 0
even = 0

#Calculate if each number is even or odd and print it
if userInput > 0:
    for i in range(1, userInput+1):
        if i % 2 == 0:
            print(f"{i} Even")
            even += 1
        elif i % 2 != 0:
            print(f"{i} Odd")
            odd += 1
    print()
    print(f"Input: {userInput}")
    print(f"Even: {even}")
    print(f"Odd: {odd}")

if userInput <= 0:
    print("Error: Negative numbers are not allowed, please restart the program")

