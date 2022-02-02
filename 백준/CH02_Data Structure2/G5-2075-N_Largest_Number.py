from sys import stdin
from bisect import bisect_right
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        temp = list(map(int, input().split()))
        for j in range(n):
            arr[j][i] = temp[j]

    print(get_n_largest(arr, n))


def get_n_largest(arr, n):
    window = deque(arr[0])

    for row in range(1, n):
        for col in range(n - 1, -1, -1):
            idx = bisect_right(window, arr[row][col])

            if idx > 0:
                window.insert(idx, arr[row][col])
                window.popleft()
            else:
                break

    return window[0]


if __name__ == "__main__":
    main()
