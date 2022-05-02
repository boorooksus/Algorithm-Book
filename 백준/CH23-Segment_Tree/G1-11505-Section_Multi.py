from sys import stdin, setrecursionlimit
from math import log, ceil

setrecursionlimit(10 ** 9)


def init(node, start, end):
    if start == end:
        tree[node][0] = arr[start]
        if arr[start] == 0:
            tree[node][1] = 1
            tree[node][0] = 1
        return tree[node]

    mid = start + (end - start) // 2
    left, right = init(2 * node, start, mid), init(2 * node + 1, mid + 1, end)
    tree[node][0] = left[0] * right[0]
    tree[node][1] = left[1] + right[1]

    return tree[node]


def update(node, start, end, idx, orig, new) -> None:
    if idx < start or idx > end:
        return

    if orig == 0:
        tree[node][1] -= 1
    else:
        tree[node][0] //= orig

    if new == 0:
        tree[node][1] += 1
    else:
        tree[node][0] *= new

    if start != end:
        mid = start + (end - start) // 2
        update(2 * node, start, mid, idx, orig, new)
        update(2 * node + 1, mid + 1, end, idx, orig, new)


def query(node, start, end, left, right):
    if right < start or end < left:
        return 1

    elif left <= start <= end <= right:
        return [0, tree[node][0]][tree[node][1] == 0]

    mid = start + (end - start) // 2
    return query(2 * node, start, mid, left, right) * \
           query(2 * node + 1, mid + 1, end, left, right)


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()


    N, M, K = map(int, input().split())

    arr = [0] + [int(input()) for _ in range(N)]
    tree = list([0, 0] for _ in range((1 << (int(ceil(log(N, 2))) + 1))))
    init(1, 1, N)

    for _ in range(M + K):
        a, b, c = map(int, input().split())
        if a == 1:
            update(1, 1, N, b, arr[b], c)
            arr[b] = c
        else:
            print(query(1, 1, N, b, c) % 1_000_000_007)
