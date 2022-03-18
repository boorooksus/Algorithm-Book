"""
메모리초과
"""
from sys import stdin
from collections import defaultdict
from typing import List


def dfs(node, graph, cnts) -> int:
    if cnts[node]:
        return cnts[node]

    cnt = 0
    for neighbor in graph[node]:
        cnt += 1 + dfs(neighbor, graph, cnts)

    cnts[node] = cnt
    return cnts[node]


def main():
    def input():
        return stdin.readline().rstrip()

    n, m = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(m):
        a, b = map(int, input().split())
        graph[b].append(a)

    cnts = defaultdict(int)
    res = []
    max_cnt = 0
    for i in range(1, n + 1):
        cnts[i] = dfs(i, graph, cnts)
        if cnts[i] > max_cnt:
            max_cnt = cnts[i]
            res = [i]
        elif cnts[i] == max_cnt:
            res.append(i)

    print(*sorted(res), sep=' ')


if __name__ == "__main__":
    main()
