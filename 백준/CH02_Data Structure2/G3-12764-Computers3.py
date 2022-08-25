from sys import stdin
from heapq import heappop, heappush
input = lambda: stdin.readline().rstrip()


INF = 1000001


if __name__ == "__main__":
    N = int(input())
    time = list(list(map(int, input().split())) for _ in range(N))

    time.sort()
    hq, available = [(INF, 0)], []
    cnt = 0
    counter = {}
    for start, end in time:
        while hq[0][0] <= start:
            e, n = heappop(hq)
            heappush(available, (n, e))

        if available:
            n, e = heappop(available)
            counter[n] += 1
            heappush(hq, (end, n))

        else:
            cnt += 1
            counter[cnt] = 1
            heappush(hq, (end, cnt))

    print(cnt)
    for i in range(1, cnt + 1):
        print(counter[i], end=' ')
