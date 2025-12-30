import unittest
from question21 import password_strength

class TestQuestion21(unittest.TestCase):
    def test_password_strength(self):
        self.assertEqual(password_strength("MyPass123"), "Strong")
        self.assertEqual(password_strength("pass"), "Weak")
        self.assertEqual(password_strength("PASSWORD123"), "Weak")

if __name__ == "__main__":
    unittest.main()
