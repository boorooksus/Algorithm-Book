from sys import stdin, setrecursionlimit
from math import ceil, log
setrecursionlimit(10 ** 9)


def init(start, end, idx):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]

    mid = start + (end - start) // 2
    tree[idx] = init(start, mid, idx * 2) + init(mid + 1, end, idx * 2 + 1)
    return tree[idx]


def update(start, end, idx, k, diff):
    if k < start or k > end:
        return

    tree[idx] += diff

    if start != end:
        mid = start + (end - start) // 2
        update(start, mid, idx * 2, k, diff)
        update(mid + 1, end, idx * 2 + 1, k, diff)


def query(start, end, idx, left, right):
    if end < left or right < start:
        return 0

    elif left <= start and end <= right:
        return tree[idx]

    mid = start + (end - start) // 2
    return query(start, mid, idx * 2, left, right) + query(mid + 1, end, idx * 2 + 1, left, right)


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()


    N, M, K = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    tree = [0] * (1 << (int(ceil(log(N, 2))) + 1))
    init(0, N - 1, 1)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(0, N - 1, 1, b - 1, c - arr[b - 1])
            arr[b - 1] = c
        else:
            print(query(0, N - 1, 1, b - 1, c - 1))
