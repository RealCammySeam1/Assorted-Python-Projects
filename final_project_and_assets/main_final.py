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

### Set colours to be used later
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET= '\033[0m'

### Create a function to simplify the printing of enemy and player health
def printHealths():
    print()
    printSystemHealth = f"{GREEN}System health: {systemHealth}/1000{RESET}\n"
    printEnemyHealth = f"{RED}Enemy health : {enemyHealth}/500{RESET}\n"

    for letter in printSystemHealth:
        print(letter, end='', flush=True)
        time.sleep(.01)

    for letter in printEnemyHealth:
        print(letter, end='', flush=True)
        time.sleep(.01)

### Make the introduction art a function for simplicity (made with artificial intelligence)
def introArt():
    print(RED)
    print("████████╗██╗  ██╗███████╗    ███████╗ ██████╗  █████╗ ███╗   ██╗██████╗")
    print("╚══██╔══╝██║  ██║██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗████╗  ██║██╔══██╗")
    print("   ██║   ███████║█████╗      ██║  ███╗██████╔╝███████║██╔██╗ ██║██║  ██║")
    print("   ██║   ██╔══██║██╔══╝      ██║   ██║██╔══██╗██╔══██║██║╚██╗██║██║  ██║")
    print("   ██║   ██║  ██║███████╗    ╚██████╔╝██║  ██║██║  ██║██║ ╚████║██████╔╝")
    print("   ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═════╝")
    print("")
    print("  -  ████████╗███████╗██████╗ ███╗   ███╗██╗███╗   ██╗ █████╗ ██╗")
    print("    ╚══██╔══╝██╔════╝██╔══██╗████╗ ████║██║████╗  ██║██╔══██╗██║")
    print("       ██║   █████╗  ██████╔╝██╔████╔██║██║██╔██╗ ██║███████║██║")
    print("       ██║   ██╔══╝  ██╔══██╗██║╚██╔╝██║██║██║╚██╗██║██╔══██║██║")
    print("       ██║   ███████╗██║  ██║██║ ╚═╝ ██║██║██║ ╚████║██║  ██║███████╗")
    print("       ╚═╝   ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝╚══════╝")
    print(RESET)

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
    optionDeleteSucceedLine1 = "{GREEN}You sucessfully removed the malicious program!{RESET}\n"

    for letter in optionDeleteSucceedLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

def optionDeleteFail():
    global systemHealth
    systemHealth -= optionDeleteFailDamage
    optionDeleteFailLine1 = "{RED}The program has already rooted itself in other folders. Delete unsuccessfull.{RESET}\n"

    for letter in optionDeleteFailLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

def optionKillSucceed():
    global enemyHealth
    enemyHealth -= optionKillSucceedDamage
    optionKillSucceedLine1 ="{GREEN}You successfully killed the task, resolving the issue!{RESET}\n"

    for letter in optionKillSucceedLine1:
        print(letter, end='', flush=True)
        time.sleep(.01)

def optionKillFail():
    global systemHealth
    systemHealth -= optionKillFailDamage
    optionKillFailLine1 = "{RED}The virus has set itself to automatically start on boot! Killing the task does not resolve the issue.{RESET}\n"

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

def loading():
    print("|", end='\r')
    time.sleep(0.5)
    print("/", end='\r')
    time.sleep(0.5)
    print("-", end='\r')
    time.sleep(0.5)
    print("\\", end='\r')
    time.sleep(0.5)
    print("|", end='\r')
    time.sleep(0.5)

navigateFailProbability = ["true", "true", "true", "false"]

### Call the intro functions to start the game, so it can be called at any time
introArt()
intro()

while gameRunning == True:

    def playerTurn(): ### Make the majority of the game a function so it can be called easily
        global rollChoice, directory, printHealths, attackOptionsKill, attackOptionsDelete, systemHealth, enemyHealth, navigateFailProbability
        rollChoice() ### Choose a random directory from the list by calling the "rollChoice" function
        playerTurnLine1 = f"There is an issue in '{YELLOW}{directory[3:]}{RESET}' ! Navigate to this folder to battle the enemy!\n" ### Print the directory minus the first three characters, so it only prints the directory name
        playerTurnLine2 = f"Type {YELLOW}'{directory}'{RESET} to navigate there and start the battle!\n"

        for letter in playerTurnLine1:
            print(letter, end='', flush=True)
            time.sleep(.01)

        for letter in playerTurnLine2:
            print(letter, end='', flush=True)
            time.sleep(.01)

        navigateFail = random.choice(navigateFailProbability) ### Choose whether or not the game fails to navigate to the directory

        if navigateFail == "true":

            userInput = str(input("Type the command: "))

            if userInput == directory:

                ### Base the directory where the error occured on which directory the user was trying to navigate to
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

                loading()

                print("ERROR!\n")

                failedMessage1 = "You ran into an issue when navigating to the directory!\n"
                failedMessage2 = f"The issue is in: {YELLOW}'{issueDir}'{RESET}\n"

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

            userInput = str(input("Type the command: "))

            loading()

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
                    print("{RED}INVALID INPUT!{RESET}")
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