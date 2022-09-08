from sys import stdin
from collections import defaultdict
from typing import List
input = lambda: stdin.readline().rstrip()


def dfs(route: List[int]) -> bool:
    if len(route) == 5:
        return True

    for friend in graph[route[-1]]:
        if not visit[friend]:
            visit[friend] = True
            if dfs(route + [friend]):
                return True
            visit[friend] = False


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visit = [False] * N
    for i in range(N):
        visit[i] = True
        if dfs([i]):
            print(1)
            exit()
        visit[i] = False
    print(0)
