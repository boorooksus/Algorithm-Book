from sys import stdin
from collections import deque


def bfs():
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    visit = list(list(list(False for _ in range(M)) for _ in range(N)) for _ in range(2))
    dq = deque([(0, 0, 0, 0)])  # (row, col, sword, time)
    visit[0][0][0] = True

    while dq:
        cy, cx, sword, ct = dq.popleft()

        if ct >= T:
            break

        for i in range(4):
            ny, nx, ns = cy + dy[i], cx + dx[i], sword

            if 0 <= ny < N and 0 <= nx < M and \
                    not visit[ns][ny][nx]:
                if ns == 0 and arr[ny][nx] == 1:
                    continue
                if ny == N - 1 and nx == M - 1:
                    print(ct + 1)
                    return
                if arr[ny][nx] == 2:
                    ns = 1
                visit[ns][ny][nx] = True
                dq.append((ny, nx, ns, ct + 1))

    print("Fail")


if __name__ == "__main__":
    input = lambda: stdin.readline().rstrip()

    N, M, T = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    bfs()
