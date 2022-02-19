import sqlite3

import ATM


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
        if (amount > 0 and self.balance + amount < ATM.max_balance):
            self.balance += float(amount)
        else:
            raise ValueError("Invalid Balance")

    # Takes out desired amount
    def withdraw(self, amount):
        if (amount > 0 and float(amount) < self.balance):
            self.balance -= float(amount)
        else:
            raise ValueError("Insufficient Funds")

    def transfer(self, amount, recipient):
        self.withdraw(amount)

        if(ATM.userExists(recipient) and amount > 0 and float(amount) < self.balance):
            db = sqlite3.connect('user_info.db')
            c = db.cursor()
            c.execute("SELECT balance FROM users where userID=?", (recipient,))
            balance = c.fetchone()[0]
            balance += float(amount)
            c.execute("UPDATE users SET balance =? WHERE userID =?", (balance, recipient,))
            db.commit()
            c.close()
            db.close()
        else:
            raise Exception("Recipient does not exist or Invalid Balance")


    # Allows user to change their password
    def changePassword(self, newPassword):
        self.password = newPassword
        db = sqlite3.connect('user_info.db')
        c = db.cursor()
        c.execute("UPDATE users SET password =? WHERE userID =?", (newPassword, self.userID,))
        db.commit()
        c.close()
        db.close()

