"""
시간 초과
"""
from sys import stdin
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()


def disjoint(x: int, y: int) -> int:
    graph[x].remove(y)
    graph[y].remove(x)
    return bfs(x, y) * bfs(y, x)


def bfs(x: int, y: int) -> int:
    cnt = 0
    dq = deque([x])
    visit = [False] * (N + 1)
    visit[x] = True

    while dq:
        node = dq.popleft()
        if node == y:
            return 0
        cnt += 1
        for neighbor in graph[node]:
            if not visit[neighbor]:
                visit[neighbor] = True
                dq.append(neighbor)

    return cnt


if __name__ == "__main__":
    N, M, Q = map(int, input().split())
    parents = defaultdict(int)
    graph = defaultdict(list)
    cxns = [tuple(map(int, input().split())) for _ in range(M)]
    for a, b in cxns:
        graph[a].append(b)
        graph[b].append(a)
    ans = 0
    for _ in range(Q):
        a = int(input())
        ans += disjoint(*cxns[a - 1])
    print(ans)

