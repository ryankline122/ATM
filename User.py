class User:
    # Constructor
    def __init__(self, name, userID, password, balance, loginStatus):
        self.name = name
        self.userID = userID
        self.password = password
        self.balance = balance
        self.loginStatus = loginStatus


    # Increases balance by specified amount
    def deposit(self, amount):
        self.balance += float(amount)

    # Takes out desired amount
    def withdraw(self, amount):
        self.balance -= float(amount)

    # Prints the users current balance
    def showBalance(self):
        print("Balance: $" + str(self.balance))

    #Allows user to change their password
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

    # For writing a User Object to a string
    def __toStr___(self):
        return (self.name + "," +self.userID+ "," +self.password+ "," +str(self.balance)+ "," +str(self.loginStatus))


    # Getter/Setter

    # @property
    # def userID(self):
    #     return '{}'.format(self.userID)
    #
    # @property
    # def password(self):
    #     return '{}'.format(self.password)
    #
    # @property
    # def balance(self):
    #     return '{}'.format(self.balance)
    #
    # @password.setter
    # def password(self, value):
    #     self._password = value
    #
    # @userID.setter
    # def userID(self, value):
    #     self._userID = value
    #
    # @balance.setter
    # def balance(self, value):
    #     self._balance = value

