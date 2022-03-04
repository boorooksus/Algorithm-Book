from sys import stdin
from heapq import heappop, heappush


def main():
    n = int(stdin.readline())
    towers = list(map(int, stdin.readline().split()))

    res = [0] * n
    hq = []
    for i in range(n - 1, -1, -1):
        while hq and hq[0][0] < towers[i]:
            t, idx = heappop(hq)
            res[idx] = i + 1

        heappush(hq, (towers[i], i))

    print(*res, sep=' ')


if __name__ == "__main__":
    main()
