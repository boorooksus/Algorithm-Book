from sys import stdin
from collections import defaultdict
from math import sqrt


parents = defaultdict(int)


def find(x: int) -> int:
    if parents[x] == 0 or parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruskal() -> int:
    dists = []
    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            dists.append((sqrt((crds[i][0] - crds[j][0]) ** 2 + (crds[i][1] - crds[j][1]) ** 2), i, j))

    dists.sort()
    ans = 0
    for dist, x, y in dists:
        x, y = find(x), find(y)
        if x != y:
            union(x, y)
            ans += dist
            if cnt == N - 1:
                break

    return ans


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N, M = map(int, input().split())
    crds = [[]] + [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())
        union(a, b)
        cnt += 1

    print("%.2f" % kruskal())
