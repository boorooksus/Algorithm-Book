from sys import stdin
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()


def bfs(x: int) -> int:
    cnt = 0
    dq = deque([x])
    visit = defaultdict(bool)
    visit[x] = True

    while dq:
        node = dq.popleft()
        for nxt in graph[node]:
            if not visit[nxt]:
                visit[nxt] = True
                cnt += 1
                dq.append(nxt)

    return cnt


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(M):
        a, b = map(int, input().split())
        graph[b].append(a)
    X = int(input())
    print(bfs(X))

