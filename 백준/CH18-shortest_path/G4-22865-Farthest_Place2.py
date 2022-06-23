"""
다익스트라
통과
"""
from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop
from typing import List


input = lambda: stdin.readline().rstrip()
INF = 1_000_000_000


def dijkstra(start: int) -> List[int]:
    dists = [INF] * (N + 1)
    hq = [(0, start)]

    while hq:
        dist, node = heappop(hq)

        if dist > dists[node]:
            continue

        for next, nd in graph[node]:
            if dist + nd < dists[next]:
                dists[next] = dist + nd
                heappush(hq, (dists[next], next))

    return dists


if __name__ == "__main__":
    N = int(input())
    A, B, C = map(int, input().split())
    M = int(input())
    graph = defaultdict(list)
    for _ in range(M):
        D, E, L = map(int, input().split())
        graph[D].append((E, L))
        graph[E].append((D, L))

    a, b, c = dijkstra(A), dijkstra(B), dijkstra(C)
    ans, min_dist = 0, 0
    for i in range(1, N + 1):
        temp = min(a[i], b[i], c[i])
        if temp > min_dist:
            ans = i
            min_dist = temp

    print(ans)
