from sys import stdin
from heapq import heappop, heappush


def main():
    n, k = map(int, stdin.readline().split())
    heights = list(map(int, stdin.readline().split()))

    if k == n:
        print(0)
        return

    hq = []
    for i in range(1, n):
        heappush(hq, -(heights[i] - heights[i - 1]))

    res = heights[-1] - heights[0]
    for i in range(k - 1):
        res -= -heappop(hq)

    print(res)


if __name__ == "__main__":
    main()
