"""
풀이 출처: https://mangu.tistory.com/67
세그먼트 트리에서 수의 개수 저장

"""
from sys import stdin
from math import log2, ceil


MAXN = 2_000_000


def update(node, start, end, idx):
    if idx < start or end < idx:
        return

    tree[node] += 1
    if start == end:
        return

    mid = start + (end - start) // 2
    update(2 * node, start, mid, idx)
    update(2 * node + 1, mid + 1, end, idx)


def query(node, start, end, k):
    tree[node] -= 1

    if start == end:
        return start

    mid = start + (end - start) // 2
    if k <= tree[2 * node]:
        return query(node << 1, start, mid, k)
    else:
        return query(node << 1 | 1, mid + 1, end, k - tree[node * 2])


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N = int(input())
    tree = [0] * (1 << (int(ceil(log2(MAXN))) + 1))

    for _ in range(N):
        T, X = map(int, input().split())
        if T == 1:
            update(1, 1, MAXN, X)
        else:
            print(query(1, 1, MAXN, X))
