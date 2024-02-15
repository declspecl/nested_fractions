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

    def test_hard(self):
        """
        [[(1 / 2) / (1 / 3)] / 10] / [5 / (9 / 5)] = 27 / 500
        """

        f_12: Fraction = Fraction(1, 2)
        f_13: Fraction = Fraction(1, 3)
        f_12_13: Fraction = Fraction(f_12, f_13)
        f_12_13_10: Fraction = Fraction(f_12_13, 10)

        f_95 = Fraction(9, 5)
        f_5_95 = Fraction(5, f_95)

        f_12_13_10_5_95 = Fraction(f_12_13_10, f_5_95)

        correct_simplification = Fraction(27, 500)

        self.assertEqual(f_12_13_10_5_95.simplify(), correct_simplification)

if __name__ == "__main__":
    unittest.main()
