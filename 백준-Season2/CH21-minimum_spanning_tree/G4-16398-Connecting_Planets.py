from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


def find(x: int) -> int:
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x: int, y: int) -> None:
    x, y = find(x), find(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


def mst() -> int:
    ans = 0
    while hq:
        cost, a, b = heappop(hq)
        a, b = find(a), find(b)
        if a != b:
            union(a, b)
            ans += cost

    return ans


if __name__ == "__main__":
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]

    parents = [i for i in range(N)]
    hq = []
    for i in range(N):
        for j in range(i + 1, N):
            heappush(hq, (costs[i][j], i, j))

    print(mst())
