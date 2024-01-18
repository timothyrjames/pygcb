import math

class RationalNumber(object):
    def __init__(self, numerator, divisor):
        self.n = numerator
        self.d = divisor
        self.reduce()

    def __add__(self, other):
        # Use a common divisor and add the numerators.
        d = self.d * other.d
        n = self.n * other.d + other.n * self.d
        return RationalNumber(n, d) 

    def __sub__(self, other):
        # Subtraction is just addition with a negated 2nd operand.
        return self.__add__(-other)

    def __mul__(self, other):
        # Multiply numerators and divisors.
        n = self.n * other.n
        d = self.d * other.d
        return RationalNumber(n, d)

    def __truediv__(self, other):
        # Division is just the reverse of multiplication.
        return self.__mul__(RationalNumber(other.d, other.n))

    def __neg__(self):
        # Negate with a new RationalNumber with negated numerator.
        return RationalNumber(-self.n, self.d)

    def __str__(self):
        return '%s / %s' % (int(self.n), int(self.d))

    def reduce(self):
        a = self.n
        b = self.d
        # Use modulo operator to find even divisors.
        # Keep iterating until we find one (which might be 1).
        while a % b != 0:
            temp = b
            b = a % b
            a = temp
        # Once greatest common divisor is found, reset numerator and divisor.
        self.n = self.n / b
        self.d = self.d / b

half = RationalNumber(1, 2)
seventh = RationalNumber(1, 7)
quarter = RationalNumber(8, 32)
six = RationalNumber(6, 1)

print(half)
print(seventh)
print(quarter)

# use __mul__
print('Half of a quarter is %s.' % (half * quarter))

# use __truediv__
print('There are %s quarters in a half.' % (half / quarter))

# use __sub__
print('Half minus a seventh is %s.' % (half - seventh))

# use __add__
print('Six plus a half is %s.' % (six + half))

# use __trudiv__
print('There are %s sevenths in six.' % (six / seventh))