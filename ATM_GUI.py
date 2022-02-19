import sqlite3
import tkinter as tk
from tkinter import *
from tkinter import ttk
import ATM

import os

root = tk.Tk()
root.geometry("800x400")





homePage = Frame(root)
createAccount = Frame(root)
moneyMoves = Frame(root)
passwordChange = Frame(root)
passwordChange2 = Frame(root)
Top_Frame = Frame(root)
Transfer_Frame = Frame(root)

for frame in (homePage, createAccount, passwordChange, passwordChange2, moneyMoves, Top_Frame, Transfer_Frame):
    frame.grid(row=0, column=0, sticky='news')


# Functions

#transaction log on hold for now
#def transactionLog():

# newUserLabel.place(x=665, y=360)

#seeMore_btn = ImageTk.PhotoImage(Image.open("pngfind.com-black-button-png-50298_80x40.png"))

#img_label3 = Label(image=seeMore_btn)


createAccountFrame = LabelFrame(createAccount, width=800, height=400)
createAccountFrame.pack(fill="both", expand=1)

createAccountcanvas = Canvas(createAccountFrame, width=800, height=400, bg='#75706F')
createAccountcanvas.place(x=0, y=0)

nameLabel = Label(createAccountFrame, text="What is your name?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
nameLabel.place(x=20, y=20)
firstName = Entry(createAccountFrame, width=15, fg='black', borderwidth=2)
firstName.place(x=225, y=35)

userNameLabel = Label(createAccountFrame, text="What would you like your username to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
userNameLabel.place(x=20, y=90)
userName1 = Entry(createAccountFrame, width=25, fg='black', borderwidth=2)
userName1.place(x=250, y=105)

passwordLabel = Label(createAccountFrame, text="What would you like your password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel.place(x=20, y=160)
password1 = Entry(createAccountFrame, width=25, fg='black', borderwidth=2)
password1.place(x=250, y=170)

securityPINNLabel = Label(createAccountFrame, text="Add a PIN number of 4 digits.",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityPINNLabel.place(x=20, y=230)
secPIN1 = Entry(createAccountFrame, width=25, fg='black', borderwidth=2)
secPIN1.place(x=275, y=245)

initialDepositLabel = Label(createAccountFrame, text="What would you like your initial deposit to be?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
initialDepositLabel.place(x=20, y=300)
deposit = Entry(createAccountFrame, width=25, fg='black', borderwidth=2)
deposit.place(x=265, y=315)

updateButton = tk.Button(createAccountFrame, text="Add to database!", padx=17, pady=17, fg="white", bg='#343332'
                         , command=lambda:getCreationData())
updateButton.place(x=600, y=225)

backButton2 = tk.Button(createAccountFrame, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(homePage))
backButton2.place(x=635, y=325)



#password change while logged in
passwordChangeLabel = LabelFrame(passwordChange, width=800, height=400)
passwordChangeLabel.pack(fill="both", expand=1)

passwordChangecanvas = Canvas(passwordChangeLabel, width=800, height=400, bg='#75706F')
passwordChangecanvas.place(x=0, y=0)

forgotPassword = Label(passwordChangeLabel, text="Change Password", bg='#75706F', fg='Black', font= "Times 36 bold underline")
forgotPassword.place(x=210, y=50)

currentPass = Label(passwordChangeLabel, text="Confirm your current password?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
currentPass.place(x=200, y=135)
currentPassInput = Entry(passwordChangeLabel, show="*", width=25, fg='black', borderwidth=2)
currentPassInput.place(x=400, y=150)

securityPINLabel = Label(passwordChangeLabel, text="Confirm your PIN number",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityPINLabel.place(x=235, y=210)
secPIN = Entry(passwordChangeLabel, show="*", width=25, fg='black', borderwidth=2)
secPIN.place(x=400, y=225)

passwordLabel = Label(passwordChangeLabel, text="Set new password",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel.place(x=275, y=285)
password2 = Entry(passwordChangeLabel, show="*", width=25, fg='black', borderwidth=2)
password2.place(x=400, y=295)

doneButton = tk.Button(passwordChangeLabel, text="All Done!", padx=17, pady=17, fg="white", bg='#343332',
                       command=lambda:passChangeData())
doneButton.place(x=600, y=300)

backButton3 = tk.Button(passwordChangeLabel, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(Top_Frame)) #CHANGE BACK AFTER DONE TESTING
backButton3.place(x=50, y=300)



#password change used for inside home page
passwordChangeLabel2 = LabelFrame(passwordChange2, width=800, height=400)
passwordChangeLabel2.pack(fill="both", expand=1)

passwordChangecanvas2 = Canvas(passwordChangeLabel2, width=800, height=400, bg='#75706F')
passwordChangecanvas2.place(x=0, y=0)

forgotPassword2 = Label(passwordChangeLabel2, text="Change Password", bg='#75706F', fg='Black', font= "Times 36 bold underline")
forgotPassword2.place(x=210, y=50)

userNameLabel2 = Label(passwordChangeLabel2, text="What is your username?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
userNameLabel2.place(x=250, y=135)
userName3 = Entry(passwordChangeLabel2, width=25, fg='black', borderwidth=2)
userName3.place(x=400, y=150)

securityPINLabel2 = Label(passwordChangeLabel2, text="What is your PIN number?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityPINLabel2.place(x=235, y=210)
secPIN2 = Entry(passwordChangeLabel2, show="*", width=25, fg='black', borderwidth=2)
secPIN2.place(x=400, y=225)

passwordLabel2 = Label(passwordChangeLabel2, text="What would you like your new password to be?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
passwordLabel2.place(x=150, y=285)
password3 = Entry(passwordChangeLabel2, show="*", width=25, fg='black', borderwidth=2)
password3.place(x=400, y=295)

doneButton2 = tk.Button(passwordChangeLabel2, text="All Done!", padx=17, pady=17, fg="white", bg='#343332',
                       command=lambda:forgotPassword())
doneButton2.place(x=600, y=300)

backButton4 = tk.Button(passwordChangeLabel2, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(homePage)) #CHANGE BACK AFTER DONE TESTING
backButton4.place(x=50, y=300)


# check if valid username and password and change frame to dashboard
#Selmir



#Top_Frame Frame Original Selmir
accountFrame = LabelFrame(Top_Frame, width=800, height=400)
accountFrame.pack(fill="both", expand=1)

# Define a Canvas Widget

canvasT4 = Canvas(accountFrame, width=800, height=400, bg='#75706F')
canvasT4.place(x=0, y=0)

#canvasT = Canvas(accountFrame, width=390, height=150, bg='#343332')
#canvasT.place(x=5, y=5)

canvasT2 = Canvas(accountFrame, width=390, height=150, bg='#343332')
canvasT2.place(x=210, y=5)

canvasT3 = Canvas(accountFrame, width=700, height=150, bg='#343332')
canvasT3.place(x=50, y=180)

recentLogLabel = Label(accountFrame, text="Available Features", padx=10, pady=10, bg='#343332', fg='gray',
                           font='Times 10 bold')
recentLogLabel.place(x=335, y=185)

#savingAccountLabel = Label(accountFrame, text="Saving Account", padx=10, pady=10, bg='#343332', fg='gray')
#savingAccountLabel.place(x=15, y=10)

checkingAccountLabel = Label(accountFrame, text="Account Balance", padx=10, pady=10, bg='#343332', fg='gray')
checkingAccountLabel.place(x=220, y=10)

availableBalanceLabel = Label(accountFrame, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  font="Italics 7")
availableBalanceLabel.place(x=215, y=105)

#availableBalanceLabel = Label(accountFrame, text="Available Balance", padx=10, pady=10, bg='#343332', fg='gray',
                                  #font="Italics 7")
#availableBalanceLabel.place(x=20, y=105)

#checkingAccountMoneyLabel = Label(top_FrameOG, text="$", bg='#343332', fg='gray')
#checkingAccountMoneyLabel.place(x=405, y=85)

#savingAccountMoneyLabel = Label(accountFrame, text="$", bg='#343332', fg='gray', font="Times 18 bold")
#savingAccountMoneyLabel.place(x=25, y=80)

display_text = tk.StringVar()

checkingAccountBalanceLabel = Label(accountFrame, textvariable=display_text, bg='#343332', fg='gray', font="Times 18 bold")
checkingAccountBalanceLabel.place(x=225, y=80)

#savingAccountBalanceLabel = Label(accountFrame, text="500.00", bg='#343332', fg='gray', font="Times 18 bold")
#savingAccountBalanceLabel.place(x=38, y=80)

logoutButton = tk.Button(accountFrame, text="Logout", padx=7, pady=7, fg="white", bg='#343332', command=lambda:logout())
logoutButton.place(x=620, y=240)

moneyMovesButton = tk.Button(accountFrame, text="Deposit/Withdraw Screen", padx=7, pady=7, fg="white", bg='#343332', command=lambda:raise_frame(moneyMoves))
moneyMovesButton.place(x=120,y=240)

transferButton = tk.Button(accountFrame, text="Transfer Portal", padx=7, pady=7, fg="white", bg='#343332', command=lambda:raise_frame(Transfer_Frame))
transferButton.place(x=310, y=240)

changePasswordButton = tk.Button(accountFrame, text="Change Password",padx=7, pady=7, fg="white", bg='#343332', command=lambda:raise_frame(passwordChange))
changePasswordButton.place(x=450, y=240)





#moneyMoves Original Logan Reneau updated by selmir
depoWithFrame = LabelFrame(moneyMoves, width=800, height=400)
depoWithFrame.pack(fill="both", expand=1)

canvasM = Canvas(depoWithFrame, width=800, height=400, bg='#75706F')
canvasM.place(x=0, y=0)

moneyTransfer = Label(depoWithFrame, text="Would you like to deposit or withdraw?",
                          padx=10, pady=10, fg="black", font="Italics 15", bg='#75706F')
moneyTransfer.place(x=225, y=20)

moneyInputLabel = Label(depoWithFrame, text="How much?",
                          padx=10, pady=10, fg="black", font="Italics 15", bg='#75706F')
moneyInputLabel.place(x=325, y=120)

moneyInput = Entry(depoWithFrame, width=23, fg='black', borderwidth=2)
moneyInput.place(x=320, y=175)

doneButton2 = tk.Button(depoWithFrame, text="Submit", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:moneymoves())
doneButton2.place(x=600, y=300)

backButton = tk.Button(depoWithFrame, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(Top_Frame))
backButton.place(x=100, y=300)

options = [
    "Deposit",
    "Withdraw"
]

myCombo = ttk.Combobox(depoWithFrame, value=options)
myCombo.current(0)
myCombo.pack(pady=80)


#update balances,etc...
#Selmir



#homePage Frame Original Selmir Lelak, Updated by Logan Reneau
User = Entry(homePage, width=30, fg='black', borderwidth=2)
User.place(x=300, y=175)

Password = Entry(homePage, show="*", width=30, fg='black', borderwidth=2)
Password.place(x=300, y=205)

newUserLabel = Label(homePage, text="New User?", fg='black')
newUserLabel.place(x=660, y=360)

# Buttons
welcomeLabel = Label(homePage, text= "Welcome to the ATM!", font="Italics 36", fg="black")
welcomeLabel.place(x=175, y=50)
#login_btn = ImageTk.PhotoImage(Image.open("login-button-png-18030_4_75x50.png"))

#img_label = Label(image=login_btn)

#register_btn = ImageTk.PhotoImage(Image.open("register-button-png-18477_4_50x40.png"))

#img_label2 = Label(image=register_btn)

loginBtn = tk.Button(homePage, text="Login", padx=25, pady=5, fg="white", bg='#343332', command=lambda:dashboard(),
                    borderwidth=0)
loginBtn.place(x=350, y=235)

createAccBtn = tk.Button(homePage, text="Register", padx=5, pady=5, fg="white", bg='#343332', command=lambda:raise_frame(createAccount), borderwidth=0)
createAccBtn.place(x=725, y=350)

forgotPasswordButton = tk.Button(homePage, text="Forgot Password?", padx=5, pady=5, fg="white", bg='#343332', command=lambda:raise_frame(passwordChange2))
forgotPasswordButton.place(x=670,y=305)

#transfer
TransferCanvas = LabelFrame(Transfer_Frame, width=800, height=400)
TransferCanvas.pack(fill="both", expand=1)

greyTransferCanvas = Canvas(TransferCanvas, width=800, height=400, bg='#75706F')
greyTransferCanvas.place(x=0, y=0)

transferLabel = Label(TransferCanvas, text="Transfer Portal", bg='#75706F', fg='Black', font= "Times 36 bold underline")
transferLabel.place(x=210, y=50)

userNameTransferLabel = Label(TransferCanvas, text="What userID to send to?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
userNameTransferLabel.place(x=250, y=135)
userNameTransferEntry = Entry(TransferCanvas, width=25, fg='black', borderwidth=2)
userNameTransferEntry.place(x=400, y=150)

securityPINTransferLabel = Label(TransferCanvas, text="What is your PIN number?",
                                  padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
securityPINTransferLabel.place(x=235, y=210)
secPINTransfer = Entry(TransferCanvas, show="*", width=25, fg='black', borderwidth=2)
secPINTransfer.place(x=400, y=225)

transferAmountLabel = Label(TransferCanvas, text="How much would you like to send?",
                          padx=15, pady=15, bg='#343332', fg='white', font="Italics 7")
transferAmountLabel.place(x=180, y=285)
transferAmountEntry = Entry(TransferCanvas, width=25, fg='black', borderwidth=2)
transferAmountEntry.place(x=400, y=295)

doneButtonTransfer = tk.Button(TransferCanvas, text="All Done!", padx=17, pady=17, fg="white", bg='#343332',
                       command=lambda:transfer())
doneButtonTransfer.place(x=600, y=300)

backButton3 = tk.Button(TransferCanvas, text="Back", padx=17, pady=17, fg="white", bg='#343332',
                        command=lambda:raise_frame(Top_Frame))
backButton3.place(x=50, y=300)

def transfer():
    if ATM.currUser.loginStatus:
        recipient = userNameTransferEntry.get()
        currPin = secPINTransfer.get()
        amount = transferAmountEntry.get()
        pinCheck = ATM.currUser.PIN
        if ATM.userExists(recipient):
            if pinCheck == currPin:
                ATM.currUser.withdraw(amount)
                ATM.updateBalance()
                ATM.currUser.transfer(amount, recipient)
                display_text.set("${:,.2f}".format(ATM.currUser.balance))
                raise_frame(Top_Frame)
            else:
                wrongPinLabel = Label(TransferCanvas, text="Incorrect PIN", fg='red', font="Times 12 bold")
                wrongPinLabel.place(x=290, y=300)
        else:
            wrongUserIDLabel = Label(TransferCanvas, text="Error: userID DNE", fg='red', font="Times 12 bold")
            wrongUserIDLabel.place(x=290, y=200)
    userNameTransferEntry.delete(0, END)
    secPINTransfer.delete(0, END)
    transferAmountEntry.delete(0, END)






def getCreationData():

    nameEntry = firstName.get()
    userNameEntry = userName1.get()
    pinNum = secPIN1.get()
    passEntry = password1.get()
    depositEntry = deposit.get()

    ATM.createAccount(nameEntry, userNameEntry, passEntry, pinNum, depositEntry, False)

    firstName.delete(0,END)
    userName1.delete(0,END)
    secPIN1.delete(0,END)
    password1.delete(0,END)
    deposit.delete(0,END)

    raise_frame(homePage)


#passChange Frame Logan Reneau
def passChangeData():
    pinNumIn = secPIN.get()
    newPass = password2.get()

    if ATM.currUser.PIN == pinNumIn and ATM.currUser.password == currentPassInput.get():
        ATM.currUser.changePassword(newPass)
        raise_frame(Top_Frame)
    else:
        errorLabelPass = Label(passwordChangeLabel, text="Error: Incorrect userID or PIN", fg='Black',
                               font='Italics 12')
        errorLabelPass.place(x=575, y=200)
    currentPassInput.delete(0, END)
    secPIN.delete(0, END)
    password2.delete(0, END)


#Home screen forgot password button
def forgotPassword():
    userNameData = userName3.get()
    pinNumIn = secPIN2.get()
    newPass = password3.get()
    errorLabelPass = Label(passwordChangeLabel, text="Error: Incorrect userID or PIN", fg='Black',
                           font='Italics 12')

    if(ATM.userExists(userNameData)):
        try:
            ATM.forgotPassword(userNameData, pinNumIn, newPass)
        except:
            ValueError(errorLabelPass.place(x=575, y=200))
        raise_frame(homePage)

    userName3.delete(0, END)
    secPIN2.delete(0, END)
    password3.delete(0, END)



 #Original Logan updated by selmir
def moneymoves():
    if ATM.currUser.loginStatus:
        money = moneyInput.get()
        if myCombo.get() == "Deposit":
            ATM.currUser.deposit(money)
            ATM.updateBalance()
            display_text.set("${:,.2f}".format(ATM.currUser.balance))
            raise_frame(Top_Frame)
        else:
            ATM.currUser.withdraw(money)
            ATM.updateBalance()
            display_text.set("${:,.2f}".format(ATM.currUser.balance))
            raise_frame(Top_Frame)
    moneyInput.delete(0, END)


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
        User.delete(0, END)
        Password.delete(0, END)
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
