from sys import stdin
from collections import deque
from typing import List


board = []
row, col = 0, 0
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def bfs(y: int, x: int, visit: List[List[bool]]) -> deque[(int, int)]:
    if visit[y][x]:
        return deque()

    dq = deque([(y, x)])
    board[y][x] = -1
    visit[y][x] = True
    melted = deque()

    while dq:
        cy, cx = dq.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < row and 0 <= nx < col and not visit[ny][nx]:
                if board[ny][nx] == 0:
                    board[ny][nx] = -1
                    dq.append((ny, nx))
                elif board[ny][nx] == 1:
                    board[ny][nx] = 0
                    melted.append((ny, nx))
                visit[ny][nx] = True

    return melted


def main():
    def input():
        return stdin.readline().rstrip()
    global board, row, col

    row, col = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row)]

    time, cnts = -1, {}
    air = deque([(0, 0)])
    while True:
        visit = list([False] * col for _ in range(row))
        cnt = len(air)
        if cnt == 0:
            break

        cnts[time] = cnt
        for _ in range(cnt):
            y, x = air.popleft()
            air += bfs(y, x, visit)
        time += 1

    print(time)
    print(cnts[time - 1])


if __name__ == "__main__":
    main()
