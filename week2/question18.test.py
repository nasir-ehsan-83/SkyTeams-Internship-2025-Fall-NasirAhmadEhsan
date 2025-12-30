import unittest
from question18 import multiplication_table

class TestQuestion18(unittest.TestCase):
    def test_multiplication_table(self):
        table = multiplication_table(5,3)
        self.assertEqual(table, [(5,1,5),(5,2,10),(5,3,15)])

if __name__ == "__main__":
    unittest.main()
