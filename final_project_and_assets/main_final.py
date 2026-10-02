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

incorrectDirectoryDamage = random.randrange(25, 75)

### Create a function to simplify the printing of enemy and player health
def printHealths():
    print(f"System health: {systemHealth}/1000")
    print(f"Enemy health : {enemyHealth}/500")

### Make the introduction art a function for simplicity
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

### Make the introduction a function for simplicity
def intro():
    global systemHealth
    print("")
    print("Welcome to the Grand Terminal, a window past the desktop.")
    print("Unfortunately, there are issues.")
    print("The system has been sluggish recently.")
    print("You must go through the file system and remove any and all issues.\n")
    printHealths()

### Options for successfull and unsuccessfull attacks for both delete and kill attacks
def optionDeleteSucceed():
    global enemyHealth
    enemyHealth -= 200
    print("You sucessfully removed the malicious program!")

def optionDeleteFail():
    global systemHealth
    systemHealth -= 100
    print("The program has already rooted itself in other folders. Delete unsuccessfull.")

def optionKillSucceed():
    global enemyHealth
    enemyHealth -= 150
    print("You successfully killed the task, resolving the issue!")

def optionKillFail():
    global systemHealth
    systemHealth -= 150
    print("The virus has set itself to automatically start on boot! Killing the task does not resolve the issue.")

enemyDirectories = ["cd /home/user/Documents", "cd /home/user/Downloads", "cd /mnt/executor", "cd /tmp", "cd /home/user/.local"]
attackOptionsDelete = [optionDeleteFail, optionDeleteSucceed]
attackOptionsKill = [optionKillFail, optionKillSucceed]

def rollChoice():
    global enemyDirectories
    global directory
    directory = random.choice(enemyDirectories)

### Call the intro to start the game
introArt()
intro()

while gameRunning == True:
    global playerTurn

    def playerTurn():
        global rollChoice, directory, printHealths, attackOptionsKill, attackOptionsDelete, systemHealth, enemyHealth
        rollChoice()
        print(f"There is an issue in '{directory}' ! Navigate to this folder to battle the enemy!")
        print(f"Type '{directory}' to navigate there and start the battle!")
        userInput = str(input("Type directory: "))

        if userInput == directory:
            print("You have made it to the directory! You have two options to attack:")
            print("1. Attempt to kill the program")
            print("2. Attempt to delete the program")
            userInput = str(input("Enter your choice (1/2): "))

            if userInput == "1":
                random.choice(attackOptionsKill)()
                printHealths()

            if userInput == "2":
                random.choice(attackOptionsDelete)()
                printHealths()

        else:
            print("You entered the directory wrong!")
            systemHealth -= incorrectDirectoryDamage
            print(f"You lost {incorrectDirectoryDamage} HP!\n")
            printHealths()

    if atTheStart == True:
        playerTurn()
        atTheStart = False

    if systemHealth <= 0:
        print("You lost. Game over.") 