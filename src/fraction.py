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
        self.depth = 0

        self._increment_depth_of_self_and_children()

    def simplify(self) -> Fraction:
        """
        calling this method on a `Fraction` will recursively simplify the fraction and return a new, simplified `Fraction` object
        for example, `[(1/2)/(4/9)]/3` will return a new `Fraction` object with the value `3/8`
        should reduce the resulting `Fraction` into simplest form. i.e. `2/4` should simplify into `1/2`
        """

        # using the node traversal list order from `self.breadth_first_traversal()`, acting as a heap to recursively simplify the fraction
        # from the bottom up

        nodes: list[Fraction] = self.breadth_first_traversal()

        # good idea:
        # recursive?
        # numerator = numerator.simplify()
        # denominator = denominator.simplify()

        pass

    def breadth_first_traversal(self) -> list[Fraction]:
        """
        returns a list of `Fraction` objects in the order of a breadth-first traversal of the `Fraction` tree
        """

        queue: list[Fraction] = [self]
        visited_nodes: list[Fraction] = []

        # while not empty
        while len(queue) > 0:
            # dequeue the first node (oldest added) ([fifo])
            node: Fraction = queue.pop(0)
            visited_nodes.append(node)
            
            if type(node.numerator) == Fraction:
                queue.append(node.numerator)
            if type(node.denominator) == Fraction:
                queue.append(node.denominator)

        return visited_nodes

    def _increment_depth_of_self_and_children(self):
        if type(self.numerator) == Fraction:
            self.numerator.depth += 1
            self.numerator._increment_depth_of_self_and_children()

        if type(self.denominator) == Fraction:
            self.denominator.depth += 1
            self.denominator._increment_depth_of_self_and_children()

    def __repr__(self) -> str:
        """
        just a utility function to make printing `Fraction`s prettier
        """

        num = "frac" if type(self.numerator) == Fraction else self.numerator
        den = "frac" if type(self.denominator) == Fraction else self.denominator

        return "({} / {}), [{}])".format(num, den, self.depth)
        
        # return "({} / {}), [{}])".format(self.numerator, self.denominator, self.depth)

    def __str__(self) -> str:
        """
        just a utility function to make printing `Fraction`s prettier
        """

        num = "frac" if type(self.numerator) == Fraction else self.numerator
        den = "frac" if type(self.denominator) == Fraction else self.denominator

        return "({} / {}), [{}])".format(num, den, self.depth)

        # return "({} / {}), [{}])".format(self.numerator, self.denominator, self.depth)