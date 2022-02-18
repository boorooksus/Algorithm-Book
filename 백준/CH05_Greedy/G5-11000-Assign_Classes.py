from sys import stdin
from heapq import heappop, heappush


def main():
    def input():
        return stdin.readline()

    n = int(input())
    times = []

    for _ in range(n):
        times.append(list(map(int, input().split())))

    times.sort()
    hq = []
    heappush(hq, times[0][1])

    for i in range(1, n):
        if hq[0] <= times[i][0]:
            heappop(hq)
        heappush(hq, times[i][1])

    print(len(hq))


if __name__ == "__main__":
    main()
