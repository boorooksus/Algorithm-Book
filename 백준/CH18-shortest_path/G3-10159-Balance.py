"""
플로이드 와샬
통과
"""
import sys
input = lambda: sys.stdin.readline().rstrip()


INF = 2001


def floyd_warshall() -> None:
    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = list([INF] * (N + 1) for _ in range(N + 1))
    for i in range(N):
        graph[i][i] = 0

    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1

    floyd_warshall()
    for i in range(1, N + 1):
        if i == 4:
            here = 0
        cnt = 0
        for j in range(1, N + 1):
            if i != j and graph[i][j] != INF:
                cnt += 1
            if i != j and graph[j][i] != INF:
                cnt += 1
        print(N - cnt - 1)


