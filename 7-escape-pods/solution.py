from sys import maxint as Inf


def solution(entrances, exits, path):
    graph, source, sink = set_1source_1sink(entrances, exits, path)
    return ford_fulkerson_max_flow(graph, source, sink)


def set_1source_1sink(entrs, exits, G):
    return [[0] + [i in entrs and Inf or 0 for i in range(len(G))] + [0]] + \
           [[0] + r + [i in exits and Inf or 0] for i, r in enumerate(G)] + \
           [[0] * (len(G) + 2)], 0, len(G) + 1


def ford_fulkerson_max_flow(G, s, t):
    max_flow = 0
    while True:
        parents = bfs(G, s, t)
        if not parents:
            break

        path_gen = lambda p, s, v: [] if s == v else [(v, p[v])] + path_gen(p, s, p[v])
        path = path_gen(parents, s, t)

        flow = reduce(min, (G[v][u] for u, v in path), Inf)
        max_flow += flow

        for u, v in path:
            G[u][v] += flow
            G[v][u] -= flow
    return max_flow


def bfs(G, s, t):
    queue = [s]
    parents = [-1] * len(G)
    visited = [i == s for i in range(len(G))]
    while queue:
        u = queue.pop(0)
        for i, v in ((i, v) for i, v in enumerate(G[u]) if not visited[i] and 0 < v):
            parents[i] = u
            if i == t:
                return parents
            visited[i] = True
            queue.append(i)
    return []


assert solution([0, 1], [4, 5], [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]) == 16
assert solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]) == 6
