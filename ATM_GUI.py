import tkinter as tk
from tkinter import  filedialog, Text
import os

root = tk.Tk()

#Functions
def login():
    return 0


def createAccount():
    return 0

canvas = tk.Canvas(root, height=400, width=800, bg='#e6e0d1')
canvas.pack()

# frame = tk.Frame(root, bg="white")
# frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Buttons
loginBtn = tk.Button(root, text="Login", padx=10, pady=5, fg="white", bg="blue")
loginBtn.pack()

createAccBtn = tk.Button(root, text="Create Account", padx=10, pady=5, fg="white", bg="red")
createAccBtn.pack()

root.mainloop()





