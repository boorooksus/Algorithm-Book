from sys import stdin
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()


def bfs(start: int, end: int) -> int:
    dq = deque([(start, 0)])
    visit = defaultdict(bool)

    while dq:
        cur, move = dq.popleft()

        for i in range(1, 7):
            nxt = cur + i
            if graph[nxt]:
                nxt = graph[nxt]
            if nxt >= end:
                return move + 1
            if visit[nxt]:
                continue
            visit[nxt] = True
            dq.append((nxt, move + 1))

    return visit[end]


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = defaultdict(int)
    for _ in range(N):
        a, b = map(int, input().split())
        graph[a] = b
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a] = b

    print(bfs(1, 100))
