from sys import stdin
from collections import defaultdict


input = lambda: stdin.readline().rstrip()


def dfs(start: int) -> int:
    if visit[start]:
        return 0
    visit[start] = True
    for node in graph[start]:
        if d[node] == 0 or dfs(d[node]):
            d[node] = start
            return 1
    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    d = [0] * (M + 1)
    graph = defaultdict(list)
    for i in range(1, N + 1):
        jobs = list(map(int, input().split()))
        for j in range(1, len(jobs)):
            graph[i].append(jobs[j])

    ans = 0
    for i in range(1, N + 1):
        visit = [False] * (N + 1)
        ans += dfs(i)
    print(ans)
