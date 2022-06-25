from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] < 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> bool:
    x, y = find(x), find(y)
    parents[x] += parents[y]
    parents[y] = find(x)
    return True


def kruskal():
    roads.sort(key=lambda x: x[2])
    res = 0
    for u, v, d in roads:
        if colleges[u] == colleges[v]:
            continue
        u, v = find(u), find(v)
        if u != v:
            union(u, v)
            res += d
            if parents[u] == -N:
                return res

    return -1


if __name__ == "__main__":
    N, M = map(int, input().split())
    colleges = [''] + list(input().split())
    parents = [-1] * (N + 1)
    graph = defaultdict(list)
    roads = list(list(map(int, input().split())) for _ in range(M))

    print(kruscal())

