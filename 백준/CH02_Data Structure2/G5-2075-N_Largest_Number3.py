import heapq
from sys import stdin


def main():
    def input():
        return stdin.readline().rstrip()

    n = int(input())
    hq = []
    for _ in range(n):
        row = list(map(int, input().split()))

        if not hq:
            for num in row:
                heapq.heappush(hq, num)
        else:
            for num in row:
                if num > hq[0]:
                    heapq.heappop(hq)
                    heapq.heappush(hq, num)

    print(heapq.heappop(hq))


if __name__ == "__main__":
    main()
