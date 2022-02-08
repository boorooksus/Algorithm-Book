from sys import stdin
from collections import deque

r = c = n = 0
board = []
dq = deque()


def find_bombs() -> None:
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'O':
                dq.append((i, j))


def place_bombs() -> None:
    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = 'O'


def explode_bombs() -> None:
    dy = [0, 1, -1, 0, 0]
    dx = [0, 0, 0, 1, -1]

    while dq:
        cy, cx = dq.popleft()
        for i in range(5):
            ny, nx = cy + dy[i], cx + dx[i]
            if 0 <= ny < r and 0 <= nx < c:
                board[ny][nx] = '.'


def main():
    def input():
        return stdin.readline().rstrip()

    global r, c, n, board, dq

    r, c, n = map(int, input().split())
    board = [list(input()) for _ in range(r)]

    # n이 짝수인 경우, 모든 칸에 폭탄이 있음
    if n % 2 == 0:
        for i in range(r):
            print('O' * c)
        return

    # n이 홀수인 경우
    for time in range(2, n + 1, 2):
        find_bombs()
        place_bombs()
        if time == n:
            break
        explode_bombs()

    for i in range(r):
        print(''.join(board[i]))


if __name__ == "__main__":
    main()
