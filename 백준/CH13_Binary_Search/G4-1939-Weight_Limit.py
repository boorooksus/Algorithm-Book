"""
다익스트라
"""
from sys import stdin, maxsize
from heapq import heappush, heappop
from collections import defaultdict


def dijkstra(start: int, end: int, graph: defaultdict) -> int:
    weights = defaultdict(int)
    hq = [(-maxsize, start)]

    while hq:
        weight, node = heappop(hq)
        if -weight < weights[node]:
            continue

        for neighbor, w in graph[node]:
            temp = min(-weight, w)
            if temp > weights[neighbor]:
                heappush(hq, (-temp, neighbor))
                weights[neighbor] = temp

    return weights[end]


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append((b, w))
        graph[b].append((a, w))
    start, dest = map(int, stdin.readline().split())

    print(dijkstra(start, dest, graph))


if __name__ == "__main__":
    main()
