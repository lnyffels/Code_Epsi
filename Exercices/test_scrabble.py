import unittest


"""
1 point		A, E, I, L, N, O, R, S, T et U 
2 points		D et G
3 points		B, C, M et P
4 points		F, H, V, W et Y
5 points		K
8 points		J et X
10 points		Q et Z

"""

class TestScrabble(unittest.TestCase):
    def test_valeur_mot(self):
        mot = "azerty"
        val = donner_valeur_mot(mot)
        self.assertEqual(val, 18)


if __name__ == '__main__':
    unittest.main()
