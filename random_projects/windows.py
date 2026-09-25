import tkinter as tk
import sys
num = 1

root = tk.Tk()
def printHello():
    num + 1
    print("hello")
    print(num)

button = tk.Button(
    text="hello",
    width=10,
    height=5,
    command=printHello
)

button.pack()
root.mainloop()