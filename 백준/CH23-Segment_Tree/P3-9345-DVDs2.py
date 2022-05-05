"""
틀림, 고쳐도 시간초과 발생할 수 있음
반복문을 이용한 세그먼트 트리 구현해야함
"""
from sys import stdin
from math import ceil, log2
from typing import List


INF = 100001


def init(node, start, end) -> List[int]:
    if start == end:
        tree[node] = [start, start, start]
        return tree[node]

    mid = start + (end - start) // 2
    l = init(2 * node, start, mid)
    r = init(2 * node + 1, mid + 1, end)
    tree[node] = [l[0] + r[0], min(l[1], r[1]), max(l[2], r[2])]

    return tree[node]


def update(node, start, end, a, b) -> List[int]:
    if start == end:
        return tree[node]

    mid = start + (end - start) // 2

    if a < start <= b <= end:
        tree[node][0] += arr[a] - arr[b]
        l = update(2 * node, start, mid, a, b)
        r = update(2 * node + 1, mid + 1, end, a, b)
        tree[node][1] = min(l[1], r[1])
        tree[node][2] = max(l[2], r[2])
        return tree[node]

    if start <= a <= end < b:
        tree[node][0] += arr[b] - arr[a]
        l = update(2 * node, start, mid, a, b)
        r = update(2 * node + 1, mid + 1, end, a, b)
        tree[node][1] = min(l[1], r[1])
        tree[node][2] = max(l[2], r[2])
        return tree[node]

    if start <= a and b <= end:
        l = update(2 * node, start, mid, a, b)
        r = update(2 * node + 1, mid + 1, end, a, b)
        tree[node][1] = min(l[1], r[1])
        tree[node][2] = max(l[2], r[2])
        return tree[node]

    else:
        return tree[node]


def query(node, start, end, left, right) -> List[int]:
    if right < start or end < left:
        return [0, INF, -INF]
    if left <= start and end <= right:
        return tree[node]

    mid = start + (end - start) // 2
    l = query(2 * node, start, mid, left, right)
    r = query(2 * node + 1, mid + 1, end, left, right)
    return [l[0] + r[0], min(l[1], r[1]), max(l[2], r[2])]


def get_sum(start, end) -> int:
    return (end * (end + 1) // 2) - (start * (start - 1) // 2)


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        arr = list(i for i in range(N))
        tree = list([0, 0, 0] for _ in range(1 << (int(ceil(log2(N))) + 1)))
        init(1, 0, N - 1)

        for _ in range(K):
            Q, A, B = map(int, input().split())

            if Q == 0:
                update(1, 0, N - 1, A, B)
                arr[A], arr[B] = arr[B], arr[A]
            else:
                res = query(1, 0, N - 1, A, B)
                temp = get_sum(A, B)
                print(["NO", "YES"][res[0] == temp and res[1] == A and res[2] == B])
