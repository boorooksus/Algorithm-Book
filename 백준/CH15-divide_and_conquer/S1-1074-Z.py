from sys import stdin


r, c = 0, 0


def divide_conquer(y: int, x: int, order: int, size: int):
    if size == 1:
        if y == r and x == c:
            print(order)
        return

    dy = [0, 0, 1, 1]
    dx = [0, 1, 0, 1]

    nsize = size // 2
    for i in range(4):
        ny, nx = y + nsize * dy[i], x + nsize * dx[i]
        norder = order + ((size * size) // 4) * i
        if ny <= r < ny + nsize and nx <= c < nx + nsize:
            divide_conquer(ny, nx, norder, nsize)


def main():
    global r, c

    n, r, c = map(int, stdin.readline().split())
    divide_conquer(0, 0, 0, 2 ** n)


if __name__ == "__main__":
    main()
