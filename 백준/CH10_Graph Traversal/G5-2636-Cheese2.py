from sys import stdin
from collections import deque
from typing import List


def bfs(row: int, col: int, board: List[List[int]]) -> int:
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    visit = list([False] * col for _ in range(row))
    dq = deque([(0, 0)])
    visit[0][0] = True
    cnt = 0

    while dq:
        cy, cx = dq.popleft()
        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            if 0 <= ny < row and 0 <= nx < col and not visit[ny][nx]:
                if board[ny][nx] == 0:
                    dq.append((ny, nx))
                elif board[ny][nx] == 1:
                    board[ny][nx] = 0
                    cnt += 1
                visit[ny][nx] = True

    return cnt


def main():
    def input():
        return stdin.readline().rstrip()

    row, col = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(row)]

    time, cnts = 0, {}
    while True:
        cnts[time] = bfs(row, col, board)
        if cnts[time] == 0:
            break
        time += 1

    print(time)
    print(cnts[time - 1])


if __name__ == "__main__":
    main()
