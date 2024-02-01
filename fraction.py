from __future__ import annotations

class Fraction:
    """class used to represent a fraction"""

    def __init__(self, numerator: int | float | Fraction, denominator: int | float | Fraction = 1):
        """
        takes two arguments: `numerator` and `denominator`
        both can be either a number (`int` or `float`) or another `Fraction` to represent nested fractions
        """

        self.numerator = numerator
        self.denominator = denominator

    def simplify(self) -> Fraction:
        """
        calling this method on a `Fraction` will recursively simplify the fraction and return a new, simplified `Fraction` object
        for example, `[(1/2)/(4/9)]/3` will return a new `Fraction` object with the value `3/8`
        should reduce the resulting `Fraction` into simplest form. i.e. `2/4` should simplify into `1/2`
        """

        pass

    def __repr__(self) -> str:
        """
        just a utility function to make printing `Fraction`s prettier
        """

        return "({} / {})".format(self.numerator, self.denominator)

    def __str__(self) -> str:
        """
        just a utility function to make printing `Fraction`s prettier
        """

        return "({} / {})".format(self.numerator, self.denominator)
