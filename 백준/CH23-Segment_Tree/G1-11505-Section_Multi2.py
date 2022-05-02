from sys import stdin, setrecursionlimit
from math import log, ceil

setrecursionlimit(10 ** 9)

MOD = 1_000_000_007


def init(node, start, end):
    if start == end:
        tree[node] = arr[start]
        return tree[node]

    mid = start + (end - start) // 2
    tree[node] = (init(2 * node, start, mid) * init(2 * node + 1, mid + 1, end)) % MOD

    return tree[node]


def update(node, start, end, idx, val) -> None:
    if idx < start or idx > end:
        return

    if start == end:
        tree[node] = val

    else:
        mid = start + (end - start) // 2
        update(2 * node, start, mid, idx, val)
        update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = (tree[2 * node] * tree[2 * node + 1]) % MOD


def query(node, start, end, left, right):
    if right < start or end < left:
        return 1

    elif left <= start <= end <= right:
        return tree[node]

    mid = start + (end - start) // 2
    return (query(2 * node, start, mid, left, right) * query(2 * node + 1, mid + 1, end, left, right)) % MOD


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()


    N, M, K = map(int, input().split())

    arr = [0] + [int(input()) for _ in range(N)]
    tree = list(0 for _ in range((1 << (int(ceil(log(N, 2))) + 1))))
    init(1, 1, N)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 1, N, b, c)
            arr[b] = c
        else:
            print(query(1, 1, N, b, c))
