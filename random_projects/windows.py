import tkinter as tk
from tkinter import *
import sys
import time

increase = 1
num = 0

root = tk.Tk()

def addNum():
    global num
    global increase
    num += increase
    print(num)

def increaseSum():
    global num
    global increase
    increase += 1
    num -= 10
    print("Subtracted 10")
    print(num)

main = Tk()
    
button = tk.Button(
    text="+1",
    width=25,
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