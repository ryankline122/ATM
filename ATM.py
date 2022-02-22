"""
Module for all backend functionality of the ATM Application.

Functions:
    createTable()\n
    createAccount(string, string, string, string, float, string)\n
    inUse()\n
    login(string, string)\n
    logout()\n
    updateBalance()\n
    forgotPassword(string, string, string)\n
    userExists(string)\n
    printData()\n
    logoutAll()\n
    deleteAll()\n
"""
import sqlite3
from User import User

currUser = User(None, None, None, None, None, None)
MAX_BALANCE = 999999999999


def createTable():
    """
    Creates a SQLite database to store user data if one does not already exist
    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                      name text,
                      userID text,
                      password text,
                      PIN text,
                      balance real,
                      loginStatus text
                  )""")


def createAccount(name, userID, password, PIN, balance):
    """
    Creates a new entry in the database with the given parameters

        :param name: Name of the user
        :type name: str
        :param userID: The userID to be associated with the user
        :type userID: str
        :param password: The password to be associated with the user
        :type password: str
        :param PIN: A 4-digit number to be associated with the user
        :type PIN: int
        :param balance: Represents the users starting balance
        :type balance: float

    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    usr = User(name, userID, password, PIN, balance, "False")
    c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",
              (usr.name, usr.userID, usr.password, usr.PIN, usr.balance, usr.loginStatus))
    db.commit()
    c.close()
    db.close()
    login(userID, password)


def inUse():
    """
    Gives the current use status of the ATM\n
    :return: Boolean
    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute(
        "SELECT exists(SELECT userID FROM users where loginStatus=?)", ("True",))
    [exists] = c.fetchone()
    return exists


def login(userID, password):
    """
    Sets the currUser parameters to the info of the user logging in

    :param userID: The userID of the user logging in
    :type userID: str
    :param password: The password of the user logging in
    :type password: str

    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute(
        "UPDATE users SET loginStatus = 'True' WHERE userID =?", (userID,))
    db.commit()
    c.execute("SELECT name FROM users where userID=?", (userID,))
    name = ','.join(c.fetchone())
    c.execute("SELECT balance FROM users where userID=?", (userID,))
    balance = c.fetchone()[0]
    c.execute("SELECT PIN FROM users where userID=?", (userID,))
    PIN = c.fetchone()[0]

    currUser.name = name
    currUser.userID = userID
    currUser.password = password
    currUser.PIN = PIN
    currUser.balance = balance
    currUser.loginStatus = True

    c.close()
    db.close()


def logout():
    """
    Sets currUser's login status to "False" and calls updateBalance()
    """
    currUser.loginStatus = "False"
    updateBalance()

    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("UPDATE users SET loginStatus =? WHERE userID =?",
              (currUser.loginStatus, currUser.userID,))
    db.commit()
    c.close()
    db.close()


def updateBalance():
    """
     Updates the balance of the current user in the database
    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("UPDATE users SET balance =? WHERE userID =?", (currUser.balance, currUser.userID,))
    db.commit()
    c.close()
    db.close()


def forgotPassword(userID, PIN, newPassword):
    """
    Allows a user to change their password by confirming their PIN number

    :param userID: The userID of the user wanted to change their password
    :type userID: str
    :param PIN: The PIN number associated with the given userID
    :type PIN: str
    :param newPassword: The user's desired new password
    :type newPassword: str
    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT PIN FROM users WHERE userID=?", (userID,))
    usrPIN = c.fetchone()[0]

    if PIN == usrPIN:
        c.execute("UPDATE users SET password=? WHERE userID=?", (newPassword, userID,))
        db.commit()
    else:
        raise ValueError
    c.close()
    db.close()


def userExists(userID):
    """
    Checks if the given userID exists in the database

    :param userID: The userID to search for
    :type userID: str
    :return: Boolean
    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT userID FROM users")
    (c.execute("SELECT exists(SELECT userID FROM users where userID=?)", (userID,)))
    [exists] = c.fetchone()

    return exists


def printData():
    """
    FOR DEBUGGING: Prints all user data to the console
    """
    db = sqlite3.connect("user_info.db")
    c = db.cursor()
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.close()
    db.close()


def logoutAll():
    """
    FOR DEBUGGING: Logs out all users
    """
    db = sqlite3.connect("user_info.db")
    c = db.cursor()
    c.execute("UPDATE users SET loginStatus =? where loginStatus =?", ("False", "True",))
    db.commit()
    c.close()
    db.close()


def deleteAll():
    """
    FOR DEBUGGING: Erases all user data
    """
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute('DELETE FROM users')
    db.commit()
    c.close()
    db.close()
