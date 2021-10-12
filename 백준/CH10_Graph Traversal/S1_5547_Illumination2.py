from sys import stdin
from collections import deque


def bfs(row, col, w, h) -> None:
    dq = deque([(row, col)])
    visit[row][col] = 1

    while dq:
        cy, cx = dq.popleft()

        for i in range(6):
            ny, nx = cy + dy[cy % 2][i], cx + dx[cy % 2][i]

            if 0 <= ny <= h + 1 and 0 <= nx <= w + 1 and \
                    visit[ny][nx] == 0 and area[ny][nx] == 0:
                dq.append((ny, nx))
                visit[ny][nx] = True


dy = [[-1, 0, 1, 1, 0, -1], [-1, 0, 1, 1, 0, -1]]
dx = [[0, 1, 0, -1, -1, -1], [1, 1, 1, 0, -1, 0]]

w, h = map(int, stdin.readline().split())
area = [[0 for _ in range(w + 2)]]
for i in range(h):
    area.append([0] + list(map(int, stdin.readline().split())) + [0])
area.append([0 for _ in range(w + 2)])
visit = [[False for _ in range(w + 2)] for _ in range(h + 2)]

bfs(0, 0, w, h)

result = 0
for y in range(1, h + 1):
    for x in range(1, w + 1):
        if area[y][x] == 0:
            continue
        for k in range(6):
            ny, nx = y + dy[y % 2][k], x + dx[y % 2][k]
            if visit[ny][nx]:
                result += 1

print(result)
