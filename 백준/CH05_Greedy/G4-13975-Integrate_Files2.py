from sys import stdin
from typing import List
from heapq import heappush, heappop, heapify


input = lambda: stdin.readline().rstrip()


def cal(arr: List[int]) -> int:
    res = 0
    while len(arr) > 1:
        a, b = heappop(arr), heappop(arr)
        res += a + b
        heappush(arr, a + b)

    return res


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        K = int(input())
        docs = list(map(int, input().split()))
        heapify(docs)
        print(cal(docs))
