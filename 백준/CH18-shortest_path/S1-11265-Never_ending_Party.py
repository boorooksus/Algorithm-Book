"""
다익스트라
python 시간초과 pypy 통과
"""
from sys import stdin
from typing import List
from heapq import heappop, heappush


n: int
m: int
graph: List[List[int]]


def dijkstra(start: int, dest: int, time: int) -> bool:
    if graph[start][dest] <= time:
        return True

    hq = [(0, start)]

    while hq:
        dist, node = heappop(hq)
        if dist > time:
            return False

        if dist > graph[start][node]:
            continue

        for neighbor in range(1, n + 1):
            if neighbor == node:
                continue
            if dist + graph[node][neighbor] < graph[start][neighbor]:
                graph[start][neighbor] = dist + graph[node][neighbor]
                heappush(hq, (graph[start][neighbor], neighbor))
            if neighbor == dest and graph[start][neighbor] <= time:
                return True

    return False


def main():
    def input():
        return stdin.readline().rstrip()
    global n, m, graph

    n, m = map(int, input().split())
    graph = [[0] * (n + 1)] + \
            [[0] + list(map(int, input().split())) for _ in range(n)]

    for _ in range(m):
        a, b, c = map(int, input().split())
        if dijkstra(a, b, c):
            print("Enjoy other party")
        else:
            print("Stay here")


if __name__ == "__main__":
    main()
