from __future__ import annotations
import math

class Fraction:
    """class used to represent a fraction"""

    def __init__(self, numerator: int | float | Fraction, denominator: int | float | Fraction = 1):
        """
        takes two arguments: `numerator` and `denominator`
        both can be either a number (`int` or `float`) or another `Fraction` to represent nested fractions
        """

        self.numerator = numerator
        self.denominator = denominator

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

        fraction_traversal: list[Fraction] = self.level_order_traversal()
        
        fraction_simplified_queue = fraction_traversal[2 ** self.tree_height - 1:]

        while len(fraction_simplified_queue) > 1:
            current = 0
            temp_simplified_layer: list[Fraction] = []

            while current < len(fraction_simplified_queue):
                temp_simplified_layer.append(fraction_simplified_queue[current] / fraction_simplified_queue[current + 1])
                current += 2

            fraction_simplified_queue = temp_simplified_layer
        
        gcd = math.gcd(fraction_simplified_queue[0].numerator, fraction_simplified_queue[0].denominator)
        fraction_simplified_queue[0].numerator /= gcd
        fraction_simplified_queue[0].denominator /= gcd

        return fraction_simplified_queue[0]

    def level_order_traversal(self) -> list[Fraction]:
        """
        returns a list of `Fraction` objects in a level-order traversal (same as BFS) of the `Fraction` tree
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
        expands all `Fraction`s recursively to create a symmetrical, perfect binary tree with `n=root.tree_height+1` layers of `Fraction`s
        """

        # am i on the bottom of the tree? (am i a double constant fraction)
        if self.tree_height == 0:
            return
        
        # i am not on the bottom of the tree
        if type(self.numerator) != Fraction:
            self.numerator = Fraction(self.numerator, 1)

        self.numerator.tree_height = self.tree_height - 1
        self.numerator.expand()

        # i am not on the bottom of the tree
        if type(self.denominator) != Fraction:
            self.denominator = Fraction(self.denominator, 1)

        self.denominator.tree_height = self.tree_height - 1
        self.denominator.expand()

    def __repr__(self) -> str:
        """
        just a utility function to make printing `Fraction`s prettier
        """

        return "({} / {}) @ {}".format(self.numerator, self.denominator, self.tree_height)

    def __str__(self) -> str:
        """
        just a utility function to make printing `Fraction`s prettier
        """

        return "({} / {}) @ {}".format(self.numerator, self.denominator, self.tree_height)
    
    def __eq__(self, other: Fraction) -> bool:
        """
        compares two `Fraction` objects for equality by comparing their numerator and denominator values
        """

        return self.numerator == other.numerator and self.denominator == other.denominator
    
    def __truediv__(self, other: Fraction) -> Fraction:
        """
        overloads the `/` operator to allow for division of `Fraction` objects
        """

        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __floordiv__(self, other: Fraction) -> Fraction:
        """
        overloads the `//` operator to allow for floor division of `Fraction` objects
        """

        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
