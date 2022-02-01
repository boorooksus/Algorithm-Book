import sys
from collections import defaultdict
import heapq


def input():
    return sys.stdin.readline().strip()


parents = []


def main():
    global parents

    v, e = map(int, input().split())

    parents = [i for i in range(v + 1)]
    graph = defaultdict(list)
    hq = []

    for _ in range(e):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        heapq.heappush(hq, (w, a, b))

    res = 0
    while hq:
        w, a, b = heapq.heappop(hq)

        if get_parent(a) != get_parent(b):
            union_parent(a, b)
            res += w

    print(res)


def get_parent(x: int) -> int:
    if parents[x] == x:
        return x
    else:
        parents[x] = get_parent(parents[x])
        return parents[x]


def union_parent(x: int, y: int) -> None:
    x, y = get_parent(x), get_parent(y)
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


if __name__ == "__main__":
    main()
