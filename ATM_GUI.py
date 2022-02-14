import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ATM

import os

root = tk.Tk()
root.geometry("800x400")


# Functions


# create a new user account
def createAccount():
    myLabel3 = Label(root, text="Testing...")
    myLabel3.place(x=100, y=150)

#transaction log on hold for now
#def transactionLog():
    placeHolderLabel = Label(root, text="Testing", fg='black')
   # newUserLabel.place(x=665, y=360)

#seeMore_btn = ImageTk.PhotoImage(Image.open("pngfind.com-black-button-png-50298_80x40.png"))

#img_label3 = Label(image=seeMore_btn)

def createAccount():
    top_Frame = LabelFrame(root, width=800, height=400)
    top_Frame.pack(fill="both", expand=1)

    canvas = Canvas(top_Frame, width=800, height=400, bg='#75706F')
    canvas.place(x=0, y=0)

    nameLabel = Label(top_Frame, text="What is your name?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    nameLabel.place(x=20, y=20)
    firstName = Entry(root, width=15, fg='black', borderwidth=2)
    firstName.place(x=225, y=35)

    userNameLabel = Label(top_Frame, text="What would you like your username to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    userNameLabel.place(x=20, y=90)
    userName = Entry(root, width=25, fg='black', borderwidth=2)
    userName.place(x=250, y=105)

    passwordLabel = Label(top_Frame, text="What would you like your password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    passwordLabel.place(x=20, y=160)
    password = Entry(root, width=25, fg='black', borderwidth=2)
    password.place(x=250, y=170)

    securityQuestionLabel = Label(top_Frame, text="Security Question: What is your favorite color?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    securityQuestionLabel.place(x=20, y=230)
    secQuestion = Entry(root, width=25, fg='black', borderwidth=2)
    secQuestion.place(x=275, y=245)

    initialDepositLabel = Label(top_Frame, text="What would you like your initial deposit to be?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    initialDepositLabel.place(x=20, y=300)
    deposit = Entry(root, width=25, fg='black', borderwidth=2)
    deposit.place(x=265, y=315)

    doneButton = tk.Button(top_Frame, text="All Done!", padx=17, pady=17, fg="white", bg='#343332')
    doneButton.place(x=600, y=300)



def passwordChange():
    top_Frame = LabelFrame(root, width=800, height=400)
    top_Frame.pack(fill="both", expand=1)

    canvas = Canvas(top_Frame, width=800, height=400, bg='#75706F')
    canvas.place(x=0, y=0)

    forgotPassword = Label(top_Frame, text="Forgot Password?", bg='#75706F', fg='Black', font= "Times 36 bold")
    forgotPassword.place(x=210, y=50)

    userNameLabel = Label(top_Frame, text="What is your username?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    userNameLabel.place(x=250, y=135)
    userName = Entry(root, width=25, fg='black', borderwidth=2)
    userName.place(x=400, y=150)

    securityQuestionLabel = Label(top_Frame, text="What is your favorite color?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    securityQuestionLabel.place(x=235, y=210)
    secQuestion = Entry(root, width=25, fg='black', borderwidth=2)
    secQuestion.place(x=400, y=225)

    passwordLabel = Label(top_Frame, text="What would you like your  new password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
    passwordLabel.place(x=150, y=285)
    password = Entry(root, width=25, fg='black', borderwidth=2)
    password.place(x=400, y=295)

    doneButton = tk.Button(top_Frame, text="All Done!", padx=17, pady=17, fg="white", bg='#343332')
    doneButton.place(x=600, y=300)


def moneyMoves():
    top_Frame = LabelFrame(root, width=800, height=400)
    top_Frame.pack(fill="both", expand=1)

    canvas = Canvas(top_Frame, width=800, height=400, bg='#75706F')
    canvas.place(x=0, y=0)

    moneyTransfer = Label(top_Frame, text="Would you like to deposit or withdraw?",
                          padx=10, pady=10, fg="black", font="Italics 15", bg='#75706F')
    moneyTransfer.place(x=225, y=20)

    moneyInputLabel = Label(top_Frame, text="How much?",
                          padx=10, pady=10, fg="black", font="Italics 15", bg='#75706F')
    moneyInputLabel.place(x=325, y=120)

    moneyInput = Entry(root, width=23, fg='black', borderwidth=2)
    moneyInput.place(x=320, y=175)

    doneButton = tk.Button(top_Frame, text="Submit", padx=17, pady=17, fg="white", bg='#343332')
    doneButton.place(x=600, y=300)

    options = [
        "Deposit",
        "Withdraw"
    ]

    myCombo = ttk.Combobox(top_Frame, value=options)
    myCombo.current(0)
    myCombo.pack(pady=80)

# check if valid username and password and change frame to dashboard
def dashboard():

    success = False
    Username = User.get()
    Passw = Password.get()
    db = sqlite3.connect('user_info.db')
    c = db.cursor()

    c.execute("SELECT * FROM users where userID=? AND password=?",
              (Username, Passw))

    row = c.fetchone()
    if row:
        success = True

    if (success):
      ATM.login(Username, Passw)
      Top_Frame()
      ATM.logout()

    else:
        myLabel4 = Label(root, text="Incorrect username or password", fg='red', font="Times 12 bold")
        myLabel4.place(x=290, y=300)


def Top_Frame():
    top_Frame = LabelFrame(root, width=800, height=400)
    top_Frame.pack(fill="both", expand=1)

    # Define a Canvas Widget
    canvas = Canvas(top_Frame, width=390, height=150)
    canvas.place(x=0, y=0)

    canvas2 = Canvas(top_Frame, width=390, height=150)
    canvas2.place(x=400, y=0)

    canvas3 = Canvas(top_Frame, width=700, height=150)
    canvas3.place(x=50, y=180)

    # Create a rectangle in Canvas
    canvas.create_rectangle(4, 146, 396, 4, outline='gray', width=2, fill='#343332')
    canvas2.create_rectangle(4, 146, 396, 4, outline='gray', width=2, fill='#343332')
    canvas3.create_rectangle(4, 146, 696, 4, outline='gray', width=2, fill='#343332')

    recentLogLabel = Label(top_Frame, text="Recent Transactions", padx=10, pady=10, bg='#343332', fg='gray',
                           font='Times 10 bold')
    recentLogLabel.place(x=335, y=185)

    savingAccountLabel = Label(top_Frame, text="Saving Account", padx=10, pady=10, bg='#343332', fg='gray')
    savingAccountLabel.place(x=5, y=5)

    checkingAccountLabel = Label(top_Frame, text="Checking Account", padx=10, pady=10, bg='#343332', fg='gray')
    checkingAccountLabel.place(x=405, y=5)

    availableBalanceLabel = Label(top_Frame, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
    availableBalanceLabel.place(x=405, y=105)

    availableBalanceLabel = Label(top_Frame, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
    availableBalanceLabel.place(x=5, y=105)

    checkingAccountMoneyLabel = Label(top_Frame, text="$", bg='#343332', fg='gray')
    checkingAccountMoneyLabel.place(x=405, y=85)

    savingAccountMoneyLabel = Label(top_Frame, text="$", bg='#343332', fg='gray')
    savingAccountMoneyLabel.place(x=5, y=85)

    checkingAccountBalanceLabel = Label(top_Frame, text="500.00", bg='#343332', fg='gray', font="Times 18 bold")
    checkingAccountBalanceLabel.place(x=415, y=80)

    savingAccountBalanceLabel = Label(top_Frame, text="500.00", bg='#343332', fg='gray', font="Times 18 bold")
    savingAccountBalanceLabel.place(x=15, y=80)

#update balances,etc...
def update_topFrame():
    Tk.update()


User = Entry(root, width=30, fg='black', borderwidth=2)
User.place(x=300, y=175)

Password = Entry(root, width=30, fg='black', borderwidth=2)
Password.place(x=300, y=205)

newUserLabel = Label(root, text="New User?", fg='black')
newUserLabel.place(x=665, y=360)

# Buttons
welcomeLabel = Label(root, text= "Welcome to the ATM!", font="Italics 36", fg="black")
welcomeLabel.place(x=175, y=50)
login_btn = ImageTk.PhotoImage(Image.open("login-button-png-18030_4_75x50.png"))

img_label = Label(image=login_btn)

register_btn = ImageTk.PhotoImage(Image.open("register-button-png-18477_4_50x40.png"))

img_label2 = Label(image=register_btn)

loginBtn = tk.Button(root, image=login_btn, command=dashboard, borderwidth=0)
loginBtn.place(x=355, y=235)

createAccBtn = tk.Button(root, image=register_btn, command=createAccount, borderwidth=0)
createAccBtn.place(x=725, y=350)

forgotPasswordButton = tk.Button(root, text="Forgot Password?", padx=5, pady=5, fg="white", bg='#343332', command=passwordChange)
forgotPasswordButton.place(x=670,y=310)

forgotPasswordButto = tk.Button(root, text="Deposit/Withdraw Screen", padx=5, pady=5, fg="white", bg='#343332', command=moneyMoves)
forgotPasswordButto.place(x=630,y=270)

root.mainloop()
