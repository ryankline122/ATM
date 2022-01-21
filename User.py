class User:
    def __init__(self, name, userID, password, balance):
        self.name = name
        self.userID = userID
        self.password = password
        self.balance = balance

    def createAccount(self):
        self.name = input("Enter your name: ")
        self.userID = input("Create a unique userID: ")
        self.password = input("Create a secure password: ")
        self.balance = float(input("Set initial deposit: $"))

