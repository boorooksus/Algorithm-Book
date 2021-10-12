from sys import stdin
from collections import deque


def bfs(row, col, building, w, h) -> int:
    odd_dy = [-1, 0, 1, 1, 0, -1]
    odd_dx = [1, 1, 1, 0, -1, 0]
    even_dy = [-1, 0, 1, 1, 0, -1]
    even_dx = [0, 1, 0, -1, -1, -1]

    dq = deque([(row, col)])
    visit[row][col] = 1
    cnt = 0
    central_park = False

    while dq:
        cy, cx = dq.popleft()
        wall = 6

        for i in range(6):
            if cy % 2 == 1:
                ny, nx = cy + odd_dy[i], cx + odd_dx[i]
            else:
                ny, nx = cy + even_dy[i], cx + even_dx[i]

            if building == 0 and \
                    (ny <= 0 or ny > h or nx <= 0 or nx > w):
                central_park = True

            if 0 < ny <= h and 0 < nx <= w and \
                    area[ny][nx] == building:
                wall -= 1
                if visit[ny][nx] == 0:
                    dq.append((ny, nx))
                    visit[ny][nx] = 1
        cnt += wall

    return 0 if central_park else cnt


w, h = map(int, stdin.readline().split())
area = [[0 for _ in range(w + 1)]]
for i in range(h):
    area.append([0] + list(map(int, stdin.readline().split())))
visit = [[0 for _ in range(w + 1)] for _ in range(h + 1)]
result = 0

for i in range(1, h + 1):
    for j in range(1, w + 1):
        if area[i][j] == 1 and visit[i][j] == 0:
            result += bfs(i, j, 1, w, h)

        elif area[i][j] == 0 and visit[i][j] == 0:
            result -= bfs(i, j, 0, w, h)

print(result)
