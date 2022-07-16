"""
floyd warshall + brute force
통과
"""
from sys import stdin
input = lambda: stdin.readline().rstrip()
INF = 100000


def floyd_warshall() -> None:
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(i + 1, N + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    graph[j][i] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = list([INF] * (N + 1) for _ in range(N + 1))
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 2
        graph[b][a] = 2

    floyd_warshall()
    ans = [0, 0, INF]
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            temp = 0
            for k in range(1, N + 1):
                if k != i and k != j:
                    temp += min(graph[i][k], graph[j][k])
            if temp < ans[2]:
                ans = [i, j, temp]
    print(*ans)

