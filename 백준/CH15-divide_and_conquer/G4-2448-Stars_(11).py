from sys import stdin


arr = []


def stars(y: int, x: int, size: int):
    global arr

    if size == 3:
        arr[y][x] = '*'
        arr[y + 1][x - 1], arr[y + 1][x + 1] = '*', '*'
        for i in range(5):
            arr[y + 2][x - 2 + i] = '*'
        return

    nsize = size // 2
    stars(y, x, nsize)
    stars(y + nsize, x - nsize, nsize)
    stars(y + nsize, x + nsize, nsize)


def main():
    global arr

    n = int(stdin.readline())
    arr = [[' '] * n * 2 for _ in range(n)]
    stars(0, n - 1, n)
    for i in range(n):
        print(''.join(arr[i]))


if __name__ == "__main__":
    main()
