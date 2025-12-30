import unittest
from question12 import evalRPN

class TestRPN(unittest.TestCase):
    def test_rpn(self):
        self.assertEqual(evalRPN(["2","1","+","3","*"]), 9)
        self.assertEqual(evalRPN(["4","13","5","/","+"]), 6)
        self.assertEqual(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]), 22)

if __name__ == "__main__":
    unittest.main()
