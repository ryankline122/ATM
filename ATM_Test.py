import sqlite3
import unittest
import ATM

# In the terminal:
# "python -m pytest --cov=ATM
# "python -m pytest -v --cov=ATM --cov-report=html

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


    def test_login1(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual("John", ATM.currUser.name)

        ATM.deleteAll()

    def test_login2(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual("jdoe123", ATM.currUser.userID)

        ATM.deleteAll()


    def test_login3(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual("passphrase", ATM.currUser.password)

        ATM.deleteAll()


    def test_login4(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", '1234', 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual('1234', ATM.currUser.PIN)

        ATM.deleteAll()


    def test_login5(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual(100.99, ATM.currUser.balance)

        ATM.deleteAll()


    def test_login6(self):
        ATM.createTable()

        ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
        ATM.login("jdoe123", "passphrase")

        self.assertEqual(True, ATM.currUser.loginStatus)

        ATM.deleteAll()

if __name__ == '__main__':
    unittest.main()
