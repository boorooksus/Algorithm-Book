from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


def dfs(start: int) -> int:
    if visit[start]:
        return 0
    visit[start] = True

    for node in graph[start]:
        if d[node] == -1 or dfs(d[node]):
            d[node] = start
            return 1
    return 0


if __name__ == "__main__":
    N = int(input())
    sharks = list(list(map(int, input().split())) for _ in range(N))

    d = [-1] * N
    graph = defaultdict(list)
    for i in range(len(sharks)):
        for j in range(len(sharks)):
            if i == j:
                continue
            if sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1] \
                    and sharks[i][2] == sharks[j][2] and i > j:
                continue
            if sharks[i][0] >= sharks[j][0] and sharks[i][1] >= sharks[j][1] \
                    and sharks[i][2] >= sharks[j][2]:
                graph[i].append(j)

    for i in range(2):
        for j in range(N):
            visit = [False] * N
            dfs(j)

    print(d.count(-1))
