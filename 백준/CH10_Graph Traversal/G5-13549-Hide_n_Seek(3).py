from sys import stdin
from collections import defaultdict, deque
from heapq import heappush, heappop


def dijkstra() -> int:
    visit = defaultdict(bool)
    hq = [(0, n)]

    while hq:
        time, cur = heappop(hq)
        visit[cur] = True

        if cur == k:
            return time

        if cur > 0 and not visit[cur - 1]:
            heappush(hq, (time + 1, cur - 1))
        if cur < 1000000 and not visit[cur + 1]:
            heappush(hq, (time + 1, cur + 1))
        if cur <= 500000 and not visit[2 * cur]:
            heappush(hq, (time, 2 * cur))

    return 0


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    print(dijkstra())

