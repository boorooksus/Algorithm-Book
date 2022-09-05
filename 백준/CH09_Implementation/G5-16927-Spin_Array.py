from sys import stdin
from collections import deque
input = lambda: stdin.readline().rstrip()


def rotate(y: int, x: int, n: int, m: int) -> None:
    dy, dx = [0, 1, 0, -1], [1, 0, -1, 0]
    cy, cx = y, x
    dq = deque()
    for d in range(4):
        for i in range([n, m][d % 2 == 0]):
            dq.append(arr[cy][cx])
            cy += dy[d]
            cx += dx[d]

    dq.rotate(-R)

    cy, cx = y, x
    for d in range(4):
        for i in range([n, m][d % 2 == 0]):
            arr[cy][cx] = dq.popleft()
            cy += dy[d]
            cx += dx[d]


if __name__ == "__main__":
    N, M, R = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    for i in range(min(N, M) // 2):
        rotate(i, i, N - 2 * i - 1, M - 2 * i - 1)

    for i in range(N):
        for j in range(M):
            print(arr[i][j], end=' ')
        print()

