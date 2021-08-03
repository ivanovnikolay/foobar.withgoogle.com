from math import sqrt


def solution(area):
    e = int(sqrt(area))
    if e:
        s = e*e
        return [s] + solution(area - s)
    return []


assert solution(12) == [9, 1, 1, 1]
assert solution(15324) == [15129, 169, 25, 1]
