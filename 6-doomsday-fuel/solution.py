from fractions import Fraction, gcd


def solution(m):
    ''' Markov chain absorb '''
    S = [sum(r) for r in m]
    Q = Matrix([Fraction(e, S[i]) for j, e in enumerate(r) if S[j] == 0] for i, r in enumerate(m) if S[i])
    R = Matrix([Fraction(e, S[i]) for j, e in enumerate(r) if S[j] != 0] for i, r in enumerate(m) if S[i])
    if Q and R:
        I = Matrix.I(n=len(Q))
        F = ~(I - Q)
        s0 = (F * R)[0]
    else:
        s0 = [Fraction(1, 1)]
    d = lcm(*[f.denominator for f in s0 if f.numerator])
    return [(f*d).numerator for f in s0] + [d]


def lcm(*numbers):
    ''' Least Common Multiple '''
    return reduce(lambda a, b: a * b // gcd(a, b), numbers)


class Matrix(list):
    @classmethod
    def I(cls, n):
        return cls([i == j for i in range(n)] for j in range(n))

    def __sub__(self, o):
        return Matrix([i - j for i, j in zip(r, c)] for r, c in zip(self, o))

    def __mul__(self, o):
        return isinstance(o, Matrix) and \
            Matrix([sum(i * j for i, j in zip(r, c)) for c in o.transpose()] for r in self) or \
            Matrix([i * o for i in r] for r in self)

    def __invert__(self):
        ''' Returns an invert matrix '''
        adj = Matrix([(-1)**(i+j)*abs(self.minor(i, j)) for j in self.indexes()] for i in self.indexes()).transpose()
        det = abs(self)
        return adj * Fraction(1, det)

    def __abs__(self):
        ''' Returns a determinant '''
        return len(self) == 1 and self[0][0] or \
            reduce(lambda det, j: det + ((-1)**j)*self[0][j]*abs(self.minor(0, j)), self.indexes(), 0)

    def indexes(self):
        return range(len(self))

    def transpose(self):
        return Matrix(c for c in zip(*self))

    def minor(self, i, j):
        return Matrix(r[:j] + r[j+1:] for r in self[:i] + self[i+1:])


assert solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]) == [7, 6, 8, 21]
assert solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == [0, 3, 2, 9, 14]
