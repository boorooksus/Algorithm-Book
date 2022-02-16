from sys import stdin
import heapq
from collections import defaultdict
from typing import List


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


def mst(n: int, hq: List[int]) -> int:
    res = 0

    while hq:
        w, a, b = heapq.heappop(hq)

        if find(a) != find(b):
            res += w
            union(a, b)

    return res


def main():
    def input():
        return stdin.readline()

    n, m = int(input()), int(input())
    hq = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        heapq.heappush(hq, (w, a, b))

    print(mst(n, hq))


if __name__ == "__main__":
    main()
