from distutils.util import execute
import sqlite3


class User:
    # Constructor
    def __init__(self, name, userID, password, PIN, balance, loginStatus):
        self.name = name
        self.userID = userID
        self.password = password
        self.PIN = PIN
        self.balance = balance
        self.loginStatus = loginStatus

    # Increases balance by specified amount
    def deposit(self, amount):
        self.balance += float(amount)

    # Takes out desired amount
    def withdraw(self, amount):
        # If enough money in account, reduce balance
        self.balance -= float(amount)

    def transfer(self, amount, recipient):
        # If enough money in account, reduce balance
        self.balance -= float(amount)

        # Connect to database, if recipient exists, increase balance by amount
        db = sqlite3.connect('user_info.db')
        c = db.cursor()
        c.execute("SELECT balance FROM users where userID=?", (recipient,))
        balance = c.fetchone()[0]
        balance += amount

        c.execute("UPDATE users SET balance =? WHERE userID =?", (balance, recipient,))
        db.commit()
        c.close()
        db.close()

    # Allows user to change their password
    def changePassword(self):
        currPass = input("Confirm current password: ")
        if (currPass != self.password):
            print("Incorrect password. Try again")
        else:
            newPass = input("Enter your new password: ")
            confirmNewPass = input("Enter new password again to confirm: ")

            if (newPass != confirmNewPass):
                print("New password doesn't match")
            else:
                self.password = newPass
                print("Password set!")


    def getBalance(recipient):
        db = sqlite3.connect('user_info.db')
        c = db.cursor()
        c.execute("SELECT balance FROM users WHERE userID=?", (recipient,))
        balance = c.fetchone()[0]
        return balance
