import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
import os

root = tk.Tk()
root.geometry("800x400")




# Functions


#create a new user account
def createAccount():
        myLabel3 = Label(root, text="Testing...")
        myLabel3.place(x=100, y=150)


#check if valid username and password
def checkCredentials():

    myLabel = Label(root, text=User.get())
    myLabel.place(x=400, y=355)

    myLabel2 = Label(root, text=Password.get())
    myLabel2.place(x=400, y=375)

    # if valid call dashboard function
    dashboard()

# call new frame to display account information
def dashboard():
    dashboardFrame = Frame(root)



User = Entry(root, width=30, fg='black', borderwidth=2)
User.place(x=300, y=175)

Password = Entry(root, width=30, fg='black', borderwidth=2)
Password.place(x=300, y=205)

newUserLabel = Label(root, text ="New User?", fg='black')
newUserLabel.place(x=665, y=360)

# Buttons
login_btn = ImageTk.PhotoImage(Image.open("login-button-png-18030_4_75x50.png"))

img_label = Label(image=login_btn)


register_btn = ImageTk.PhotoImage(Image.open("register-button-png-18477_4_50x40.png"))

img_label2 = Label(image=register_btn)

loginBtn = tk.Button(root, image=login_btn, command=checkCredentials, borderwidth=0)
loginBtn.place(x=365, y=235)

createAccBtn = tk.Button(root, image=register_btn, command=createAccount, borderwidth=0)
createAccBtn.place(x=725, y=350)

root.mainloop()
