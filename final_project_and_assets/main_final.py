"""
===============================================
Assignment [2]
Student Name: [Cameron]
Date: [17/09/2026]

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

import random

atTheStart = True
gameRunning = True
systemHealth = 1000
enemyHealth = 500

def introArt():
    print("████████╗██╗  ██╗███████╗    ███████╗ ██████╗  █████╗ ███╗   ██╗██████╗")
    print("╚══██╔══╝██║  ██║██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗")
    print("   ██║   ███████║█████╗      ██║  ███╗██████╔╝███████║██╔██╗ ██║██║  ██║")
    print("   ██║   ██╔══██║██╔══╝      ██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║  ██║")
    print("   ██║   ██║  ██║███████╗    ╚██████╔╝██║  ██║██║  ██║██║ ╚████║██████╔╝")
    print("   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝")
    print("")
    print("████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗")
    print("╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║")
    print("   ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║")
    print("   ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║")
    print("   ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗")
    print("   ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝")

def intro():
    print("")
    print("Welcome to the Grand Terminal, a window past the desktop.")
    print("Unfortunately, there are issues.")
    print("The system has been sluggish recently.")
    print("You must go through the file system and remove any and all issues.")
    print("")

def optionDeleteSucceed():
    enemyHealth -= 200
    print("You sucessfully removed the malicious program!")

def optionDeleteFail():
    systemHealth -= 100
    print("The program has already rooted itself in other folders. Delete unsuccessfull.")

def optionKillSucceed():
    enemyHealth -= 150
    print("You successfully killed the task, resolving the issue!")

def optionKillFail():
    systemHealth -= 150
    print("The virus has set itself to automatically start on boot! Killing the task does not resolve the issue.")


introArt()
intro()

enemyDirectories = ["/home/user/documents", "/mnt/executor", "/tmp"]
attackOptionsDelete = [optionDeleteFail, optionDeleteSucceed]
attackOptionsKill = [optionKillFail, optionKillSucceed]

def rollChoice():
    global directory
    directory = random.choice(enemyDirectories)

while gameRunning == True:
    if systemHealth <= 0:
        print("You lost. Game over.") 

    def playerTurn():
        rollChoice()
        print(f"There is an issue in '{directory}' ! Navigate to this folder to battle the enemy!")
        print(f"Type 'cd {directory}' to navigate there and start the battle!")
        userInput = str(input("Type directory: "))

        if userInput.lower == directory:
            print("You have made it to the directory! You have two options to attack:")
            print("1. Attempt to kill the program")
            print("2. Attempt to delete the program")
            userInput = str(input("Enter your choice (1/2): "))

            if userInput == "1":
                random.choice(attackOptionsKill)

            if userInput == "2":
                random.choice(attackOptionsDelete)

        else:
            print("You entered the directory wrong!")
            systemHealth -= 50