import tkinter as tk
from tkinter import  filedialog, Text
import os
from main import ATM


root = tk.Tk()

#Functions


canvas = tk.Canvas(root, height=400, width=800, bg='#e6e0d1')
canvas.pack()

# Buttons
loginBtn = tk.Button(root, text="Login", padx=10, pady=5, fg="white", bg="blue")
loginBtn.pack()

createAccBtn = tk.Button(root, text="Create Account", padx=10, pady=5, fg="white", bg="red")
createAccBtn.pack()

root.mainloop()





