from sys import stdin
from collections import defaultdict


graph = defaultdict(list)
visit = []
res = 0


def main():
    def input():
        return stdin.readline().rstrip()

    global graph, visit, res

    v = int(input())

    visit = [False] * (v + 1)

    for _ in range(v):
        line = list(map(int, input().split()))
        for i in range(1, len(line) - 1, 2):
            graph[line[0]].append((line[i], line[i + 1]))

    x = dfs(1)
    res = max(x, res)
    print(res)


def dfs(node) -> int:
    global graph, visit, res

    visit[node] = True
    radii = []
    for neighbor, dist in graph[node]:
        if not visit[neighbor]:
            radii.append(dist + dfs(neighbor))

    if not radii:
        return 0

    radii.sort(reverse=True)

    if len(radii) > 1:
        res = max(res, radii[0] + radii[1])

    return max(radii)


if __name__ == "__main__":
    main()
