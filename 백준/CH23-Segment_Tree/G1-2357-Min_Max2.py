"""
반복문을 이용한 세그먼트 트리
"""
from sys import stdin
from math import ceil, log2


INF = 100001


def init():
    for i in range(N):
        tree[N + i] = (arr[i], arr[i])

    for i in range(N - 1, 0, -1):
        l, r = tree[i << 1], tree[i << 1 | 1]
        tree[i] = (min(l[0], r[0]), max(l[1], r[1]))


def update(idx, val):
    tree[N + idx] = (val, val)

    i = N + idx
    while i > 1:
        tree[i >> 1] = (min(tree[i][0], tree[i + 1][0]),
                        max(tree[i][1], tree[i + 1][1]))
        i >>= 1


def query(left, right):
    left += N
    right += N
    res = [INF, -INF]

    while left < right:
        if left & 1:
            res[0] = min(tree[left][0], res[0])
            res[1] = max(tree[left][1], res[1])
            left += 1
        if right & 1:
            right -= 1
            res[0] = min(tree[right][0], res[0])
            res[1] = max(tree[right][1], res[1])
        left >>= 1
        right >>= 1

    return res


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M = map(int, input().split())
    arr = [int(input()) for _ in range(N)]

    tree = list((0, 0) for _ in range(1 << (int(ceil(log2(N))) + 1)))
    init()
    for _ in range(M):
        a, b = map(int, input().split())
        res = query(a - 1, b)
        print("%d %d" % (res[0], res[1]))
