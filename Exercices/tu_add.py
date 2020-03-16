import unittest


class Calcul:
    def __init__(self):
        pass

    def additionne(self, a, b):
        return a - b


class MyTestAdditionneCase(unittest.TestCase):
    def test_addionne(self):
        # Arrange
        a = 6
        b = 4
        mon_objet_calcul = Calcul()

        # Act
        result = mon_objet_calcul.additionne(a, b)


        # Assert
        self.assertEqual(result, 10)


if __name__ == '__main__':
    unittest.main()
