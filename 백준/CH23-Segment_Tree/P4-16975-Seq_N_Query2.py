"""
lazy propagation을 문제에 맞게 적용
query함수에서 인자로 범위가 아닌 인덱스 하나만 받음
"""
from sys import stdin
from math import log2, ceil


def init(node, start, end) -> int:
    if start == end:
        tree[node] = arr[start]

    else:
        mid = start + (end - start) // 2
        tree[node] = init(2 * node, start, mid) + \
                     init(2 * node + 1, mid + 1, end)
    return tree[node]


def propagation(node, start, end) -> None:
    if lazy[node] == 0:
        return

    tree[node] += (end - start + 1) * lazy[node]
    if start != end:
        lazy[2 * node] += lazy[node]
        lazy[2 * node + 1] += lazy[node]
    lazy[node] = 0


def update(node, start, end, left, right, val) -> None:
    propagation(node, start, end)

    if right < start or end < left:
        return

    if left <= start and end <= right:
        tree[node] += (end - start + 1) * val
        if start != end:
            lazy[2 * node] += val
            lazy[2 * node + 1] += val
        return

    mid = start + (end - start) // 2
    update(2 * node, start, mid, left, right, val)
    update(2 * node + 1, mid + 1, end, left, right, val)
    tree[node] = tree[2 * node] + tree[2 * node + 1]


def query(node, start, end, idx) -> int:
    propagation(node, start, end)

    if idx < start or end < idx:
        return 0

    if start == end == idx:
        return tree[node]

    mid = start + (end - start) // 2
    return query(2 * node, start, mid, idx) + \
           query(2 * node + 1, mid + 1, end, idx)


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N = int(input())
    arr = list(map(int, input().split()))
    tree = [0] * (1 << (int(ceil(log2(N))) + 1))
    lazy = [0] * len(tree)
    init(1, 0, N - 1)

    M = int(input())
    for _ in range(M):
        args = list(map(int, input().split()))
        if args[0] == 1:
            update(1, 0, N - 1, args[1] - 1, args[2] - 1, args[3])
        else:
            print(query(1, 0, N - 1, args[1] - 1))
