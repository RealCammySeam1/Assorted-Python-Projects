for i in range(1,10):
    print(i)

user = int(input("Enter a number (type -1 to quit): "))

total = 0
while user != -1:
    total = total + user
    print(f"The running total is {total}")
    user = int(input("Enter a number (type -1 to quit): "))

print("Your time has come to an end.")

flag = True
while flag == True or user != -1:
    print("running...")
    while flag == False:
        print("TERMINATED")

    ### DO NOT USE BREAK