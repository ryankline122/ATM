import ATM
import getpass
import sqlite3
import sys

# Runs command-line application. Provides user with commands to navigate the application
def main():
    commands = ["login", "new", "help", "show-balance",
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
                    pswrd = input("Create a secure password: ")
                    confirmPassword = input("Confirm password: ")

                bal = float(input("Set initial deposit: $"))
                ATM.createAccount(name,userID,pswrd,bal,False)


        # LOGIN
        elif (action.lower() == "login"):
            success = False

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
                    success = True


                    ATM.login(nameInput, passInput)
                    print("Login Successful")
                else:
                    print("Incorrect username or password")

        # SHOW-BALANCE
        elif (action.lower() == "show-balance"):
            # TODO: Catch error if no user is logged in
            print("Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))


        # DEPOSIT
        elif (action.lower() == "deposit"):
            # TODO: Catch error if no user is logged in
            amount = float(input("How much would you like to deposit? $"))
            ATM.currUser.deposit(amount)
            print("New Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
            ATM.updateBalance()


        # WITHDRAW
        # TODO: Don't let user take out more than is present in their account
        elif (action.lower() == "withdraw"):
            #TODO: Catch error if no user is logged in
            amount = float(input("How much would you like to withdraw? $"))
            ATM.currUser.withdraw(amount)
            print("New Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
            ATM.updateBalance()


        # TRANSFER
        # TODO: Don't allow user to use transfer() on themselves
        elif (action.lower() == "transfer"):
            # TODO: Catch error if no user is logged in
            amount = float(input("How much would you like to transfer? $"))
            recipient = input("Enter the recipients' userID: ")
            ATM.currUser.transfer(amount, recipient)
            print("New Balance: " + ("${:,.2f}".format(ATM.currUser.balance)))
            ATM.updateBalance()

        # PRINT DATA
        elif (action.lower() == "data"):
            ATM.printData()


        # HELP
        elif (action.lower() == "help"):
            for i in commands:
                print(i)


        # LOGOUT
        elif (action.lower() == "logout"):
            ATM.logout()
            print("Goodbye" + ATM.currUser.name)


        # EXIT
        elif (action.lower() == "exit"):
            if(ATM.inUse()):
                ATM.logout()
                print("Goodbye")
                sys.exit()
        else:
            print("Invalid command")

# ATM Boot-up
print("Welcome to our ATM!")
main()