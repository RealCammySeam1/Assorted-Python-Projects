import tkinter as tk

root = tk.Tk()

scoreLabel = tk.Label(
    text = f"label"
)

button = tk.Button(
    text = "One more damage per hit "
)

root.title("Shop")
root.geometry("250x250")

scoreLabel.pack()
button.pack()
root.mainloop()