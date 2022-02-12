#! /usr/bin/env python3

import ATM
import getpass
import sqlite3
import sys

max_balance = 999999999999

# Runs command-line application. Provides user with commands to navigate the application
def main():
    commands = ["login", "new", "help", "balance",
                "deposit", "withdraw", "transfer", "data", "exit"]
    action = ""
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    # Creates user database if needed, adds user info upon successful creation
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                    name text,
                    userID text,
                    password text,
                    balance real,
                    loginStatus text
                )""")

    # RUNS PROGRAM UNTIL USER ENTERS "exit" COMMAND
    while (action != "exit"):
        action = input(
            "Enter a command (Type 'help' for a list of commands): ")


        # CREATE NEW ACCOUNT
        if (action.lower() == "new"):
            name = input("Enter your name: ")
            userID = input("Create a unique userID: ")
            (c.execute("SELECT exists(SELECT userID FROM users where userID=?)", (userID,)))
            [exists] = c.fetchone()

            if (exists):
                print("Username already exists. Try again")
            else:
                # "Run" --> "Edit Configuration" --> Check "Emulate terminal in output console
                pswrd = getpass.getpass("Create your password: ", stream=None)
                confirmPassword = getpass.getpass("Confirm your password: ")

                while (confirmPassword != pswrd):
                    print("Passwords don't match. Try again")
                    pswrd = getpass.getpass("Create your password: ", stream=None)
                    confirmPassword = getpass.getpass("Confirm your password: ")
                try:
                    bal = float(input("Set initial deposit: $"))
                    if(bal < max_balance):
                        ATM.createAccount(name, userID, pswrd, bal, False)
                    else:
                        print("Error - Balance exceeds limit")
                except ValueError:
                    print("Error - Invalid balance input")


        # LOGIN
        elif (action.lower() == "login"):
            if (ATM.inUse()):
                print("Error: In use by another user")
            else:
                nameInput = input("Enter your username: ")
                # "Run" --> "Edit Configuration" --> Check "Emulate terminal in output console
                passInput = getpass.getpass("Enter your password: ", stream=None)
                c.execute("SELECT * FROM users where userID=? AND password=?",
                          (nameInput, passInput))
                row = c.fetchone()
                if row:
                    ATM.login(nameInput, passInput)
                    print("Login Successful")
                else:
                    print("Incorrect username or password")


        # SHOW-BALANCE
        elif (action.lower() == "balance"):
            try:
                print("Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
            except TypeError:
                print("Error - No user logged in")


        # DEPOSIT
        elif (action.lower() == "deposit"):
            if(ATM.inUse()):
                try:
                    amount = float(input("How much would you like to deposit? $"))
                    if(amount > 0 and (ATM.currUser.balance + amount) < max_balance):
                        ATM.currUser.deposit(amount)
                        print("New Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
                        ATM.updateBalance()
                    else:
                        print("Error - Balance either exceeds limit or is invalid input")
                except ValueError:
                    print("Error - Invalid Input")
            else:
                print("Error - No user logged in")


        # WITHDRAW
        elif (action.lower() == "withdraw"):
            if(ATM.inUse()):
                try:
                    amount = float(input("How much would you like to withdraw? $"))
                    if(amount <= ATM.currUser.balance):
                        ATM.currUser.withdraw(amount)
                        print("New Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
                        ATM.updateBalance()
                    else:
                        print("Error - insufficient funds")
                except ValueError:
                    print("Error - Invalid Input")
            else:
                print("Error - No user logged in")


        # TRANSFER
        elif (action.lower() == "transfer"):
            if(ATM.inUse()):
                try:
                    amount = float(input("How much would you like to transfer? $"))
                    if(amount <= ATM.currUser.balance):
                        recipient = input("Enter the recipients' userID: ")
                        if(recipient != ATM.currUser.userID):
                            ATM.currUser.transfer(amount, recipient)
                            print("New Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
                            ATM.updateBalance()
                        else:
                            print("Error - You are attempting to transfer to yourself")
                    else:
                        print("Error - Insufficient funds")
                except ValueError:
                    print("Error - Invalid Input")
            else:
                print("Error - No user logged in")

        # PRINT DATA
        elif (action.lower() == "data"):
            ATM.printData()


        # HELP
        elif (action.lower() == "help"):
            for i in commands:
                print(i)


        # LOGOUT
        elif (action.lower() == "logout"):
            if(ATM.inUse()):
                ATM.logout()
                print("Goodbye " + ATM.currUser.name)
            else:
                print("Error - No user logged in")


        # Logs out of all accounts that are currently logged in.
        # For debugging purposes
        elif (action.lower() == "close"):
            ATM.logoutAll()
            print("Success")


        # EXIT
        elif (action.lower() == "exit"):
            if(ATM.inUse()):
                ATM.logout()
                print("Shutting Down")
                sys.exit()
        else:
            print("Invalid command")


# ATM Boot-up
print("Welcome to our ATM!")
main()