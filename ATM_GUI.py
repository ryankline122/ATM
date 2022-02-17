import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import ATM

import os

root = tk.Tk()
root.geometry("800x400")





homePage = Frame(root)
createAccount = Frame(root)
moneyMoves = Frame(root)
passwordChange = Frame(root)
Top_Frame = Frame(root)
Transfer_Frame = Frame(root)

for frame in (homePage, createAccount, passwordChange, moneyMoves, Top_Frame, Transfer_Frame):
    frame.grid(row=0, column=0, sticky='news')


# Functions

#transaction log on hold for now
#def transactionLog():

# newUserLabel.place(x=665, y=360)

#seeMore_btn = ImageTk.PhotoImage(Image.open("pngfind.com-black-button-png-50298_80x40.png"))

#img_label3 = Label(image=seeMore_btn)


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
userName1 = Entry(top_Frame, width=25, fg='black', borderwidth=2)
userName1.place(x=250, y=105)

passwordLabel = Label(top_Frame, text="What would you like your password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel.place(x=20, y=160)
password1 = Entry(top_Frame, width=25, fg='black', borderwidth=2)
password1.place(x=250, y=170)

securityPINNLabel = Label(top_Frame, text="Add a PIN number of 4 digits.",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityPINNLabel.place(x=20, y=230)
secPIN1 = Entry(top_Frame, width=25, fg='black', borderwidth=2)
secPIN1.place(x=275, y=245)

initialDepositLabel = Label(top_Frame, text="What would you like your initial deposit to be?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
initialDepositLabel.place(x=20, y=300)
deposit = Entry(top_Frame, width=25, fg='black', borderwidth=2)
deposit.place(x=265, y=315)

updateButton = tk.Button(top_Frame, text="Add to database!", padx=17, pady=17, fg="white", bg='#343332'
                         , command=lambda:getCreationData())
updateButton.place(x=600, y=225)

backButton2 = tk.Button(top_Frame, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(homePage))
backButton2.place(x=635, y=325)




top_Frame2 = LabelFrame(passwordChange, width=800, height=400)
top_Frame2.pack(fill="both", expand=1)

canvas = Canvas(top_Frame2, width=800, height=400, bg='#75706F')
canvas.place(x=0, y=0)

forgotPassword = Label(top_Frame2, text="Forgot Password?", bg='#75706F', fg='Black', font= "Times 36 bold")
forgotPassword.place(x=210, y=50)

userNameLabel = Label(top_Frame2, text="What is your username?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
userNameLabel.place(x=250, y=135)
userName2 = Entry(top_Frame2, width=25, fg='black', borderwidth=2)
userName2.place(x=400, y=150)

securityPINLabel = Label(top_Frame2, text="What is your PIN number?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityPINLabel.place(x=235, y=210)
secPIN = Entry(top_Frame2, width=25, fg='black', borderwidth=2)
secPIN.place(x=400, y=225)

passwordLabel = Label(top_Frame2, text="What would you like your  new password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel.place(x=150, y=285)
password2 = Entry(top_Frame2, width=25, fg='black', borderwidth=2)
password2.place(x=400, y=295)

doneButton = tk.Button(top_Frame2, text="All Done!", padx=17, pady=17, fg="white", bg='#343332',
                       command=lambda:passChangeData())
doneButton.place(x=600, y=300)

backButton3 = tk.Button(top_Frame2, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(homePage))
backButton3.place(x=50, y=300)


# check if valid username and password and change frame to dashboard
#Selmir



#Top_Frame Frame Original Selmir
top_FrameOG = LabelFrame(Top_Frame, width=800, height=400)
top_FrameOG.pack(fill="both", expand=1)

# Define a Canvas Widget

canvasT4 = Canvas(top_FrameOG, width=800, height=400, bg='#75706F')
canvasT4.place(x=0, y=0)

canvasT = Canvas(top_FrameOG, width=390, height=150, bg='#343332')
canvasT.place(x=5, y=5)

canvasT2 = Canvas(top_FrameOG, width=390, height=150, bg='#343332')
canvasT2.place(x=395, y=5)

canvasT3 = Canvas(top_FrameOG, width=700, height=150, bg='#343332')
canvasT3.place(x=50, y=180)

recentLogLabel = Label(top_FrameOG, text="Recent Transactions", padx=10, pady=10, bg='#343332', fg='gray',
                           font='Times 10 bold')
recentLogLabel.place(x=335, y=185)

savingAccountLabel = Label(top_FrameOG, text="Saving Account", padx=10, pady=10, bg='#343332', fg='gray')
savingAccountLabel.place(x=15, y=10)

checkingAccountLabel = Label(top_FrameOG, text="Checking Account", padx=10, pady=10, bg='#343332', fg='gray')
checkingAccountLabel.place(x=405, y=10)

availableBalanceLabel = Label(top_FrameOG, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
availableBalanceLabel.place(x=410, y=105)

availableBalanceLabel = Label(top_FrameOG, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
availableBalanceLabel.place(x=20, y=105)

#checkingAccountMoneyLabel = Label(top_FrameOG, text="$", bg='#343332', fg='gray')
#checkingAccountMoneyLabel.place(x=405, y=85)

savingAccountMoneyLabel = Label(top_FrameOG, text="$", bg='#343332', fg='gray', font="Times 18 bold")
savingAccountMoneyLabel.place(x=25, y=80)

display_text = tk.StringVar()

checkingAccountBalanceLabel = Label(top_FrameOG, textvariable=display_text, bg='#343332', fg='gray', font="Times 18 bold")
checkingAccountBalanceLabel.place(x=415, y=80)

savingAccountBalanceLabel = Label(top_FrameOG, text="500.00", bg='#343332', fg='gray', font="Times 18 bold")
savingAccountBalanceLabel.place(x=38, y=80)

logoutButton = tk.Button(top_FrameOG, text="Logout", command=lambda:logout())
logoutButton.place(x=200, y=270)

moneyMovesButton = tk.Button(top_FrameOG, text="Deposit/Withdraw Screen", padx=5, pady=5, fg="white", bg='#343332', command=lambda:raise_frame(moneyMoves))
moneyMovesButton.place(x=570,y=270)





#moneyMoves Original Logan Reneau
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
#moneyInput.get() gets the value within.

doneButton2 = tk.Button(top_Frame3, text="Submit", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:moneymoves())
doneButton2.place(x=600, y=300)

backButton = tk.Button(top_Frame3, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(Top_Frame))
backButton.place(x=100, y=300)

options = [
    "Deposit",
    "Withdraw"
]

myCombo = ttk.Combobox(top_Frame3, value=options)
myCombo.current(0)
myCombo.pack(pady=80)


#update balances,etc...
#Selmir



#homePage Frame Original Selmir Lelak, Updated by Logan Reneau
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

loginBtn = tk.Button(homePage, image=login_btn, command=lambda:dashboard(),
                    borderwidth=0)
loginBtn.place(x=355, y=235)

createAccBtn = tk.Button(homePage, image=register_btn, command=lambda:raise_frame(createAccount), borderwidth=0)
createAccBtn.place(x=725, y=350)

forgotPasswordButton = tk.Button(homePage, text="Forgot Password?", padx=5, pady=5, fg="white", bg='#343332', command=lambda:raise_frame(passwordChange))
forgotPasswordButton.place(x=670,y=310)

#transfer


def getCreationData():

    nameEntry = firstName.get()
    userNameEntry = userName1.get()
    pinNum = secPIN1.get()
    passEntry = password1.get()
    depositEntry = deposit.get()

    ATM.createAccount(nameEntry, userNameEntry, passEntry, depositEntry, pinNum, False)
    raise_frame(homePage)


#passChange Frame Logan Reneau
def passChangeData():
    userNameData = userName2.get()
    pinNumIn = secPIN.get()
    newPass = password2.get()
    currentPIN = ATM.getPIN(userNameData)

    if currentPIN == pinNumIn:
        ATM.updatePassword(newPass, userNameData)
        raise_frame(homePage)
    else:
        errorLabelPass = Label(top_Frame2, text="Error: Incorrect userID or PIN", fg='Black',
                               font='Italics 12')
        errorLabelPass.place(x=575, y=200)
        userName2.delete(0, END)
        secPIN.delete(0, END)
        password2.delete(0, END)



 #Original Logan updated by selmir
def moneymoves():
    if ATM.currUser.loginStatus:
        money = moneyInput.get()
        if myCombo.get() == "Deposit":
            ATM.currUser.deposit(money)
            display_text.set("${:,.2f}".format(ATM.currUser.balance))
            raise_frame(Top_Frame)
        else:
            ATM.currUser.withdraw(money)
            display_text.set("${:,.2f}".format(ATM.currUser.balance))
            raise_frame(Top_Frame)

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
        display_text.set("${:,.2f}".format(ATM.currUser.balance))
        raise_frame(Top_Frame)

    else:
        myLabel4 = Label(root, text="Incorrect username or password", fg='red', font="Times 12 bold")
        myLabel4.place(x=290, y=300)


def logout():
    ATM.logoutAll()
    raise_frame(homePage)


def update_topFrame():
    Tk.update()

def raise_frame(frame):
    frame.tkraise()


raise_frame(homePage)
root.mainloop()
