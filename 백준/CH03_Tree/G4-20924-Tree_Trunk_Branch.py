from sys import stdin, setrecursionlimit
from collections import defaultdict
setrecursionlimit(10 ** 9)


input = lambda: stdin.readline().rstrip()


def dfs(prev: int, cur: int) -> int:
    if len(graph[cur]) == 1:
        return 0

    res = 0
    for child in graph[cur]:
        if child[0] == prev:
            continue
        res = max(dfs(cur, child[0]) + child[1], res)
    return res


if __name__ == "__main__":
    N, R = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(N - 1):
        a, b, d = map(int, input().split())
        graph[a].append((b, d))
        graph[b].append((a, d))

    trunk = 0
    prev, node = 0, R
    if len(graph[node]) != 2:
        while len(graph[node]) <= 2:
            for next in graph[node]:
                if next[0] != prev:
                    trunk += next[1]
                    prev, node = node, next[0]
                    break
            else:
                break

    branch = dfs(prev, node)

    print(trunk, branch)

