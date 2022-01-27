class User:

    def __init__(self, name, userID, password, balance, loginStatus):
        self.name = name
        self.userID = userID
        self.password = password
        self.balance = balance
        self.loginStatus = loginStatus

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def showBalance(self):
        print("Balance: $" + str(self.balance))

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

