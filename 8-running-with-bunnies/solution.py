from itertools import permutations, product


def solution(times, times_limit):
    bunnies = range(len(times) - 2)

    negative_cicle = bellman_ford(times)
    if negative_cicle:
        return bunnies

    for i in range(len(bunnies), 0, -1):
        for rescued in permutations(bunnies, i):
            path = [0] + [r+1 for r in rescued] + [len(bunnies)+1]
            time = reduce(lambda s, p: s + times[p[0]][p[1]], zip(path, path[1:]), 0)
            if time <= times_limit:
                return sorted(rescued)
    return []


def bellman_ford(G):
    nodes = range(len(G))
    for node, u, v in product(nodes, repeat=3):
        if G[u][node] + G[node][v] < G[u][v]:
            G[u][v] = G[u][node] + G[node][v]
    return any(G[u][u] < 0 for u in nodes)


assert solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1) == [1, 2]
assert solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3) == [0, 1]
