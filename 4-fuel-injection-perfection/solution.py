def solution(n):
    n = long(n)
    steps = 0
    while 3 < n:
        steps += 1
        if n & 1:
            n += (n & 2) - 1
        else:
            n >>= 1
    return steps + n - 1


assert solution('3') == 2
assert solution('4') == 2
assert solution('15') == 5
