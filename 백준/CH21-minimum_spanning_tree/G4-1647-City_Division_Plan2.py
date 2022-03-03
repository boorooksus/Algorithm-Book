"""
parents 자료구조를 해쉬 테이블로 변경
"""
from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
from typing import List


parents = defaultdict(int)


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


def mst(n: int, hq: List[int]) -> int:
    cost = 0

    while hq:
        w, a, b = heappop(hq)
        a, b = find(a), find(b)
        if a == b:
            continue

        union(a, b)
        cost += w
        n -= 1

        if n == 2:
            break

    return cost


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    hq = []

    for _ in range(m):
        a, b, w = map(int, input().split())
        heappush(hq, (w, a, b))

    print(mst(n, hq))


if __name__ == "__main__":
    main()
