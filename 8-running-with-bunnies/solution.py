from sys import maxint as Inf
from itertools import permutations


def solution(times, times_limit):
    bunnies = range(len(times) - 2)
    try:
        for u in range(len(times)):
            print(bellman_ford(times, u))
    except StopIteration:
        return bunnies


def bellman_ford(G, s):
    V = range(len(G))
    dist = [0 if u == s else Inf for u in V]
    edges = [(u, v, G[u][v]) for u, v in permutations(V, 2)]

    for u, v, w in edges:
        if w and dist[u] + w < dist[v]:
            dist[v] = dist[u] + w

    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise StopIteration('Negative cicle')

    return dist


solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1)
solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3)
#assert solution([[0, 2, 2, 2, -1], [9, 0, 2, 2, -1], [9, 3, 0, 2, -1], [9, 3, 2, 0, -1], [9, 3, 2, 2, 0]], 1) == [1, 2]
#assert solution([[0, 1, 1, 1, 1], [1, 0, 1, 1, 1], [1, 1, 0, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0]], 3) == [0, 1]
