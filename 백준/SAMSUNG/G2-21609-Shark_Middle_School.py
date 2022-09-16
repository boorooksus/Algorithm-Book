from sys import stdin
from collections import deque
from typing import List
input = lambda: stdin.readline().rstrip()


def bfs(sy: int, sx: int) -> (int, int, List[int]):
    dy, dx = [1, -1, 0, 0], [0, 0, 1, -1]
    dq = deque([[sy, sx]])
    group = arr[sy][sx]
    visit[sy][sx] = True
    block, rainbow = 1, 0
    rainbows = []
    temp = []

    while dq:
        cy, cx = dq.popleft()
        temp.append([cy, cx])
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < N and 0 <= nx < N and not visit[ny][nx] \
                    and (arr[ny][nx] == 0 or arr[ny][nx] == group):
                visit[ny][nx] = True
                block += 1
                if arr[ny][nx] == 0:
                    rainbow += 1
                    rainbows.append([ny, nx])
                dq.append([ny, nx])

    for y, x in rainbows:
        visit[y][x] = False

    return block, rainbow, temp


def gravity() -> None:
    for c in range(N):
        for r in range(N - 2, -1, -1):
            for k in range(r, N - 1):
                if arr[k][c] >= 0 and arr[k + 1][c] == -2:
                    arr[k][c], arr[k + 1][c] = -2, arr[k][c]
                else:
                    break


def rotate() -> None:
    global M, N, arr
    new_arr = list([0] * N for _ in range(N))

    for r in range(N):
        for c in range(N):
            new_arr[r][c] = arr[c][N - r - 1]

    arr = new_arr[:]


if __name__ == "__main__":
    N, M = map(int, input().split())
    arr = list(list(map(int, input().split())) for _ in range(N))

    score = 0
    while True:
        visit = list([False] * N for _ in range(N))
        crds = []

        max_cnt, max_rainbow, max_pivot = 0, 0, [-1, -1]
        for i in range(N):
            for j in range(N):
                if not visit[i][j] and arr[i][j] > 0:
                    a, b, c = bfs(i, j)
                    (max_cnt, max_rainbow, max_pivot, crds) = max((a, b, [i, j], c[:]), (max_cnt, max_rainbow, max_pivot, crds))
        if max_cnt < 2:
            break

        score += max_cnt ** 2

        for y, x in crds:
            arr[y][x] = -2

        gravity()
        rotate()
        gravity()

    print(score)

"""
5 3
0 0 0 0 1
-1 -1 0 -1 0
-1 -1 3 -1 -1
-1 -1 0 -1 -1
0 0 2 0 0
"""