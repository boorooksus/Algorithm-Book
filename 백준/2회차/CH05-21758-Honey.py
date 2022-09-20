from sys import stdin
input = lambda: stdin.readline().rstrip()


if __name__ == "__main__":
    N = int(input())
    arr = list(map(int, input().split()))

    # case1: 벌통이 가운데 있는 경우
    if N == 3:
        print(max(arr) * 2)
        exit(0)

    dp = [i for i in arr]
    for i in range(1, N):
        dp[i] += dp[i - 1]

    res = 0
    # case2: 벌통이 제일 왼쪽에 있는 경우
    for i in range(1, N - 1):
        res = max(dp[i - 1] - dp[0] + 2 * (dp[N - 1] - dp[i]), res)

    # case3: 벌통이 제일 오른쪽에 있는 경우
    for i in range(N - 2, 0, -1):
        res = max(dp[i - 1] * 2 + dp[N - 2] - dp[i], res)

    print(res)
