import sqlite3
import unittest
import ATM

# In the terminal:
# "python -m pytest --cov-report=html --cov=(filename) --cov-branch

class TestAccountCreation(unittest.TestCase):

    def test_newAccount(self):
        ATM.createTable()

        db = sqlite3.connect('user_info.db')
        c = db.cursor()
        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        c.execute("SELECT exists(SELECT userID FROM users where userID=?)", ("jdoe123",))
        [exists] = c.fetchone()
        if(exists):
            success = True
        else:
            success = False
        self.assertEqual(True, success)

        ATM.deleteAll()

    def test_inUse1(self):
        ATM.createTable()
        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")
        res = ATM.inUse()

        self.assertEqual(True, res)

        ATM.deleteAll()


    def test_inUse2(self):
        ATM.createTable()
        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        res = ATM.inUse()

        self.assertEqual(False, res)

        ATM.deleteAll()


    def test_login_checkName(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual("John", ATM.currUser.name)

        ATM.deleteAll()

    def test_login_checkUserID(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual("jdoe123", ATM.currUser.userID)

        ATM.deleteAll()


    def test_login_checkPassword(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual("passphrase", ATM.currUser.password)

        ATM.deleteAll()


    def test_login_checkPIN(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", '1234', 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual('1234', ATM.currUser.PIN)

        ATM.deleteAll()


    def test_login_checkBalance(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual(100.99, ATM.currUser.balance)

        ATM.deleteAll()


    def test_login_status(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual(True, ATM.currUser.loginStatus)

        ATM.deleteAll()


    def test_logout(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")
        ATM.logout()

        self.assertEqual("False", ATM.currUser.loginStatus)


    def test_forgotPassword(self):
        ATM.createTable()
        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.forgotPassword("jdoe123", "1234", "newpassword")

        db = sqlite3.connect('user_info.db')
        c = db.cursor()
        c.execute("SELECT userID FROM users")
        c.execute("SELECT password FROM users where userID=?", ("jdoe123",))
        currPass = ','.join(c.fetchone())

        self.assertEqual("newpassword", currPass)
        ATM.deleteAll()


    def test_forgotPassword_incorrectPIN(self):
        with self.assertRaises(ValueError):
            ATM.createTable()
            ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
            ATM.forgotPassword("jdoe123", "4567", "newpassword")

            db = sqlite3.connect('user_info.db')
            c = db.cursor()
            c.execute("SELECT userID FROM users")
            c.execute("SELECT password FROM users where userID=?", ("jdoe123",))

        ATM.deleteAll()


    def test_userExists_True(self):
        ATM.createTable()
        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)

        self.assertEqual(True, ATM.userExists("jdoe123"))
        ATM.deleteAll()


    def test_userExists_False(self):
        ATM.createTable()
        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)

        self.assertEqual(False, ATM.userExists("janedoe"))
        ATM.deleteAll()


if __name__ == '__main__':
    unittest.main()
