name = str(input("Enter your name: "))
if name.isnumeric() == False:
    print(name*3)
else:
    print("Please type only letters.")

name = "Last" + "First"
print("Your name is: " + name)
print(name[0])
print(name[::-1]) #Fip a string