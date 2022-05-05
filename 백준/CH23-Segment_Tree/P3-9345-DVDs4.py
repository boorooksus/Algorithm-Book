"""
top-down 방식
통과
"""
from sys import stdin
from math import ceil, log2
from typing import List


INF = 100001


def init(node, start, end) -> List[int]:
    if start == end:
        tree[node] = [start, start]
        return tree[node]

    mid = start + (end - start) // 2
    l = init(2 * node, start, mid)
    r = init(2 * node + 1, mid + 1, end)
    tree[node] = [min(l[0], r[0]), max(l[1], r[1])]

    return tree[node]


def update(node, start, end, a, b) -> List[int]:
    if start == end:
        if start == a:
            tree[node] = [arr[b], arr[b]]
        elif start == b:
            tree[node] = [arr[a], arr[a]]
        return tree[node]

    mid = start + (end - start) // 2

    if a < start <= b <= end:
        l = update(2 * node, start, mid, a, b)
        r = update(2 * node + 1, mid + 1, end, a, b)
        tree[node][0] = min(l[0], r[0])
        tree[node][1] = max(l[1], r[1])
        return tree[node]

    if start <= a <= end < b:
        l = update(2 * node, start, mid, a, b)
        r = update(2 * node + 1, mid + 1, end, a, b)
        tree[node][0] = min(l[0], r[0])
        tree[node][1] = max(l[1], r[1])
        return tree[node]

    if start <= a and b <= end:
        l = update(2 * node, start, mid, a, b)
        r = update(2 * node + 1, mid + 1, end, a, b)
        return tree[node]

    else:
        return tree[node]


def query(node, start, end, left, right) -> List[int]:
    if right < start or end < left:
        return [INF, -INF]
    if left <= start and end <= right:
        return tree[node]

    mid = start + (end - start) // 2
    l = query(2 * node, start, mid, left, right)
    r = query(2 * node + 1, mid + 1, end, left, right)
    return [min(l[0], r[0]), max(l[1], r[1])]


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        arr = list(i for i in range(N))
        tree = list([0, 0] for _ in range(1 << (int(ceil(log2(N))) + 1)))
        init(1, 0, N - 1)

        for _ in range(K):
            Q, A, B = map(int, input().split())

            if Q == 0:
                update(1, 0, N - 1, A, B)
                arr[A], arr[B] = arr[B], arr[A]
            else:
                res = query(1, 0, N - 1, A, B)
                print(["NO", "YES"][res[0] == A and res[1] == B])
