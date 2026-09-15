###If and else Lessons

user_input = str(input("Enter the password: "))
passwd = 321321

if user_input == passwd:
    print("Hello")

###Use != if you want to know it the two things are NOT equal

elif user_input != passwd:
    print("Incorrect")
    print("Session terminated")
    exit

else:
    print("How?")
    print("Session terminated")
    exit

age = int(input("Enter your age: "))

if age >= 18:
    print("You can drive")

else:
    print("You can not drive")
    exit