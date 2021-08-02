from math import sqrt


def solution(area):
    e = int(sqrt(area))
    if e:
        s = e*e
        return [s] + solution(area - s)
    return []


print(solution(12))
print(solution(15324))
