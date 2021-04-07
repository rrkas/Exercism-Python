from __future__ import division

import math


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        self.__reduce()

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        numer = self.numer * other.denom + self.denom * other.numer
        denom = self.denom * other.denom
        r = Rational(numer, denom)
        r.__reduce()
        return r

    def __sub__(self, other):
        numer = self.numer * other.denom - self.denom * other.numer
        denom = self.denom * other.denom
        r = Rational(numer, denom)
        r.__reduce()
        return r

    def __mul__(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        r = Rational(numer, denom)
        r.__reduce()
        return r

    def __truediv__(self, other):
        numer = self.numer * other.denom
        denom = self.denom * other.numer
        r = Rational(numer, denom)
        r.__reduce()
        return r

    def __abs__(self):
        numer = abs(self.numer)
        denom = abs(self.denom)
        return Rational(numer, denom)

    def __pow__(self, power):
        r = Rational(self.numer, self.denom)
        r.numer **= power
        r.denom **= power
        return r

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)

    def __reduce(self):
        def compute_hcf(x, y):
            while (y):
                x, y = y, x % y
            return x
        hcf = compute_hcf(self.numer, self.denom)
        self.numer //= hcf
        self.denom //= hcf