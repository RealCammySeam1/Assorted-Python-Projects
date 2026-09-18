name = "Cameron"
name = name.lower()
print(name)
name = name.upper()
print(name)
name = "      Cameron       "
print(name)
print(name.strip())

userInput = str(input("Enter the password: "))
password = "321321"

if userInput.lower() == "321321":
    print("Correct!")

if userInput.lower() != "321321":
    print("Incorrect")