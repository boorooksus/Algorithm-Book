from sys import stdin


def main():
    n, m = map(int, stdin.readline().split())
    arr = [[0] * (m + 1)] + \
          [([0] + list(map(int, stdin.readline().split()))) for _ in range(n)]

    res = -10000

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]

            for y in range(i):
                for x in range(j):
                    res = max(arr[i][j] - arr[y][j] - arr[i][x] + arr[y][x], res)

    print(res)


if __name__ == "__main__":
    main()
