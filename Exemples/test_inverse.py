import unittest

from Exemples.inverse import inverse


class TestMath(unittest.TestCase):
    def test_inverse(self):
        x = 0
        result = inverse(x)
        self.assertEqual(result, 0.5)


if __name__ == '__main__':
    unittest.main()
