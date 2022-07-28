"""
플로이드 와샬
시간초과
"""
from sys import stdin
input = lambda: stdin.readline().rstrip()
INF = 1_000_000


def floyd_warshall() -> int:
    for i in range(1, N + 1):
        graph[i][i] = 0

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            if i == k:
                continue
            for j in range(1, N + 1):
                if j == k:
                    continue
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    res = 0
    for i in range(1, N + 1):
        res = max(graph[i][X] + graph[X][i], res)
    return res


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    graph = [[INF] * (N + 1) for _ in range(N + 1)]
    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a][b] = t

    print(floyd_warshall())
