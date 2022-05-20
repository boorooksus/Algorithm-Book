"""
메모리 초과
"""
from sys import stdin
from collections import defaultdict
from heapq import heappush, heappop


input = lambda: stdin.readline().rstrip()


def topology_sort():
    hq = [(0, start, [])]

    while True:
        total, node, cnt = heappop(hq)

        if node == end:
            return total, len(set(cnt))

        for neighbor, dist in graph[node]:
            indegrees[neighbor] -= 1
            cnts[neighbor][total + dist] += cnt + [(node, neighbor)]

            if indegrees[neighbor] == 0:
                heappush(hq, (total + dist, neighbor, cnts[neighbor][total + dist]))


if __name__ == "__main__":
    n, m = (int(input()) for _ in range(2))
    graph, indegrees = defaultdict(list), defaultdict(int)
    cnts = list(list([] for _ in range(10000)) for _ in range(n + 1))
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        indegrees[b] += 1
    start, end = map(int, input().split())

    print("%d\n%d" % topology_sort())


