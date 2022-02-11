from sys import stdin


def main():
    global r, c

    n, r, c = map(int, stdin.readline().split())

    ans = 0
    y, x = 0, 0

    while n > 0:
        if r < y + 2 ** (n - 1) \
                and c >= x + 2 ** (n - 1):
            ans += ((2 ** (n - 1)) ** 2)
            x += 2 ** (n - 1)

        elif r >= y + 2 ** (n - 1) \
                and c < x + 2 ** (n - 1):
            ans += ((2 ** (n - 1)) ** 2) * 2
            y += 2 ** (n - 1)

        elif r >= y + 2 ** (n - 1) \
                and c >= x + 2 ** (n - 1):
            ans += ((2 ** (n - 1)) ** 2) * 3
            y += 2 ** (n - 1)
            x += 2 ** (n - 1)

        n -= 1

    print(ans)


if __name__ == "__main__":
    main()
