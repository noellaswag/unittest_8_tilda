import unittest

from tilda_lab_8_med_kattis import *



class TestLab8_syntax(unittest.TestCase):  # unittest.TestCase är inbyggt

    def test_check_number(self):
        # problemet är try_syntax -> den måste anropas rätt i lab 8 ?
        self.assertEqual(try_syntax("H2"), "Formeln är syntaktiskt korrekt")
        # försökte skriva om en ny try_syntax funktion men det funkade ej

    def test_upper_letter(self):
        self.assertEqual(try_syntax("Co3", "Formeln är syntaktiskt korrekt"))

    def testa_fel_funtkion(self):
        self.assertEqual(try_syntax("C0100", "För litet tal vid radslutet"))  # dubbelkolla så det är rätt print

#början på nytt test - ej fullständig
    """
    def test_input(self):
        print("Testar att den ger rätt utskrift")
        ord = "He3"
        result = "He3"
        if self.assertEqual(ord, result):
            print("Formeln är syntaktiskt korrekt")
            
            """


if __name__ == '__main__':
    unittest.main()

"""
förslag: ny funktion try_new_syntax
    def test_check(self):
        self.assertEqual(try_new_syntax("co3"), "Formeln är syntaktiskt korrekt")

"""
