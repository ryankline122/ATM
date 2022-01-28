from User import User
import sys

# Writes user account info to text file
def createAccount():
    name = input("Enter your name: ")
    userID = input("Create a unique userID: ")
    password = input("Create a secure password: ")
    balance = float(input("Set initial deposit: $"))

    # Update me when writing to database instead of text file
    file = open("user_info", "a")
    usr = User(name, userID, password, balance, False)
    file.write(usr.__toStr___() + "\n")
    file.close()

# Reads in user_info text file. Logs user in if userID and password inputs match
def login():
    success = False
    file = open("user_info", "r")
    nameInput = input("Enter your username: ")
    passInput = input("Enter your password: ")

    for i in file:
        name, userID, password, balance, loginStatus = i.split(",")
        try:
            if (nameInput == userID and passInput == password):
                success = True
                # Creates User object with information given from the file
                global currUser
                currUser = User(name, userID, password, float(balance), loginStatus)
                currUser.loginStatus = True
                break
        except AttributeError:
            print("No matches for " + nameInput + " enter 'new' to create new account")
    file.close()

    if (success):
        print("Login Successful")
    else:
        print("Incorrect UsrID or password")

# Update user_info doc to ensure accurate balance on next login
def logout():
    return 0

# Runs command-line application. Provides user with commands to navigate the application
def main():
    commands = ["login", "new", "help", "show-balance", "deposit", "withdraw", "transfer", "exit"]
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