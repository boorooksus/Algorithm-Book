from sys import stdin, setrecursionlimit
from typing import List
setrecursionlimit(10 ** 9)


parents = []


def find(x: int) -> int:
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruskal(n: int, planets: List[List[int]]) -> int:
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            edges.append((planets[i][j], i, j))

    edges.sort()
    cost = 0
    for edge, a, b in edges:
        if find(a) == find(b):
            continue
        union(a, b)
        cost += edge

    return cost


def main():
    def input():
        return stdin.readline().rstrip()
    global parents

    n = int(input())
    planets = [list(map(int, input().split())) for _ in range(n)]
    parents = list(i for i in range(n))
    print(kruskal(n, planets))


if __name__ == "__main__":
    main()
