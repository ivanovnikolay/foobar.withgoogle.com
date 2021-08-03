def solution(x, y):
    x, y, i = int(x), int(y), 0
    try:
        while (x, y) != (1, 1):
            if x > y: x, y = y, x
            n = y - 1 if x == 1 else y // x
            y, i = y - n * x, i + n
        return str(i)
    except ZeroDivisionError:
        return 'impossible'


assert solution('4', '7') == '4'
assert solution('2', '1') == '1'
assert solution('2', '4') == 'impossible'
