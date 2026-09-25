### ALL CAPS ONLY FOR CONSTANT VARIABLES
import random

diceRoll = random.randint(1,10)

RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET= '\033[0m'

"""
print(f"{RED}This text is red!{RESET}")
print(f"{GREEN}This text is green!{RESET}")
print(f"Normal text {YELLOW}and yellow text{RESET} mixed together.")
"""

playerIsDead = False
playerHealth = 50
badGuyHealth = 30
playerAttack = 0
badGuyAttack = 0
print(f"You run into a bad guy, {RED}FIGHT!!!{RESET}")

while playerIsDead == False:
    userInput = int(input(f"{RED}1. Fight {RESET}| {GREEN}2. Defend"))
    if userInput == 1:
        playerAttack = random.randint(1, 10)
        badGuyAttack = random.randint(1, 7)
        print(f"{GREEN}You attack for {playerAttack} {RESET}| {RED}Bad guy attacks for {badGuyAttack}")
        playerHealth -= badGuyAttack
        badGuyHealth -= playerAttack
    else:
        playerShield = random.randint(2, 7)
        badGuyAttack = random.randint(1, 7)
        print(f"{GREEN}You block for {playerShield}, {RED}bad guy attacks for {badGuyAttack}{RESET}")
    print(f"{GREEN}You have {playerHealth} HP {RESET}| {RED}Bad guy has {badGuyHealth} HP{RESET}")