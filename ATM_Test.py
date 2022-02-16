import sqlite3
import unittest
import ATM

# In the terminal:
# "python -m pytest --cov=ATM
# "python -m pytest -v --cov=ATM --cov-report=html

class TestAccountCreation(unittest.TestCase):

    def test_newAccount1(self):
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
        self.assertEqual(success, True)

        ATM.deleteAll()

    # def test_newAccount2(self):
    #     ATM.createTable()
    #
    #     db = sqlite3.connect('user_info.db')
    #     c = db.cursor()
    #     ATM.createAccount("John", "jdoe123", "passphrase", 1234, 100.99, False)
    #     c.execute("SELECT exists(SELECT userID FROM users where userID=?)", ("jdoe123",))
    #     [exists] = c.fetchone()
    #     if(exists):
    #         success = True
    #     else:
    #         success = False
    #     self.assertEqual(False, success)
    #
    #     ATM.deleteAll()



if __name__ == '__main__':
    unittest.main()
