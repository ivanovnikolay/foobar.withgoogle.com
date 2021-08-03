def solution(n, b):
    ids = {}
    for i, id in enumerate(generate_ids(n, b)):
        if id in ids:
            return i - ids[id] or 1
        ids[id] = i


def generate_ids(mid, b):
    while True:
        yield mid
        mid = minion_id(mid, b)


def minion_id(n, b):
    x = ''.join(sorted(n, reverse=True))
    y = ''.join(sorted(n))
    z = int(x, b) - int(y, b)
    return itoa(z, b).zfill(len(n))


def itoa(n, b):
    return n < b and str(n) or itoa(n // b, b) + str(n % b)


assert solution('1211', 10) == 1
assert solution('210022', 3) == 3
