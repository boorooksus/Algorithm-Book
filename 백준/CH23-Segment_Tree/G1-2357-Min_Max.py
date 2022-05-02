from sys import stdin, setrecursionlimit
from typing import List
setrecursionlimit(10 ** 9)


INF = int(1e9)


def init(node, start, end) -> List[int]:
    if start == end:
        tree[node][0] = arr[start]
        tree[node][1] = arr[start]
        return tree[node]

    mid = start + (end - start) // 2
    x = init(2 * node, start, mid)
    y = init(2 * node + 1, mid + 1, end)
    tree[node] = [min(x[0], y[0]), max(x[1], y[1])]
    return tree[node]


def find(node, start, end, left, right) -> List[int]:
    if end < left or right < start:
        return [INF, -INF]

    elif left <= start and end <= right:
        return tree[node]

    else:
        mid = start + (end - start) // 2
        x = find(2 * node, start, mid, left, right)
        y = find(2 * node + 1, mid + 1, end, left, right)
        return [min(x[0], y[0]), max(x[1], y[1])]


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    tree = list([0, 0] for _ in range(400001))
    init(1, 0, N - 1)
    for _ in range(M):
        a, b = map(int, input().split())
        res = find(1, 0, N - 1, a - 1, b - 1)
        print("%d %d" % (res[0], res[1]))
