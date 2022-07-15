from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()


def bfs() -> None:
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    dq = deque([(0, dest[0], dest[1])])
    arr[dest[0]][dest[1]] = 0

    while dq:
        dist, cy, cx = dq.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < n and 0 <= nx < m and arr[ny][nx] == 1:
                arr[ny][nx] = -(dist + 1)
                dq.append((dist + 1, ny, nx))


if __name__ == "__main__":
    n, m = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(n))

    dest = (0, 0)
    for i in range(n):
        if 2 in arr[i]:
            dest = (i, arr[i].index(2))
            break

    bfs()
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 1:
                arr[i][j] = 1
            print(-arr[i][j], end=' ')
        print()
