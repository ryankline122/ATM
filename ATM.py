import os
import subprocess
from User import User
import sqlite3
import sys


# TODO: Don't create account if username already exists
# User is prompted to enter their name, desired username (if not taken), set their password, and put in an initial deposit
def createAccount():
    name = input("Enter your name: ")
    userID = input("Create a unique userID: ")
    password = input("Create a secure password: ")
    # TODO: format "balance" to fit currency style (e.g $0.00)
    balance = float(input("Set initial deposit: $"))

    # Creates user database if needed, adds user info upon successful creation
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                   name text,
                   userID text,
                   password text,
                   balance real,
                   loginStatus text
                )""")
    usr = User(name, userID, password, balance, "False")
    c.execute("INSERT INTO users VALUES(?,?,?,?,?)", (usr.name, usr.userID, usr.password, usr.balance, usr.loginStatus))
    db.commit()
    c.close()
    db.close()


# createAccount() for use within the GUI script
def createAccount_GUI(name, userID, password, balance):
    # TODO: format "balance" to fit currency style (e.g $0.00)
    balance = float(balance)

    # Creates user database if needed, adds user info upon successful creation
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                   name text,
                   userID text,
                   password text,
                   balance real,
                   loginStatus text
                )""")
    usr = User(name, userID, password, balance, "False")
    c.execute("INSERT INTO users VALUES(?,?,?,?,?)", (usr.name, usr.userID, usr.password, usr.balance, usr.loginStatus))
    db.commit()
    c.close()
    db.close()


# TODO: If there is a user already logged in, don't let user use login() until the other one is logged out
# Reads in user_info database. Logs user in if userID and password inputs match
def login():
    success = False
    nameInput = input("Enter your username: ")
    passInput = input("Enter your password: ")

    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT * FROM users where userID=? AND password=?", (nameInput, passInput))
    row = c.fetchone()
    if row:
        success = True

    if (success):
        print("Login Successful")
        c.execute("UPDATE users SET loginStatus = 'True' WHERE userID =?", (nameInput,))
        db.commit()

        c.execute("SELECT name FROM users where userID=?", (nameInput,))
        name = ','.join(c.fetchone())

        c.execute("SELECT balance FROM users where userID=?", (nameInput,))
        balance = c.fetchone()[0]

        global currUser
        currUser = User(name, nameInput, passInput, balance, "True")
    else:
        print("Incorrect UsrID or password")

    c.close()
    db.close()


# login() for use within the GUI script
def login_GUI(userID_Input, password_Input):
    success = False

    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT * FROM users where userID=? AND password=?", (userID_Input, password_Input))
    row = c.fetchone()
    if row:
        success = True

    if (success):
        print("Login Successful")
        c.execute("UPDATE users SET loginStatus = 'True' WHERE userID =?", (userID_Input,))
        db.commit()

        c.execute("SELECT name FROM users where userID=?", (userID_Input,))
        name = ','.join(c.fetchone())

        c.execute("SELECT balance FROM users where userID=?", (userID_Input,))
        balance = c.fetchone()[0]

        global currUser
        currUser = User(name, userID_Input, password_Input, balance, "True")
    else:
        # Change to be a pop-up alert for GUI
        print("Incorrect UserID or Password.")

    c.close()
    db.close()


# TODO: Check if there is a user currently logged in. If not, send error
# Update user_info doc to ensure accurate balance on next login
def logout():
    currUser.loginStatus = "False"
    updateBalance()

    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("UPDATE users SET loginStatus =? WHERE userID =?", (currUser.loginStatus, currUser.userID,))
    db.commit()
    c.close()
    db.close()

    subprocess.call([sys.executable, os.path.realpath(__file__)] + sys.argv[1:])

# For debugging/testing database
def printData():
    db = sqlite3.connect("user_info.db")
    c = db.cursor()
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.close()
    db.close()


# Updates the balance of the current user in the database
def updateBalance():
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("UPDATE users SET balance =? WHERE userID =?", (currUser.balance, currUser.userID,))
    db.commit()
    c.close()
    db.close()


# TODO: Make a deleteAccount() function



# Runs command-line application. Provides user with commands to navigate the application
def main():
    commands = ["login", "new", "help", "show-balance", "deposit", "withdraw", "transfer", "data", "exit"]
    action = ""
    while (action != "exit"):
        action = input("Enter a command (Type 'help' for a list of commands): ")

        if (action.lower() == "new"):
            createAccount()

        elif (action.lower() == "login"):
            login()

        elif (action.lower() == "show-balance"):
            currUser.showBalance()

        elif (action.lower() == "deposit"):
            amount = float(input("How much would you like to deposit? $"))
            currUser.deposit(amount)
            print("New Balance: $" + str(currUser.balance))
            updateBalance()

        # TODO: Don't let user take out more than is present in their account
        elif (action.lower() == "withdraw"):
            amount = float(input("How much would you like to withdraw? $"))
            currUser.withdraw(amount)
            print("New Balance: $" + str(currUser.balance))
            updateBalance()

        # TODO: Don't allow user to use transfer() on themselves
        elif (action.lower() == "transfer"):
            amount = float(input("How much would you like to transfer? $"))
            recipient = input("Enter the recipients' userID: ")
            currUser.transfer(amount, recipient)
            print("New Balance: $" + str(currUser.balance))
            updateBalance()

        elif (action.lower() == "data"):
            printData()

        elif (action.lower() == "help"):
            for i in commands:
                print(i)

        elif (action.lower() == "logout"):
            logout()

        elif (action.lower() == "exit"):
            #TODO: If user logged in, log them out before exit
            sys.exit()
        else:
            print("Invalid command")


# ATM Boot-up
print("Welcome to our ATM!")
main()