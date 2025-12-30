import unittest
from question7 import rock_paper_scissors

class TestRPS(unittest.TestCase):
    def test_cases(self):
        # Since random is involved, just test if output is one of the expected
        for choice in ["rock","paper","scissors"]:
            result = rock_paper_scissors(choice)
            self.assertIn(result, ["Draw","Player wins","Computer wins"])

if __name__ == "__main__":
    unittest.main()
