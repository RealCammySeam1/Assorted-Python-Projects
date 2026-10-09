"""
===============================================
Assignment [2]
Student Name: [Cameron Seamone]
Date: [17/09/2026]

By typing my name above, I confirm that this is my own work
and I have not plagiarized or copied code from others or AI sources.
===============================================
"""

import random, time, sys

atTheStart = True
gameRunning = True
systemHealth = 1000
enemyHealth = 500

### Set ranges for damage, to be used by random.randint
incorrectDirectoryDamage = random.randrange(25, 75)
optionDeleteSucceedDamage = random.randrange(150, 300)
optionDeleteFailDamage = random.randrange(75, 150)
optionKillSucceedDamage = random.randrange(100, 200)
optionKillFailDamage = random.randrange(100, 200)

### Create a function to simplify the printing of enemy and player health
def printHealths():
    print()
    printSystemHealth = f"System health: {systemHealth}/1000\n"
    printEnemyHealth = f"Enemy health : {enemyHealth}/500\n"

    for letter in printSystemHealth:
        print(letter, end='', flush=True)
        time.sleep(.01)

    for letter in printEnemyHealth:
        print(letter, end='', flush=True)
        time.sleep(.01)

### Make the introduction art a function for simplicity (made with artificial intelligence)
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
    print()
    introLine1 = "Welcome to the Grand Terminal, a window past the desktop.\n"
    introLine2 = "Unfortunately, there are issues.\n"
    introLine3 = "The system has been sluggish recently.\n"
    introLine4 = "You must go through the file system and remove any and all issues.\n"

    for letter in introLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

    for letter in introLine2:
        print(letter, end='', flush=True)
        time.sleep(.01)

    for letter in introLine3:
        print(letter, end='', flush=True)
        time.sleep(.01)

    for letter in introLine4:
        print(letter, end='', flush=True)
        time.sleep(.01)

    print()
    printHealths()

### Options for successfull and unsuccessfull attacks for both delete and kill attacks
def optionDeleteSucceed():
    global enemyHealth
    enemyHealth -= optionDeleteSucceedDamage
    optionDeleteSucceedLine1 = "You sucessfully removed the malicious program!\n"

    for letter in optionDeleteSucceedLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

def optionDeleteFail():
    global systemHealth
    systemHealth -= optionDeleteFailDamage
    optionDeleteFailLine1 = "The program has already rooted itself in other folders. Delete unsuccessfull.\n"

    for letter in optionDeleteFailLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

def optionKillSucceed():
    global enemyHealth
    enemyHealth -= optionKillSucceedDamage
    optionKillSucceedLine1 ="You successfully killed the task, resolving the issue!\n"

    for letter in optionKillSucceedLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

def optionKillFail():
    global systemHealth
    systemHealth -= optionKillFailDamage
    optionKillFailLine1 = "The virus has set itself to automatically start on boot! Killing the task does not resolve the issue.\n"

    for letter in optionKillFailLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

### Make asking if the user wants to continue a function for simplifictaion
def userWantContinue():
    continueTF = str(input("Do you want to continue? (y/n): "))
    if continueTF == "y":
        playerTurn()
        print()

enemyDirectories = ["cd /home/user/Documents", "cd /home/user/Downloads", "cd /mnt/executor", "cd /tmp", "cd /home/user/.local", "cd /home/user/.local/share", "cd /var/tmp"]
attackOptionsDelete = [optionDeleteFail, optionDeleteSucceed]
attackOptionsKill = [optionKillFail, optionKillSucceed]

### Choose a random directory to print, as a function for simplification
def rollChoice():
    global enemyDirectories
    global directory
    directory = random.choice(enemyDirectories)

navigateFailProbability = ["true", "true", "true", "false"]

### Call the intro functions to start the game
introArt()
intro()

while gameRunning == True:

    def playerTurn(): ### Make the majority of the game a function so it can be called easily
        global rollChoice, directory, printHealths, attackOptionsKill, attackOptionsDelete, systemHealth, enemyHealth, navigateFailProbability
        rollChoice() ### Choose a random directory from the list by calling the "rollChoice" function
        playerTurnLine1 = f"There is an issue in '{directory}' ! Navigate to this folder to battle the enemy!\n"
        playerTurnLine2 = f"Type '{directory}' to navigate there and start the battle!\n"

        for letter in playerTurnLine1:
            print(letter, end='', flush=True)
            time.sleep(.01)

        for letter in playerTurnLine2:
            print(letter, end='', flush=True)
            time.sleep(.01)

        navigateFail = random.choice(navigateFailProbability)
        if navigateFail == "true":
            userInput = str(input("Type the directory: "))
            if userInput == directory:

                if directory == "cd /home/user/Documents" or "cd /home/user/Downloads" or "cd /home/user/.local":
                    issueDir = "/home/user"

                if directory == "cd /home/user/.local/share":
                    issueDir = "/home/user/.local"

                if directory == "cd /mnt/executor":
                    issueDir = "/mnt"

                if directory == "cd /tmp":
                    issueDir = "/"

                if directory == "cd /var/tmp":
                    issueDir = "/var"
                
                failedMessage1 = "You ran into an issue when navigating to the directory!\n"
                failedMessage2 = f"The issue is in: '{issueDir}'\n"

                for letter in failedMessage1:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                for letter in failedMessage2:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                navigateFailLine1 = "1. Attempt to kill the program\n"
                navigateFailLine2 = "2. Attempt to delete the program\n"

                for letter in navigateFailLine1:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                for letter in navigateFailLine2:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                userInput1 = str(input("Enter your choice (1/2): "))

                if userInput1 == "1":
                    random.choice(attackOptionsKill)()
                    printHealths()
                    print()
                    userWantContinue()

                if userInput1 == "2":
                    random.choice(attackOptionsDelete)()
                    printHealths()
                    print()
                    userWantContinue()

                else:
                    print("INVALID INPUT!")
                    sys.exit()

        if navigateFail == "false":
        
            userInput = str(input("Type the directory: "))

            if userInput == directory:
                navigateSuccessLine1 ="You have made it to the directory! You have two options to attack:\n"
                navigateSuccessLine2 = "1. Attempt to kill the program\n"
                navigateSuccessLine3 = "2. Attempt to delete the program\n"

                for letter in navigateSuccessLine1:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                for letter in navigateSuccessLine2:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                for letter in navigateSuccessLine3:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                userInput = str(input("Enter your choice (1/2): "))
                if userInput == "1":
                    random.choice(attackOptionsKill)()
                    printHealths()
                    print()
                    userWantContinue()

                if userInput == "2":
                    random.choice(attackOptionsDelete)()
                    printHealths()
                    print()
                    userWantContinue()

                else:
                    print("INVALID INPUT!")
                    sys.exit()

            else:
                navigateFailLine1 = "You entered the directory wrong!"
                systemHealth -= incorrectDirectoryDamage
                wrongDirectoryLine1 = f"You lost {incorrectDirectoryDamage} HP!\n"

                for letter in navigateFailLine1:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                for letter in wrongDirectoryLine1:
                    print(letter, end='', flush=True)
                    time.sleep(.01)

                printHealths()
                print()
                userWantContinue()

    ### If the main game loop hasn't already been initialized, initialize it.
    if atTheStart == True:
        playerTurn()
        atTheStart = False

    ### End the game and display a game over message if the system health is less than or equal to zero
    if systemHealth <= 0:
        lostLine1 = "You lost. Game over."

        for letter in lostLine1:
            print(letter, end='', flush=True)
            time.sleep(.01)