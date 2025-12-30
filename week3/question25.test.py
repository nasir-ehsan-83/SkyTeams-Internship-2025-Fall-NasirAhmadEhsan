import unittest
from question25 import guess_number_game

class TestQuestion25(unittest.TestCase):
    def test_guess_number_game(self):
        self.assertEqual(guess_number_game(50,50), "Correct")
        self.assertEqual(guess_number_game(50,40), "Too Low")
        self.assertEqual(guess_number_game(50,60), "Too High")

if __name__ == "__main__":
    unittest.main()
