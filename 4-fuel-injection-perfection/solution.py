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


print(solution('3'))
print(solution('4'))
print(solution('15'))
