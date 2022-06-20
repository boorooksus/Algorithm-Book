from sys import stdin


input = lambda: stdin.readline().rstrip()
dy = [1, -1, 0, 0]
dx = [0, 0, 1, -1]


def sol(r, c, cur):
    for i in range(r, r + 2):
        for j in range(c, c + 2):
            arr[i][j] = cur
    if r <= 2 ** k - y < r + 2 and c <= x - 1 < c + 2:
        arr[2 ** k - y][x - 1] = -1
    else:
        if r < 2:
            r += 1
        if c < 2:
            c += 1
        arr[r][c] = 1


if __name__ == "__main__":
    k = int(input())
    x, y = map(int, input().split())

    arr = list([1] * 2 ** k for _ in range(2 ** k))

    if k == 1:
        arr[2 ** k - y][x - 1] = -1

    else:
        cur = 2
        for i in range(2):
            for j in range(2):
                sol(i * 2, j * 2, cur)
                cur += 1

    for i in range(2 ** k):
        print(*arr[i], sep=' ')
