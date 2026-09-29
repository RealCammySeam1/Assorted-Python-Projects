import tkinter as tk
import time
import sys
from decimal import *

sys.set_int_max_str_digits(0)
getcontext().prec = 100000000000000000

root = tk.Tk()

### Variables
num = 1000
divide = 2
upgrade1Cost = 10
upgrade2Cost = 1000
perSecond = 0
refreshNumber = 0

updatingAll = False
upgrade2Attained = False

### Show score and last action
scoreLabel = tk.Label(text = f"Score: {num}")
actionLabel = tk.Label(text = f"No current action")

def add():
	global num
	global divide
	global updatingAll
	num /= divide
	print(num)
	if updatingAll == False:
		updatingAll = True
		updateAll()

def upgrade1():
	#updateAll()
	global divide
	global num
	global upgrade1Cost
	if num <= upgrade1Cost:
		num += upgrade1Cost
		divide += 1
		upgrade1Cost *= 2
		actionLabel.config(text = f"Bought!")
	elif num < upgrade1Cost:
		actionLabel.config(text = f"Not enough points!")

def upgrade2():
	#updateAll()
	global divide
	global num
	global upgrade2Cost
	global upgrade2TF
	global perSecond
	if num >= upgrade2Cost:
		num -= upgrade2Cost
		if upgrade2Attained == False:
			upgrade2TF()
		perSecond += 25
		upgrade2Cost *= 2
		actionLabel.config(text = f"Bought!")
	elif num < upgrade2Cost:
		actionLabel.config(text = f"Not enough points!")

def upgrade2TF():
	global num
	global perSecond
	global upgrade2TF
	global upgrade2Attained
	upgrade2Attained = True
	num += perSecond / 1
	root.after(1000, upgrade2TF)

def updateAll():
	global num
	global increase
	global upgrade1Cost
	global upgrade2Cost
	global updatingAll
	global refreshNumber
	#refreshNumber += 1
	#print(refreshNumber)
	updatingAll = True
	scoreLabel.config(text = f"Score: {num:.100f}")
	button.config(text = f"DIVIDE (current: /{divide})")
	button1.config(text = f"Upgrade 1 (cost: {upgrade1Cost})")
	button2.config(text = f"Upgrade 2 (cost: {upgrade2Cost})")
	root.after(10, updateAll)

button = tk.Button(
	text = f"DIVIDE (current: /{divide})",
	width = 25,
	height = 1,
	command = add
)

button1 = tk.Button(
    text = f"Upgrade 1 (cost: {upgrade1Cost})",
    width = 25, 
    height = 1,
    command = upgrade1
)

button2 = tk.Button(
    text = f"Upgrade 2 (cost: {upgrade2Cost})",
    width = 25,
    height = 1,
    command = upgrade2
)

scoreLabel.pack()
actionLabel.pack()
button.pack(pady=5)
button1.pack(pady=5)
button2.pack(pady=5)
root.geometry("250x500")
root.mainloop()