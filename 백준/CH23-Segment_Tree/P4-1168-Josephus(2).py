from sys import stdin
from math import ceil, log2


input = lambda: stdin.readline().rstrip()


def init(node, start, end):
    if start == end:
        tree[node] = 1
        return tree[node]

    mid = start + (end - start) // 2
    tree[node] = init(node << 1, start, mid) + init(node << 1 | 1, mid + 1, end)
    return tree[node]


def query(node, start, end, k):
    tree[node] -= 1

    if start == end:
        return start

    mid = start + (end - start) // 2
    if k <= mid:
        return query(node << 1, start, mid, k)
    else:
        return query(node << 1 | 1, mid + 1, end, k)


if __name__ == "__main__":
    N, K = map(int, input().split())

    tree = [0] * (1 << (int(ceil(log2(N))) + 1))
    init(1, 1, N)

    ans = []
    while N > 0:
        if K > N:
            K %= N
        ans.append(query(1, 1, N, K))
        N -= 1

    print("<", end='')
    print(*ans, sep=', ', end='')
    print(">")


