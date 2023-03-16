from sys import stdin, setrecursionlimit
setrecursionlimit(10 ** 9)


def star(y: int, x: int, k: int) -> None:
    if k == 3:
        arr[y][x] = '*'

        arr[y + 1][x - 1], arr[y + 1][x + 1] = '*', '*'
        for i in range(x - 2, x + 3):
            arr[y + 2][i] = '*'
        return

    k //= 2
    star(y, x, k)
    star(y + k, x - k, k)
    star(y + k, x + k, k)


if __name__ == "__main__":
    N = int(stdin.readline().rstrip())

    arr = [[' '] * (N * 2) for _ in range(N)]
    star(0, N - 1, N)
    for i in range(N):
        print(''.join(arr[i]))


"""
join()을 이용한 출력이 더 빠르다
"""