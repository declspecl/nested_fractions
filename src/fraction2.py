from __future__ import annotations

class Fraction:
    """class used to represent a fraction"""

    def __init__(self, numerator: int | float | Fraction, denominator: int | float | Fraction = 1):
       

        #         d=1 R
        #         /       \
        #        3         f
        #                 / \       
        #                4   f     
        #                    |   
        #d=4                1 5

        #array length = 2^d
        array = [-1] * ((2 ** d) - 1)
        heap = [1,1,1]
        
        #heap = [r(1),3(2),f(2),4(3),f(3),1(4),5(4)]
        
        #array = [r,f,3,4,f,3,1,4,1,1,5,3,1,1,1]
        # bfs = [r,f,3,4,f,3,1,4,1,1,5,3,1,1,1]

        # left = 2k + 1
        # 
        
    def makebiglist(self):
        array = []
        array.append(self)
        if type(self.numerator) == int:
            self.numerator = Fraction(self.numerator, 1)
        array.append(self.denominator)
        array.append(self.numerator.numerator)
        array.append(self.numerator.denominator)
        array.append(self.denominator.numerator)
        array.append(self.denominator.denominator)
        array.append(self.numerator.numerator.numerator)
        array.append(self.numerator.numerator.denominator)
        array.append(self.numerator.denominator.numerator)
        array.append(self.numerator.denominator.denominator)
        array.append(self.denominator.numerator.numerator)
        array.append(self.denominator.numerator.denominator)
        array.append(self.denominator.denominator.numerator)
        array.append(self.denominator.denominator.denominator)
