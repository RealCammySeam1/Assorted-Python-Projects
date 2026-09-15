#Printing the type of variables/data types
print(type(5))
print(type("4"))
print(type(True))
print(type(3.12345))

#Nesting if and else statements

user_input = str(input("Enter yes or no: "))
age = int(input("Enter your age: "))

if user_input == "yes" or user_input == "YES":
    if age >= 15 and age != 0:
        print("Hello")

    else:
        print("You failed.")

else:
    print("Okay.")