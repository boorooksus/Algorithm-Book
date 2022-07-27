from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = [[0] * (N + 1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]

    ans = -100_000_000
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            arr[i][j] += arr[i - 1][j] + arr[i][j - 1] - arr[i - 1][j - 1]
            k = 1
            while k <= i and k <= j:
                ans = max(arr[i][j] - arr[i][j - k] - arr[i - k][j] + arr[i - k][j - k], ans)
                k += 1

    print(ans)
