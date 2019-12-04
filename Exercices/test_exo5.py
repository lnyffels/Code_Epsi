# Correction
import unittest
from Exercices.exo5 import *

class TestCapitalize(unittest.TestCase):

   def test_replace_i(self):
        s = "my name is Bob. i live in Lille"
        result= replace_i(s)
        self.assertEqual(result, "my name is Bob. I live in Lille")

   def test_replace_first_letter(self):
        s = "my name is Bob"
        result = replace_first_letter(s)
        self.assertEqual(result, "My name is Bob")

   def test_capitalize_first_letter_after_accentuation(self):
       s = "Hello Bob. what time do you have to be there ? it is your address ! yes or not"
       result = capitalize_first_letter_after_accentuation_character(s)
       self.assertEqual(result, "Hello Bob. What time do you have to be there ? It is your address ! Yes or not")

   def test_capitalize(self):
       s = "hello Bob. i am Greg. what time do you have to be there ? it is your address ! yes or not"
       result = capitalize(s)
       self.assertEqual(result, "Hello Bob. I am Greg. What time do you have to be there ? It is your address ! Yes or not")


if __name__ == '__main__':
    unittest.main()
