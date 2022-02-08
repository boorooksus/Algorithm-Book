from sys import stdin

r = c = n = 0
board = []


def place_bombs(time: int) -> None:
    bombs = ['O', '.', 'o', '.']

    for i in range(r):
        for j in range(c):
            if board[i][j] == '.':
                board[i][j] = bombs[time % 4]


def explode_bombs(time: int) -> None:
    dy = [1, -1, 0, 0]
    dx = [0, 0, 1, -1]
    bombs = ['.', 'o', '.', 'O']
    bomb = bombs[time % 4]

    for i in range(r):
        for j in range(c):
            if board[i][j] == bomb:
                board[i][j] = '.'
                for k in range(4):
                    ny, nx = i + dy[k], j + dx[k]
                    if 0 <= ny < r and 0 <= nx < c \
                            and board[ny][nx] != bomb:
                        board[ny][nx] = '.'


def main():
    def input():
        return stdin.readline().rstrip()

    global r, c, n, board

    r, c, n = map(int, input().split())
    for _ in range(r):
        board.append(list(char for char in input()))

    for time in range(2, n + 1):
        if time % 2 == 0:
            place_bombs(time)
        else:
            explode_bombs(time)

    res = []
    for i in range(r):
        res.append(''.join(board[i]))

    if n % 4 != 1:
        for i in range(r):
            res[i] = res[i].upper()

    for i in range(r):
        print(res[i])


if __name__ == "__main__":
    main()
