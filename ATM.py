from User import User
import sys

def createAccount():
    # Writes user account info to text file
    name = input("Enter your name: ")
    userID = input("Create a unique userID: ")
    password = input("Create a secure password: ")
    balance = float(input("Set initial deposit: $"))
    file = open("user_info", "a")
    file.write("\n" + name + "," + userID + "," + password + "," + str(balance))


def login():
    # Reads in user_info text file. Logs user in if userID and password inputs match
    success = False
    file = open("user_info", "r")
    nameInput = input("Enter your username: ")
    passInput = input("Enter your password: ")
    # Loops through data for a given user in the text file. Separates items with comma
    for i in file:
        name, userID, password, balance = i.split(",")
        try:
            if (nameInput == userID and passInput == password):
                success = True
                break
        except AttributeError:
            print("No matches for " + nameInput + " enter 'new' to create new account")
    file.close()

    if (success):
        print("Login Successful")
    else:
        print("Incorrect UsrID or password")


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
            showBalance()

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


