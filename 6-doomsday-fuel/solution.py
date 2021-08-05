from fractions import Fraction


def solution(m):
    # Markov chain absorb
    sums = [sum(r) for r in m]
    Q = Matrix([[Fraction(e, sums[i]) for j, e in enumerate(r) if sums[j]] for i, r in enumerate(m) if sums[i]])
    R = Matrix([[Fraction(e, sums[i]) for j, e in enumerate(r) if not sums[j]] for i, r in enumerate(m) if sums[i]])
    L = ~(Matrix.E(len(Q)) - Q) * R
    s0 = L[0]
    denominator = max(f.denominator for f in s0)
    return [(f*denominator).numerator for f in s0] + [denominator]


class Matrix(list):
    @classmethod
    def E(cls, n):
        return cls([[i==j for i in range(n)] for j in range(n)])

    def __add__(self, o):
        return Matrix([[i+j for i, j in zip(r, c)] for r, c in zip(self, o)])

    def __sub__(self, o):
        return self + o*(-1)

    def __mul__(self, o):
        if isinstance(o, Matrix):
            return Matrix([[sum(i*j for i, j in zip(r, c)) for c in o.transpose()] for r in self])
        return Matrix([[o*e for e in r] for r in self])

    def __invert__(self):
        m = Matrix()
        det = abs(self)
        for i in range(len(self)):
            r = []
            for j in range(len(self)):
                r.append((-1)**(i+j)*abs(self.minor(i, j)))
            m.append(r)
        return m.transpose() * Fraction(1, det)

    def __abs__(self):
        if len(self) == 1:
            return self[0][0]
        if len(self) == 2:
            return self[0][0]*self[1][1] - self[0][1]*self[1][0]

        det = 0
        for i in range(len(self)):
            det += ((-1)**i)*self[0][i]*abs(self.minor(0, i))
        return det

    def transpose(self):
        return Matrix([c for c in zip(*self)])

    def minor(self, i, j):
        return Matrix([r[:j] + r[j+1:] for r in (self[:i] + self[i+1:])])


print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))
print(solution([[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]))
