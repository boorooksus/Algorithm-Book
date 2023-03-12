from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    confs = list(list(map(int, input().split())) for _ in range(N))

    confs.sort()
    hq = []
    for start, end in confs:
        if hq and hq[0] <= start:
            heappop(hq)
        heappush(hq, end)

    print(len(hq))
