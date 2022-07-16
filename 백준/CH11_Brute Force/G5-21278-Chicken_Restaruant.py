"""
bfs + brute force
통과
"""
from sys import stdin
from collections import defaultdict, deque
input = lambda: stdin.readline().rstrip()


def bfs(x: int, y: int) -> int:
    dq = deque([(0, x), (0, y)])
    visit = [False] * (N + 1)
    visit[x], visit[y] = True, True

    res = 0
    while dq:
        dist, node = dq.popleft()
        for next in graph[node]:
            if not visit[next]:
                visit[next] = True
                res += dist + 1
                dq.append((dist + 1, next))
    return res * 2


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    res = [0, 0, 100000]
    for i in range(1, N):
        for j in range(i + 1, N + 1):
            temp = bfs(i, j)
            if temp < res[2]:
                res = [i, j, temp]
    print(*res)
