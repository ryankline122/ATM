from User import User
import sqlite3

currUser = User(None,None,None,None,None,None)

def createTable():
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    # Creates user database if needed, adds user info upon successful creation
    c.execute("""CREATE TABLE IF NOT EXISTS users(
                      name text,
                      userID text,
                      password text,
                      PIN text,
                      balance real,
                      loginStatus text
                  )""")


# User is prompted to enter their name, desired username (if not taken), set their password, and put in an initial deposit
def createAccount(name, userID, password, PIN, balance, loginStatus):
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    # Checks if user already exists
    usr = User(name, userID, password, PIN, balance, "False")
    c.execute("INSERT INTO users VALUES(?,?,?,?,?,?)",
            (usr.name, usr.userID, usr.password, usr.PIN, usr.balance, usr.loginStatus))
    db.commit()
    c.close()
    db.close()


# Returns True if there is a user currently logged in
def inUse():
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute(
        "SELECT exists(SELECT userID FROM users where loginStatus=?)", ("True",))
    [exists] = c.fetchone()
    if (exists):
        return True
    else:
        return False


# Reads in user_info database. Logs user in if userID and password inputs match
def login(userID, password):
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


# Update user_info doc to ensure accurate balance on next login
def logout():
    currUser.loginStatus = "False"
    updateBalance()

    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("UPDATE users SET loginStatus =? WHERE userID =?",
                (currUser.loginStatus, currUser.userID,))
    db.commit()
    c.close()
    db.close()


# Updates the balance of the current user in the database
def updateBalance():
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("UPDATE users SET balance =? WHERE userID =?",( currUser.balance, currUser.userID,))
    db.commit()
    c.close()
    db.close()


# Allows a user to change their password by using their PIN number
def forgotPassword(userID, PIN, newPassword):
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT PIN FROM users WHERE userID=?", (userID,))
    usrPIN = c.fetchone()[0]

    if(PIN == usrPIN):
        c.execute("UPDATE users SET password=? WHERE userID=?", (newPassword, userID,))
        db.commit()
    else:
        raise ValueError
    c.close()
    db.close()


# Checks if the given userID exists in the database
def userExists(userID):
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute("SELECT userID FROM users")
    (c.execute("SELECT exists(SELECT userID FROM users where userID=?)", (userID,)))
    [exists] = c.fetchone()

    if (exists):
        return True
    else:
        return False




# DEBUGGING

# Prints all user data
def printData():
    db = sqlite3.connect("user_info.db")
    c = db.cursor()
    c.execute("SELECT * FROM users")
    print(c.fetchall())
    c.close()
    db.close()


# For logging out users stuck to "True"
def logoutAll():
    db = sqlite3.connect("user_info.db")
    c = db.cursor()
    c.execute("UPDATE users SET loginStatus =? where loginStatus =?", ("False", "True",))
    db.commit()
    c.close()
    db.close()


# Erases all user data
def deleteAll():
    db = sqlite3.connect('user_info.db')
    c = db.cursor()
    c.execute('DELETE FROM users')
    db.commit()
    c.close()
    db.close()
