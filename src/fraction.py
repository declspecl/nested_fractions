from __future__ import annotations

import math

class Fraction:
    """class used to represent a fraction"""

    def __init__(self, numerator: int | float | Fraction, denominator: int | float | Fraction = 1, tree_height: int | None = None):
        """
        takes two arguments: `numerator` and `denominator`
        both can be either a number (`int` or `float`) or another `Fraction` to represent nested fractions
        """

        self.numerator = numerator
        self.denominator = denominator

        # only if manually overridden
        if not tree_height is None:
            self.tree_height = tree_height

        # if left empty (natural Fraction generation)
        else:
            numerator_tree_height: int = self.numerator.tree_height if type(self.numerator) == Fraction else -1
            denominator_tree_height: int = self.denominator.tree_height if type(self.denominator) == Fraction else -1

            highest_tree_height_of_numerator_or_denominator: int = max(numerator_tree_height, denominator_tree_height)

            # will be 0 if numerator and denominator are both constants
            # will be 1 or higher BY DEFINITION if either the numerator or denominator is a fraction
            self.tree_height: int = highest_tree_height_of_numerator_or_denominator + 1

            # results in root node having the highest tree height, and double constants fractions having 0 tree height

    def simplify(self) -> Fraction:
        """
        calling this method on a `Fraction` will recursively simplify the fraction and return a new, simplified `Fraction` object
        for example, `[(1/2)/(4/9)]/3` will return a new `Fraction` object with the value `3/8`
        should reduce the resulting `Fraction` into simplest form. i.e. `2/4` should simplify into `1/2`
        """

        self.expand()

        fraction_traversal: list[Fraction] = self.breadth_first_traversal()

        new_fraction: Fraction = Fraction(1, 1)

        # there are (2 ** (self.tree_height + 1)) - 1 nodes in the tree
        # the last layer fractions are the final 2 ** self.tree_height nodes

        i: int = len(fraction_traversal) - (2 ** self.tree_height)
        should_flip_operation: bool = False

        while i + 1 < len(fraction_traversal):
            left = fraction_traversal[i]
            right = fraction_traversal[i + 1]
            
            if not should_flip_operation:
                new_fraction.numerator *= (left.numerator * right.denominator)
                new_fraction.denominator *= (left.denominator * right.numerator)
            else:
                new_fraction.numerator *= (left.denominator * right.numerator)
                new_fraction.denominator *= (left.numerator * right.denominator)

            i += 2
            should_flip_operation = not should_flip_operation

        gcd = math.gcd(new_fraction.numerator, new_fraction.denominator)

        new_fraction.numerator //= gcd
        new_fraction.denominator //= gcd

        return new_fraction

    def breadth_first_traversal(self) -> list[Fraction]:
        """
        returns a list of `Fraction` objects in the order of a breadth-first traversal of the `Fraction` tree
        """

        queue: list[Fraction] = [self]
        visited_nodes: list[Fraction] = []

        # while not empty
        while len(queue) > 0:
            # dequeue the first node (oldest added) ([fifo])
            node: Fraction = queue.pop(0) # queue = [], visited = [self, num, dem]
            visited_nodes.append(node)
            
            if type(node.numerator) == Fraction:
                queue.append(node.numerator)
            if type(node.denominator) == Fraction:
                queue.append(node.denominator)

        return visited_nodes
    
    def expand(self):
        """
        expands all `Fraction`s recursively to create a symmetrical, perfect binary tree with `n=root.depth` layers
        """

        # am i on the bottom of the tree? (am i a double constant fraction)
        if self.tree_height == 0:
            return
        
        # i am not on the bottom of the tree
        if type(self.numerator) != Fraction:
            self.numerator = Fraction(self.numerator, 1, self.tree_height - 1)

        self.numerator.expand()

        # i am not on the bottom of the tree
        if type(self.denominator) != Fraction:
            self.denominator = Fraction(self.denominator, 1, self.tree_height - 1)

        self.denominator.expand()

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
    
    def __eq__(self, other: Fraction) -> bool:
        """
        compares two `Fraction` objects for equality by comparing their numerator and denominator values
        """

        return self.numerator == other.numerator and self.denominator == other.denominator