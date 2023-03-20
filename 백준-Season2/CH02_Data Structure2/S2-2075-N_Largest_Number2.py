from sys import stdin
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())

    hq = []
    for _ in range(N):
        row = list(map(int, input().split()))

        if not hq:
            for num in row:
                heappush(hq, num)
        else:
            for num in row:
                if num > hq[0]:
                    heappop(hq)
                    heappush(hq, num)

    print(hq[0])
