"""
플로이드와샬
"""
from sys import stdin
from typing import List


def floyd_warshall(n: int, graph: List[List[int]]) -> None:
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    graph = [[0] * (n + 1)] + \
            [[0] + list(map(int, input().split())) for _ in range(n)]

    floyd_warshall(n, graph)

    for _ in range(m):
        a, b, c = map(int, input().split())
        if graph[a][b] <= c:
            print("Enjoy other party")
        else:
            print("Stay here")


if __name__ == "__main__":
    main()
