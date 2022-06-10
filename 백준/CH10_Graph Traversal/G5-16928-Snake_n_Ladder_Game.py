from sys import stdin
from collections import defaultdict, deque


input = lambda: stdin.readline().rstrip()


def bfs(start: int, end: int) -> int:
    dq = deque([(start, 0)])
    visit = defaultdict(int)

    while dq:
        cur, move = dq.popleft()

        if graph[cur] == 0:
            move += 1
            for i in range(1, 7):
                nxt = cur + i
                if nxt > end:
                    nxt = end
                if visit[nxt] != 0 and move > visit[nxt]:
                    continue
                visit[nxt] = move
                dq.append((nxt, move))
        else:
            nxt = graph[cur]
            if nxt > end:
                nxt = end
            if visit[nxt] != 0 and move > visit[nxt]:
                continue
            visit[nxt] = move
            dq.append((nxt, move))

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
