import unittest
from question12 import traffic_light

class TestQuestion12(unittest.TestCase):
    def test_traffic_light(self):
        self.assertEqual(traffic_light('Red'), "Stop")
        self.assertEqual(traffic_light('Yellow'), "Ready")
        self.assertEqual(traffic_light('Green'), "Go")
        self.assertEqual(traffic_light('Blue'), "Invalid")

if __name__ == "__main__":
    unittest.main()
