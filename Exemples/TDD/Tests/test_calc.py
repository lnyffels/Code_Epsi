import unittest

from Exemples.TDD.Model.calc import Calc


class TestCalc(unittest.TestCase):
    def test_sum(self):
        cal = Calc()
        result = cal.sum(3,7)
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
