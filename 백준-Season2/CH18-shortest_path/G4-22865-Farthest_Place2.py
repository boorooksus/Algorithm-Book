from sys import stdin
from heapq import heappush, heappop
from collections import defaultdict
input = lambda: stdin.readline().rstrip()


INF = int(1e9)


def dijkstra(start: int) -> None:
    res = [INF] * (N + 1)
    res[start] = 0
    hq = [(0, start)]

    while hq:
        dist, node = heappop(hq)

        if dist > res[node]:
            continue

        for nxt, d in graph[node]:
            if dist + d < res[nxt]:
                res[nxt] = dist + d
                heappush(hq, (dist + d, nxt))

    for i in range(1, N + 1):
        dists[i] = min(dists[i], res[i])


if __name__ == "__main__":
    N = int(input())
    friends = list(map(int, input().split()))
    M = int(input())

    graph = defaultdict(list)
    for _ in range(M):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    dists = [INF] * (N + 1)
    for friend in friends:
        dijkstra(friend)

    ans, temp = 0, 0
    for i in range(1, N + 1):
        if dists[i] > temp:
            ans, temp = i, dists[i]

    print(ans)

"""
다익스트라 방식
"""