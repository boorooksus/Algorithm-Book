import sys
from collections import defaultdict
from typing import List


def input():
    return sys.stdin.readline().strip()


n = 0
graph = defaultdict(list)
visit = []
res = [[]]


def dfs(x: int) -> List[int]:
    global n, graph, visit, res

    # if visit[x]:
    #     return [x]
    #
    # visit[x] = True

    nodes = []
    for neighbor in graph[x]:
        if not visit[neighbor]:
            visit[neighbor] = True
            nodes += dfs(neighbor)
            visit[neighbor] = False

    for node in nodes:
        res[x][node] = 1

    return list(set([x] + nodes))


def main():
    global n, graph, visit, res

    n = int(input())
    for i in range(n):
        row = list(map(int, input().split()))
        for j in range(len(row)):
            if row[j]:
                graph[i].append(j)

    visit = [False] * n
    res = list([0] * n for _ in range(n))
    for i in range(n):
        dfs(i)

    for i in range(n):
        print(*res[i])


if __name__ == "__main__":
    main()
