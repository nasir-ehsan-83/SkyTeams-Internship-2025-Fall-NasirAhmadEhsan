import unittest
from question8 import ATM

class TestATM(unittest.TestCase):
    def test_cases(self):
        atm = ATM()
        self.assertEqual(atm.deposit(100), "100 deposited successfully")
        self.assertEqual(atm.withdraw(50), "50 withdrawn successfully")
        self.assertEqual(atm.get_balance(), 50)
        self.assertEqual(atm.withdraw(100), "Insufficient balance")

if __name__ == "__main__":
    unittest.main()
