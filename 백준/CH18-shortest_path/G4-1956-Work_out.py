"""
시간초과
"""
from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop


input = lambda: stdin.readline().rstrip()
MAX = 4_000_000


def cycle(start: int) -> int:
    hq = [(start, 0)]
    visit = [False] * (V + 1)

    while hq:
        node, total = heappop(hq)
        visit[node] = True

        if total > ans:
            return MAX

        if node == start and total > 0:
            return total

        for neighbor, dist in graph[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                heappush(hq, (neighbor, total + dist))

    return MAX


if __name__ == "__main__":
    V, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))

    ans = MAX
    for i in range(1, V + 1):
        ans = min(cycle(i), ans)

    print([ans, -1][ans == MAX])
