from sys import stdin


def main():
    n = int(stdin.readline())
    stats = list(map(int, stdin.readline().split()))

    res = 0
    start, end = 0, n - 1
    while start < end:
        res = max((end - start - 1) * min(stats[start], stats[end]), res)

        if stats[start] < stats[end]:
            start += 1
        else:
            end -= 1

    print(res)


if __name__ == "__main__":
    main()
