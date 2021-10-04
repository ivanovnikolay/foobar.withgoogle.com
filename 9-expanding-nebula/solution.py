results, history = {}, []

def solution(g, prev=None, i=0, j=0):
    M, N = len(g)+1, len(g[0])+1
    prev = prev or [[0]*N for _ in range(M)]
    if j == N:
        return 1

    index = tuple([i, j] + history[-(M+1):])
    if index not in results:
        results[index] = 0
        for gas in (0, 1):
            if i == 0 or j == 0 or (gas + prev[i][j-1] + prev[i-1][j] + prev[i-1][j-1] == 1) == g[i-1][j-1]:
                prev[i][j] = gas
                history.append(gas)
                results[index] += solution(g, prev, (i+1)%M, j+(i+1)//M)
                history.pop()

    return results[index]


assert solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]) == 11567
results, history = {}, []

assert solution([[True, False, True], [False, True, False], [True, False, True]]) == 4
results, history = {}, []

assert solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]) == 254
results, history = {}, []
