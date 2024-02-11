import unittest
from fraction2 import Fraction

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
    fraction1: Fraction = Fraction(1, 2) # 0
    fraction2: Fraction = Fraction(1, 3) # 0
    fraction3: Fraction = Fraction(fraction1, fraction2) # 1
    fraction4: Fraction = Fraction(3, fraction3) # 2

    fraction12: Fraction = Fraction(1, 3) # 0
    fraction13: Fraction = Fraction(fraction12, fraction2) # 1
    fraction14: Fraction = Fraction(fraction13, fraction3) # 2


    fraction5 = Fraction(fraction4, 5) # 0
    fraction6 = Fraction(5, fraction5) # 1

    fraction7 = Fraction(fraction14, fraction6) # 3

    fraction7._depthify()
    print(fraction7)
    # unittest.main()

# nested fraction manifesto
# if we normalize everything, the deepest layer will be ONLY constants and thus can be trivially simplifi