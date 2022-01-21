class User:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.userID = input("Create a unique userID: ")
        self.password = input("Create a secure password: ")
        self.balance = float(input("Set initial deposit: $"))

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        self.balance -= amount

    def changePassword(self):
        currPass = input("Confirm current password: ")

        if(currPass != self.password):
            print("Incorrect password. Try again")
        else:
            newPass = input("Enter your new password: ")
            confirmNewPass = input("Enter new password again to confirm: ")

            if(newPass != confirmNewPass):
                print("New password doesn't match")
            else:
                print("Password set!")