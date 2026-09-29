import tkinter as tk
from tkinter import *
import sys
import time

increase = 1
num = 0
global num
num = 0

root = tk.Tk()

def addNum():
    global num
    global increase
    num += increase
    print(num)

def increaseSum():
    if num >= 10:
        num
        global increase
        increase += 1
        num -= 10
        print("Subtracted 10")
        print(num)
    else:
        print("Not enough points!")

main = Tk()
    
button = tk.Button(
    text="+1",
    width=35,
    height=5,
    command=addNum
).pack()

button = tk.Button(
    text="Double increase per click (cost = 10)",
    width=25,
    height=5,
    command=increaseSum
).pack()

test = True

root.mainloop()