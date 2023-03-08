from sys import stdin
input = lambda: stdin.readline().rstrip()


def divide_and_conquer(n: int, y: int, x: int, start: int):
    if n == 0:
        return start

    n -= 1
    if r < y + 2 ** n and c < x + 2 ** n:
        return divide_and_conquer(n, y, x, start)
    elif r < y + 2 ** n and c >= x + 2 ** n:
        return divide_and_conquer(n, y, x + 2 ** n, start + 2 ** (2 * n))
    elif r >= y + 2 ** n and c < x + 2 ** n:
        return divide_and_conquer(n, y + 2 ** n, x, start + 2 ** (2 * n + 1))
    else:
        return divide_and_conquer(n, y + 2 ** n, x + 2 ** n, start + 3 * (2 ** (2 * n)))


if __name__ == "__main__":
    N, r, c = map(int, input().split())

    print(divide_and_conquer(N, 0, 0, 0))
