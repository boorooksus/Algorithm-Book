from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
input = lambda: stdin.readline().rstrip()
INF = 1_000_000


def dijkstra(start: int, end: int) -> int:
    if start == end:
        return 0

    cost = [INF] * (N + 1)
    hq = [(0, start)]
    while hq:
        c, node = heappop(hq)
        if c > cost[node]:
            continue
        for next, t in graph[node]:
            if c + t < cost[next]:
                cost[next] = c + t
                heappush(hq, (c + t, next))

    return cost[end]


if __name__ == "__main__":
    N, M, X = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b, t = map(int, input().split())
        graph[a].append((b, t))

    time = [0] * (N + 1)
    for i in range(1, N + 1):
        time[i] += dijkstra(i, X)
        time[i] += dijkstra(X, i)

    print(max(time))
