from User import User
import sqlite3
import sys

# Temporary User
global currUser


# Writes user account info to text file
def createAccount():
    name = input("Enter your name: ")
    userID = input("Create a unique userID: ")
    password = input("Create a secure password: ")
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
    c.execute("INSERT INTO users VALUES(?,?,?,?,?)",(usr.name, usr.userID, usr.password, usr.balance, usr.loginStatus))
    db.commit()
    c.close()
    db.close()


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
    else:
        print("Incorrect UsrID or password")

    #print data

    c.close()
    db.close()

# Update user_info doc to ensure accurate balance on next login
def logout():
    return 0


def printData():
    db = sqlite3.connect("user_info.db")
    c = db.cursor()
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.close()
    db.close()


# Runs command-line application. Provides user with commands to navigate the application
def main():
    commands = ["login", "new", "help", "show-balance", "deposit", "withdraw", "transfer", "data", "exit"]
    action = ""
    while(action != "exit"):
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

        elif (action.lower() == "withdraw"):
            amount = float(input("How much would you like to withdraw? $"))
            currUser.withdraw(amount)
            print("New Balance: $" + str(currUser.balance))

        elif (action.lower() == "transfer"):
            amount = float(input("How much would you like to transfer? $"))
            recipient = float(input("Enter the recipients' userID: "))
            currUser.withdraw(amount)
            print("New Balance: $" + str(currUser.balance))

        elif(action.lower() == "data"):
            printData()

        elif(action.lower() == "help"):
            for i in commands:
                print(i)

        elif(action.lower() == "exit"):
            sys.exit()
        else:
            print("Invalid command")

# ATM Boot-up
print("Welcome to our ATM!")
main()