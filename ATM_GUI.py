import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ATM

import os

root = tk.Tk()
root.geometry("800x400")

def raise_frame(frame):
    frame.tkraise()


homePage = Frame(root)
createAccount = Frame(root)
moneyMoves = Frame(root)
passwordChange = Frame(root)
Top_Frame = Frame(root)

for frame in (homePage, createAccount, passwordChange, moneyMoves, Top_Frame):
    frame.grid(row=0, column=0, sticky='news')


# Functions

#transaction log on hold for now
#def transactionLog():

# newUserLabel.place(x=665, y=360)

#seeMore_btn = ImageTk.PhotoImage(Image.open("pngfind.com-black-button-png-50298_80x40.png"))

#img_label3 = Label(image=seeMore_btn)

#createAcount Frame Logan Renaau
top_Frame = LabelFrame(createAccount, width=800, height=400)
top_Frame.pack(fill="both", expand=1)

canvas = Canvas(top_Frame, width=800, height=400, bg='#75706F')
canvas.place(x=0, y=0)

nameLabel = Label(top_Frame, text="What is your name?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
nameLabel.place(x=20, y=20)
firstName = Entry(top_Frame, width=15, fg='black', borderwidth=2)
firstName.place(x=225, y=35)

userNameLabel = Label(top_Frame, text="What would you like your username to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
userNameLabel.place(x=20, y=90)
userName = Entry(top_Frame, width=25, fg='black', borderwidth=2)
userName.place(x=250, y=105)

passwordLabel = Label(top_Frame, text="What would you like your password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel.place(x=20, y=160)
password = Entry(top_Frame, width=25, fg='black', borderwidth=2)
password.place(x=250, y=170)

securityQuestionLabel = Label(top_Frame, text="Security Question: What is your favorite color?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityQuestionLabel.place(x=20, y=230)
secQuestion = Entry(top_Frame, width=25, fg='black', borderwidth=2)
secQuestion.place(x=275, y=245)

initialDepositLabel = Label(top_Frame, text="What would you like your initial deposit to be?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
initialDepositLabel.place(x=20, y=300)
deposit = Entry(root, width=25, fg='black', borderwidth=2)
deposit.place(x=265, y=315)

doneButton = tk.Button(top_Frame, text="All Done!", padx=17, pady=17, fg="white", bg='#343332',
                       command=lambda:raise_frame(Top_Frame))
doneButton.place(x=600, y=300)



#passChange Frame Logan Reneau
top_Frame2 = LabelFrame(passwordChange, width=800, height=400)
top_Frame2.pack(fill="both", expand=1)

canvas = Canvas(top_Frame2, width=800, height=400, bg='#75706F')
canvas.place(x=0, y=0)

forgotPassword = Label(top_Frame2, text="Forgot Password?", bg='#75706F', fg='Black', font= "Times 36 bold")
forgotPassword.place(x=210, y=50)

userNameLabel = Label(top_Frame2, text="What is your username?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
userNameLabel.place(x=250, y=135)
userName = Entry(top_Frame2, width=25, fg='black', borderwidth=2)
userName.place(x=400, y=150)

securityQuestionLabel = Label(top_Frame2, text="What is your favorite color?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityQuestionLabel.place(x=235, y=210)
secQuestion = Entry(top_Frame2, width=25, fg='black', borderwidth=2)
secQuestion.place(x=400, y=225)

passwordLabel = Label(top_Frame2, text="What would you like your  new password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel.place(x=150, y=285)
password = Entry(top_Frame2, width=25, fg='black', borderwidth=2)
password.place(x=400, y=295)

doneButton = tk.Button(top_Frame2, text="All Done!", padx=17, pady=17, fg="white", bg='#343332',
                       command=lambda:raise_frame(Top_Frame))
doneButton.place(x=600, y=300)


#moneyMoves Frame Logan Reneau
top_Frame3 = LabelFrame(moneyMoves, width=800, height=400)
top_Frame3.pack(fill="both", expand=1)

canvasM = Canvas(top_Frame3, width=800, height=400, bg='#75706F')
canvasM.place(x=0, y=0)

moneyTransfer = Label(top_Frame3, text="Would you like to deposit or withdraw?",
                          padx=10, pady=10, fg="black", font="Italics 15", bg='#75706F')
moneyTransfer.place(x=225, y=20)

moneyInputLabel = Label(top_Frame3, text="How much?",
                          padx=10, pady=10, fg="black", font="Italics 15", bg='#75706F')
moneyInputLabel.place(x=325, y=120)

moneyInput = Entry(top_Frame3, width=23, fg='black', borderwidth=2)
moneyInput.place(x=320, y=175)

doneButton2 = tk.Button(top_Frame3, text="Submit", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(Top_Frame))
doneButton2.place(x=600, y=300)

options = [
    "Deposit",
    "Withdraw"
]

myCombo = ttk.Combobox(top_Frame3, value=options)
myCombo.current(0)
myCombo.pack(pady=80)

# check if valid username and password and change frame to dashboard
#Selmir
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


#Top_Frame Frame Orignial Selmir
top_FrameOG = LabelFrame(Top_Frame, width=800, height=400)
top_FrameOG.pack(fill="both", expand=1)

# Define a Canvas Widget
canvasT = Canvas(top_FrameOG, width=390, height=150)
canvasT.place(x=0, y=0)

canvasT2 = Canvas(top_FrameOG, width=390, height=150)
canvasT2.place(x=400, y=0)

canvasT3 = Canvas(top_FrameOG, width=700, height=150)
canvasT3.place(x=50, y=180)

    # Create a rectangle in Canvas
canvasT.create_rectangle(4, 146, 396, 4, outline='gray', width=2, fill='#343332')
canvasT2.create_rectangle(4, 146, 396, 4, outline='gray', width=2, fill='#343332')
canvasT3.create_rectangle(4, 146, 696, 4, outline='gray', width=2, fill='#343332')

recentLogLabel = Label(top_FrameOG, text="Recent Transactions", padx=10, pady=10, bg='#343332', fg='gray',
                           font='Times 10 bold')
recentLogLabel.place(x=335, y=185)

savingAccountLabel = Label(top_FrameOG, text="Saving Account", padx=10, pady=10, bg='#343332', fg='gray')
savingAccountLabel.place(x=5, y=5)

checkingAccountLabel = Label(top_FrameOG, text="Checking Account", padx=10, pady=10, bg='#343332', fg='gray')
checkingAccountLabel.place(x=405, y=5)

availableBalanceLabel = Label(top_FrameOG, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
availableBalanceLabel.place(x=405, y=105)

availableBalanceLabel = Label(top_FrameOG, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
availableBalanceLabel.place(x=5, y=105)

checkingAccountMoneyLabel = Label(top_FrameOG, text="$", bg='#343332', fg='gray')
checkingAccountMoneyLabel.place(x=405, y=85)

savingAccountMoneyLabel = Label(top_FrameOG, text="$", bg='#343332', fg='gray')
savingAccountMoneyLabel.place(x=5, y=85)

checkingAccountBalanceLabel = Label(top_FrameOG, text="500.00", bg='#343332', fg='gray', font="Times 18 bold")
checkingAccountBalanceLabel.place(x=415, y=80)

savingAccountBalanceLabel = Label(top_FrameOG, text="500.00", bg='#343332', fg='gray', font="Times 18 bold")
savingAccountBalanceLabel.place(x=15, y=80)

#update balances,etc...
#Selmir
def update_topFrame():
    Tk.update()

#homePage Frame Original Ryan K, Updated by Logan Reneau
User = Entry(homePage, width=30, fg='black', borderwidth=2)
User.place(x=300, y=175)

Password = Entry(homePage, width=30, fg='black', borderwidth=2)
Password.place(x=300, y=205)

newUserLabel = Label(homePage, text="New User?", fg='black')
newUserLabel.place(x=665, y=360)

# Buttons
welcomeLabel = Label(homePage, text= "Welcome to the ATM!", font="Italics 36", fg="black")
welcomeLabel.place(x=175, y=50)
login_btn = ImageTk.PhotoImage(Image.open("login-button-png-18030_4_75x50.png"))

img_label = Label(image=login_btn)

register_btn = ImageTk.PhotoImage(Image.open("register-button-png-18477_4_50x40.png"))

img_label2 = Label(image=register_btn)

loginBtn = tk.Button(homePage, image=login_btn, command=dashboard, borderwidth=0)
loginBtn.place(x=355, y=235)

createAccBtn = tk.Button(homePage, image=register_btn, command=lambda:raise_frame(createAccount), borderwidth=0)
createAccBtn.place(x=725, y=350)

forgotPasswordButton = tk.Button(homePage, text="Forgot Password?", padx=5, pady=5, fg="white", bg='#343332', command=lambda:raise_frame(passwordChange))
forgotPasswordButton.place(x=670,y=310)

forgotPasswordButto = tk.Button(homePage, text="Deposit/Withdraw Screen", padx=5, pady=5, fg="white", bg='#343332', command=lambda:raise_frame(moneyMoves))
forgotPasswordButto.place(x=630,y=270)


raise_frame(homePage)
root.mainloop()