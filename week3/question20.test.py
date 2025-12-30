import unittest
from question20 import bmi_calculator

class TestQuestion20(unittest.TestCase):
    def test_bmi_calculator(self):
        self.assertEqual(bmi_calculator(70,1.75), (22.86,'Normal weight'))
        self.assertEqual(bmi_calculator(50,1.75), (16.33,'Underweight'))

if __name__ == "__main__":
    unittest.main()
