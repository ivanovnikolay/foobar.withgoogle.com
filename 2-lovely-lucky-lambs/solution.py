from itertools import takewhile


def solution(total_lambs):
    def fib_sum():
        f1, f2, s = 0, 1, 0
        while True:
            f1, f2, s = f2, f1+f2, f2+s
            yield s

    def stingy():
        return sum(1 for _ in takewhile(lambda s: s <= total_lambs, fib_sum()))

    def generous():
        return int.bit_length(total_lambs + 1) - 1

    return stingy() - generous()


assert solution(10) == 1
assert solution(143) == 3
