import unittest
from aplikacja1 import dodawanie

class Test(unittest.TestCase):
    def test_add(self):
        self.assertEqual(dodawanie(2, 2), 4)
        self.assertEqual(dodawanie(-1, 1), 0)
        self.assertEqual(dodawanie(0, 0), 0)
        self.assertEqual(dodawanie(-1, -1), -2)

Test()