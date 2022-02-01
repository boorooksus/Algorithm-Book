import sys
import heapq
from collections import defaultdict


def input():
    return sys.stdin.readline().strip()


n = 0
graph = defaultdict(list)
res = [[]]
INF = sys.maxsize


def dijkstra(x: int) -> None:
    hq = []
    heapq.heappush(hq, (0, x))
    while hq:
        dist, node = heapq.heappop(hq)

        if dist > res[x][node]:
            continue

        for neighbor in graph[node]:
            if res[x][neighbor] > dist + 1:
                res[x][neighbor] = dist + 1
                heapq.heappush(hq, (res[x][neighbor], neighbor))


def main():
    global n, graph, res

    n = int(input())
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            if row[j]:
                graph[i].append(j)

    res = [[INF for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dijkstra(i)

    for i in range(n):
        for j in range(n):
            print(1 if res[i][j] != INF or i == j else 0, end=' ')
        print()


if __name__ == "__main__":
    main()
