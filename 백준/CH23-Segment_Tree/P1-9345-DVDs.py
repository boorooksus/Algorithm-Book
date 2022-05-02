"""
틀림
반례: 2~4 선반에 1, 3, 5 DVD가 있는 경우에도 YES 출력
세그먼트 트리를 누적합이 아닌 최대, 최소로 바꿔야함.
"""
from sys import stdin
from math import ceil, log2


def init(node, start, end) -> int:
    if start == end:
        tree[node] = start
        return tree[node]

    mid = start + (end - start) // 2
    tree[node] = init(2 * node, start, mid) + \
                 init(2 * node + 1, mid + 1, end)
    return tree[node]


def update(node, start, end, a, b) -> None:
    if start == end:
        return

    mid = start + (end - start) // 2

    if a < start <= b <= end:
        tree[node] += arr[a] - arr[b]
        update(2 * node, start, mid, a, b)
        update(2 * node + 1, mid + 1, end, a, b)
        return

    if start <= a <= end < b:
        tree[node] += arr[b] - arr[a]
        update(2 * node, start, mid, a, b)
        update(2 * node + 1, mid + 1, end, a, b)
        return

    if start <= a and b <= end:
        update(2 * node, start, mid, a, b)
        update(2 * node + 1, mid + 1, end, a, b)
        return

    else:
        return


def query(node, start, end, left, right) -> int:
    if right < start or end < left:
        return 0
    if left <= start and end <= right:
        return tree[node]

    mid = start + (end - start) // 2
    return query(2 * node, start, mid, left, right) + \
            query(2 * node + 1, mid + 1, end, left, right)


def get_sum(start, end) -> int:
    return (end * (end + 1) // 2) - (start * (start - 1) // 2)


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    T = int(input())
    for _ in range(T):
        N, K = map(int, input().split())
        arr = list(i for i in range(N))
        tree = [0] * (1 << (int(ceil(log2(N))) + 1))
        init(1, 0, N - 1)

        for _ in range(K):
            Q, A, B = map(int, input().split())

            if Q == 0:
                update(1, 0, N - 1, A, B)
                arr[A], arr[B] = arr[B], arr[A]
            else:
                res = query(1, 0, N - 1, A, B)
                print(["NO", "YES"][res == get_sum(A, B)])
