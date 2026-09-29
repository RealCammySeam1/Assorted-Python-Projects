def hello(): #Function
    print("\n" "hi river." "\n")

def bye():
    var = "python"
    for letter in var():
        print(letter)

def getPlayerName():
    name = str(input("Enter the name of the player: "))
    return name

def add(x,y):
    return x+y

def blanc(): #Setting a blank function (temporary)
    pass

#MAIN
hello() #Call a function call
x = 1
y = 1
print(add(x, y), "\n")

playerName = getPlayerName()
print(f"The name of the player is {playerName}.")