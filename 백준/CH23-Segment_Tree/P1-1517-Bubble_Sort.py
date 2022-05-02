from sys import stdin, setrecursionlimit
from math import log, ceil
setrecursionlimit(10 ** 9)


def update(node, start, end, idx) -> None:
    if start == end:
        tree[node] = 1
        return

    mid = start + (end - start) // 2
    if idx <= mid:
        update(2 * node, start, mid, idx)
    else:
        update(2 * node + 1, mid + 1, end, idx)
    tree[node] = tree[node * 2] + tree[2 * node + 1]


def query(node, start, end, left, right) -> int:
    if end < left or right < start:
        return 0

    elif left <= start and end <= right:
        return tree[node]

    else:
        mid = start + (end - start) // 2
        return query(2 * node, start, mid, left, right) + \
               query(2 * node + 1, mid + 1, end, left, right)


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N = int(input())
    temp = list(map(int, input().split()))
    arr = list([v, i] for i, v in enumerate(temp))
    arr.sort()
    tree = [0] * (1 << (int(ceil(log(N, 2))) + 1))

    ans = 0
    for i in range(N):
        ans += query(1, 0, N - 1, arr[i][1] + 1, N - 1)
        update(1, 0, N - 1, arr[i][1])
    print(ans)


"""
오름차순 정렬
-> 차례대로 각 원소에 대해 query 수행
-> 자신보다 값이 작으면서 인덱스가 큰 경우에 swap이 일어남 -> 구간합 구하기
-> update 수행

"""