from sys import stdin

n, m, res = 0, 0, 0
board = []
visit = []
dy = [0, -1, 0, -1,
      1, 0, 1, 0]
dx = [-1, 0, 1, 0,
      0, -1, 0, 1]


def bt(y: int, x: int, s: int) -> None:
    global n, m, res

    if x == m:
        x = 0
        y += 1

    if y == n:
        res = max(res, s)
        return

    if not visit[y][x]:
        visit[y][x] = True
        ns = 2 * board[y][x]

        for i in range(4):
            ay, ax = y + dy[i], x + dx[i]
            by, bx = y + dy[i + 4], x + dx[i + 4]

            if 0 <= ay < n and 0 <= ax < m and\
                    0 <= by < n and 0 <= bx < m and\
                    not visit[ay][ax] and not visit[by][bx]:
                visit[ay][ax] = True
                visit[by][bx] = True
                ns += board[ay][ax] + board[by][bx]
                bt(y, x + 1, s + ns)
                visit[ay][ax] = False
                visit[by][bx] = False
                ns -= board[ay][ax] + board[by][bx]

        visit[y][x] = False

    bt(y, x + 1, s)


def main():
    global n, m, visit, board

    n, m = map(int, stdin.readline().split())
    for _ in range(n):
        board.append(list(map(int, stdin.readline().split())))

    visit = [[False for _ in range(m)] for _ in range(n)]
    bt(0, 0, 0)
    print(res)


if __name__ == '__main__':
    main()
