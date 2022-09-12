"""
다익스트라
통과
플로이드 와샬 풀이보다 더 빠름
"""
import sys
from heapq import heappush, heappop
from collections import defaultdict
input = lambda: sys.stdin.readline().rstrip()


INF = 2001


def dijkstra(start: int) -> None:
    dists = [INF] * (N + 1)
    hq = [(0, start)]

    while hq:
        dist, node = heappop(hq)
        if dists[node] < dist:
            continue

        for next in graph[node]:
            if dist + 1 < dists[next]:
                dists[next] = dist + 1
                heappush(hq, (dist + 1, next))

    for i in range(1, N + 1):
        if i != start and dists[i] != INF:
            cnt[i] += 1
            cnt[start] += 1


if __name__ == "__main__":
    N = int(input())
    M = int(input())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)

    cnt = [0] * (N + 1)
    for i in range(1, N + 1):
        dijkstra(i)

    for i in range(1, N + 1):
        print(N - cnt[i] - 1)
