from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] == 0:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def kruscal() -> int:
    dists = []
    for i in range(N - 1):
        for j in range(i + 1, N):
            dist = min(list(abs(planets[i][k] - planets[i][k]) for k in range(2)))
            dists.append((dist, i, j))

    dists.sort()
    for dist in dists:



if __name__ == "__main__":
    N = int(input())
    planets = [list(map(int, input().split())) for _ in range(N)]
    parents = defaultdict(int)

