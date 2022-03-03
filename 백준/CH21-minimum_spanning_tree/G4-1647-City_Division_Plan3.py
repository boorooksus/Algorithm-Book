"""
heapq 대신 list 이용
"""
from sys import stdin
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


def mst(n: int, graph: List[tuple]) -> int:
    cost = 0
    graph.sort()

    for w, a, b in graph:
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
    graph = []

    for _ in range(m):
        a, b, w = map(int, input().split())
        graph.append((w, a, b))

    print(mst(n, graph))


if __name__ == "__main__":
    main()
