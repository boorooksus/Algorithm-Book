from sys import stdin


if __name__ == "__main__":
    x, y = map(int, stdin.readline().rstrip().split())

    if x == y:
        print(0)
        exit()

    else:
        n = int((y - x) ** 0.5)

        if n ** 2 == y - x:
            print(2 * n - 1)
        else:
            diff = (y - x) - n ** 2
            if diff <= n:
                print(2 * n)
            else:
                print(2 * n + 1)
