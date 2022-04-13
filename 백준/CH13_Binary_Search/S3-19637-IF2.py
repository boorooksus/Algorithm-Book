from sys import stdin
from typing import List


def binary_search(seq: List, x: int) -> str:
    start, end = 0, len(seq) - 1
    res = 0
    while start <= end:
        mid = start + (end - start) // 2
        if int(seq[mid][1]) >= x:
            end = mid - 1
            res = mid
        else:
            start = mid + 1

    return seq[res][0]


if __name__ == "__main__":
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    powers = [tuple(input().split()) for _ in range(n)]

    for _ in range(m):
        print(binary_search(powers, int(input())))

