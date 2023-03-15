from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()


def bfs() -> int:
    dq = deque([(1, 0)])  # location, count

    while dq:
        loc, cnt = dq.popleft()
        for i in range(1, 7):

            if loc + i >= 100:
                # 목적지 도착
                return cnt + 1

            if graph[loc + i] > 0:
                # 방문하지 않은 칸
                dq.append((graph[loc + i], cnt + 1))
                graph[loc + i] = 0  # visit 처리

    return 0


if __name__ == "__main__":
    N, M = map(int, input().split())
    graph = [i for i in range(101)]

    # ladders
    for _ in range(N):
        a, b = map(int, input().split())
        graph[a] = b

    # snakes
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a] = b

    print(bfs())
