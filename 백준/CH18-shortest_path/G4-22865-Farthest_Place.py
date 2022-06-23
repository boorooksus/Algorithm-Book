"""
플로이드 와샬
시간 초과
"""
from sys import stdin


input = lambda: stdin.readline().rstrip()
INF = 10001


def floyd_warshall():
    for k in range(1, 7):
        for i in range(1, 7):
            for j in range(1, 7):
                if i == j:
                    graph[i][j] = 0
                    continue

                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    dists = [(INF, 0)] * (N + 1)
    for i in range(1, N + 1):
        if 0 < graph[A][i] < dists[i][0]:
            dists[i] = (graph[A][i], -i)
        if 0 < graph[B][i] < dists[i][0]:
            dists[i] = (graph[B][i], -i)
        if 0 < graph[C][i] < dists[i][0]:
            dists[i] = (graph[C][i], -i)

    res = sorted(list(dists))

    while res and res[-1][0] == INF:
        res.pop()

    return -res[-1][1]


if __name__ == "__main__":
    N = int(input())
    A, B, C = map(int, input().split())
    M = int(input())

    graph = list([INF] * (N + 1) for _ in range(N + 1))
    for _ in range(M):
        D, E, L = map(int, input().split())
        graph[D][E] = L
        graph[E][D] = L

    print(floyd_warshall())
