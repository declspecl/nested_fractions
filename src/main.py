import unittest
from fraction import Fraction

class FractionTest(unittest.TestCase):
    def test_easy(self):
        """
        (45 / 93) / 5 = 3 / 31
        """

        fourty_three_over_ninety = Fraction(45, 93)
        above_over_five = Fraction(fourty_three_over_ninety, 5)

        correct_simplification = Fraction(3, 31)

        self.assertEqual(above_over_five.simplify(), correct_simplification)

    def test_medium(self):
        """
        [(1 / 2) / (4 / 9)] / 3 = 3 / 8
        """

        one_over_two = Fraction(1, 2)
        four_over_nine = Fraction(4, 9)

        frac_of_above = Fraction(one_over_two, four_over_nine)

        frac_of_above_over_three = Fraction(frac_of_above, 3)

        correct_simplification = Fraction(3, 8)

        self.assertEqual(frac_of_above_over_three.simplify(), correct_simplification)

if __name__ == "__main__":
    unittest.main()

# nested fraction manifesto
# if we expand everything to the deepest point, the deepest layer will be ONLY constants and thus can be trivially simplified (DCFs)
# performing a breadth-first traversal will place all of the DCFs at the end of the list, which can then be evaluated independently in pairs