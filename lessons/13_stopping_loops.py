gameAlive = True
playerHP = 100

while gameAlive == True:
    if playerHP <= 0:
        gameAlive = False
    if playerHP == 50:
        print("HP hanved!")
    