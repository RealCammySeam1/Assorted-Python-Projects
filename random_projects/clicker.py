import tkinter as tk
import time
import sys

root = tk.Tk()

### Variables
num = 10000000
increase = 1
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
	global increase
	global updatingAll
	num += increase
	if updatingAll == False:
		updatingAll = True
		updateAll()

def upgrade1():
	#updateAll()
	global increase
	global num
	global upgrade1Cost
	if num >= upgrade1Cost:
		num -= upgrade1Cost
		increase += 1
		upgrade1Cost *= 1.25
		actionLabel.config(text = f"Bought!")
	elif num < upgrade1Cost:
		actionLabel.config(text = f"Not enough points!")

def upgrade2():
	#updateAll()
	global increase
	global num
	global upgrade2Cost
	global upgrade2TF
	global perSecond
	if num >= upgrade2Cost:
		num -= upgrade2Cost
		if upgrade2Attained == False:
			upgrade2TF()
		perSecond += 25
		upgrade2Cost *= 1.25
		actionLabel.config(text = f"Bought!")
	elif num < upgrade2Cost:
		actionLabel.config(text = f"Not enough points!")

def upgrade2TF(): #Add the number of points per second once per second 
	              #and set upgrade2Attained to "True" to prevent multiple instances of upgrade2TF
	global num
	global perSecond
	global upgrade2TF
	global upgrade2Attained
	upgrade2Attained = True
	num += perSecond
	root.after(1000, upgrade2TF)

def updateAll(): #Refresh all prices and buttons
	global num
	global increase
	global upgrade1Cost
	global upgrade2Cost
	global updatingAll
	global refreshNumber
	#refreshNumber += 1
	#print(refreshNumber)
	updatingAll = True
	scoreLabel.config(text = f"Score: {num:.0f}")
	button.config(text = f"ADD (current: +{increase})")
	button1.config(text = f"Upgrade 1 (cost: {upgrade1Cost:.0f})")
	button2.config(text = f"Upgrade 2 (cost: {upgrade2Cost:.0f})")
	root.after(10, updateAll)

button = tk.Button(
	text = f"ADD (current: +{increase})",
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