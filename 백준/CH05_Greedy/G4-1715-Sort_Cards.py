from sys import stdin
from heapq import heappop, heappush, heapify


input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    cards = list(int(input()) for _ in range(N))

    heapify(cards)
    res = 0
    while len(cards) > 1:
        a = heappop(cards)
        b = heappop(cards)
        res += a + b
        heappush(cards, a + b)

    print(res)
