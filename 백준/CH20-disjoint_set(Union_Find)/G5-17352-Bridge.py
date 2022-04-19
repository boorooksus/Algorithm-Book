from sys import stdin
from collections import defaultdict


parents = defaultdict(int)


def find(x: int) -> int:
    if parents[x] == 0 or parents[x] == x:
        parents[x] = x
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    N = int(input())
    for _ in range(N - 2):
        a, b = map(int, input().split())
        union(a, b)

    a = find(1)
    for i in range(2, N + 1):
        b = find(i)
        if a != b:
            print("%d %d" % (a, b))
            exit(0)
