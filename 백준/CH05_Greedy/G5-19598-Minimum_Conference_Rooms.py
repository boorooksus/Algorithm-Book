from sys import stdin
from heapq import heappush, heappop


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    times = [tuple(map(int, input().split())) for _ in range(n)]

    times.sort()
    hq = []
    for start, end in times:
        if not hq:
            heappush(hq, end)
        else:
            prev = heappop(hq)
            if start < prev:
                heappush(hq, prev)
            heappush(hq, end)
    print(len(hq))


if __name__ == "__main__":
    main()
