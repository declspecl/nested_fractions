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

        correct_simplification = Fraction(3, 9)

        self.assertEqual(frac_of_above_over_three.simplify(), correct_simplification)

if __name__ == "__main__":
    # make a couple fraction objects & print them
    
    fraction1: Fraction = Fraction(1, 2)
    fraction2: Fraction = Fraction(1, 3)
   
    print(fraction1)
    print(fraction2)

    # make a nested fraction and print it
    fraction3: Fraction = Fraction(fraction1, fraction2)
    fraction4: Fraction = Fraction(fraction3, 10)

    print(fraction4)

    # (((1 / 2) / (1 / 3)) / 10)
    # result = Fraction(left.numerator * right.denominator, left.denominator * right.numerator)

    # ((3 / 2) / 10)
    # ((3 / 2) / (10 / 1))
    # result = Fraction(left.numerator * right.denominator, left.denominator * right.numerator)

    # (3 / 20)

    # unittest.main()
