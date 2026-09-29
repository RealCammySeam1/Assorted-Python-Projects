var = "python"

#Printing indexes of a string (Notice that 0 is mapped to P)
print(var[0])
print(var[1])
print(var[2])
print(var[3])
print(var[4])

for letter in var:
    print(letter)
#var.isdigit() VS var.isalpha()

print(var.isalpha())
print(var.isdigit())

#Using the 'in' command
if "th" in var:
    print("th is in the variable")
else:
    print("th is not in the variable")