from sys import stdin
from collections import deque


def main():
    def input():
        return stdin.readline().rstrip()
    M, N = map(int, input().split())

    box = []
    cnt = 0
    riped = deque()
    for i in range(N):
        box.append(list(map(int, input().split())))
        for j in range(M):
            if box[i][j] == 0:
                cnt += 1
            elif box[i][j] == 1:
                riped.append((i, j, 1))

    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    res = 0
    while cnt > 0 and riped:
        cy, cx, res = riped.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < N and 0 <= nx < M and box[ny][nx] == 0:
                cnt -= 1
                riped.append((ny, nx, res + 1))
                box[ny][nx] = 1

    if not riped:
        res = -1
    print(res)


if __name__ == "__main__":
    main()
