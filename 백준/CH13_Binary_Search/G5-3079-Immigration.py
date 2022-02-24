"""
시간 초과
"""
from sys import stdin
from heapq import heappop, heappush


def main():
    n, m = map(int, stdin.readline().split())
    t = [int(stdin.readline()) for _ in range(n)]

    hq = []
    for i, time in enumerate(t):
        heappush(hq, [time, i])

    res = 0
    while m > 0:
        time, idx = heappop(hq)
        heappush(hq, [time + t[idx], idx])
        res = time
        m -= 1

    print(res)


if __name__ == "__main__":
    main()
