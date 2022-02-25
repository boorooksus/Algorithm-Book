from sys import stdin


def main():
    n, k = map(int, stdin.readline().split())

    start, end = 0, n // 2
    papers = 0
    while start <= end:
        mid = start + (end - start) // 2

        papers = (mid + 1) * (n - mid + 1)
        if papers < k:
            start = mid + 1
        elif papers > k:
            end = mid - 1
        else:
            break

    print(['NO', 'YES'][papers == k])


if __name__ == "__main__":
    main()
